import pytest
import allure
from pathlib import Path
from config.environments import ENV_CONFIG
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.home_page import HomePage
import logging
from utility.logging_config import DailyFileHandler

log = logging.getLogger(__name__)


# ========================================================================
# PYTEST + PLAYWRIGHT TEST CONFIGURATION FILE
# ========================================================================
# This file provides:
# 1. Command-line options (browser, base URL, video, screenshots, etc.)
# 2. Hooks to track test results
# 3. Fixtures for browser setup and teardown
# 4. Screenshot, video, and trace attachments to Allure reports
# 5. LoginPage exported as page fixture
# ========================================================================


# ----------------------------------------------------------------------------
# STEP 1: ADD COMMAND LINE OPTIONS
# ----------------------------------------------------------------------------
def pytest_addoption(parser):
    """
    Adds command line options for test configuration.
    You can override these when running pytest or store defaults in pytest.ini.
    """
    #parser.addoption("--browser", default="chromium", help="Browser: chromium, firefox, webkit")
    parser.addoption("--env", default="uat", help="Test environment: dev, uat, preprod")
    #parser.addoption("--headed", action="store_true", help="Run in headed (visible) mode")
    #parser.addoption("--base-url", default="https://naveenautomationlabs.com/opencart", help="Base URL for tests")
    #parser.addoption("--video", default="retain-on-failure", help="Record video: on, off, retain-on-failure")
    #parser.addoption("--screenshot", default="only-on-failure", help="Take screenshot: on, off, only-on-failure")
    #parser.addoption("--tracing", default="retain-on-failure", help="Tracing: on, off, retain-on-failure")


# ----------------------------------------------------------------------------
# STEP 2: GET CONFIGURATION VALUE (CMDLINE OR pytest.ini)
# ----------------------------------------------------------------------------
def get_config_value(config, option_name):
    """
    Helper to read configuration values.
    Tries to get from command line first, otherwise from pytest.ini.
    Supports both string and boolean options.
    """
    # Try command-line first
    cmd_value = config.getoption(option_name)
    if cmd_value is not None:
        return cmd_value

    # Fallback to pytest.ini
    if option_name == "headed":
        ini_value = config.getini(option_name)
        return ini_value.lower() == "true" if isinstance(ini_value, str) else ini_value
    else:
        return config.getini(option_name)

# ----------------------------------------------------------------------------
# STEP 3: HOOK TO TRACK TEST RESULTS (PASS/FAIL)
# ----------------------------------------------------------------------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Captures the test result (pass/fail/skip) after each test.
    This is used later to decide whether to take screenshots or save traces.
    """
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)


# ----------------------------------------------------------------------------
# STEP 4: Load Env Variables based on env(uat, dev, preprod)
# ----------------------------------------------------------------------------
@pytest.fixture(scope="session")
def environment(request):
    """
    Used to capture the env type under test example uat, preprod, dev and send
    their base_url, username, password
    """
    env = get_config_value(request.config, "env")
    if not env:
        message = (
        "Environment is not configured. "
        "Use --env=dev, --env=uat or --env=preprod."
    )
        log.error(message)
        raise ValueError(message)
    env = env.lower()

    if env not in ENV_CONFIG:
        message = (f"Unsupported environment: {env}. " f"Supported: {list(ENV_CONFIG.keys())}")
        log.error(message)
        raise ValueError(message)

    selected_environment = ENV_CONFIG[env]
    log.info(
        f"\n[ENV] Selected Environment: {selected_environment.name}"
    )
    log.info(
        f"[ENV] Selected Base URL: {selected_environment.base_url}"
    )

    return selected_environment

# ----------------------------------------------------------------------------
# STEP 5: Allure Report Environment config
# ----------------------------------------------------------------------------

@pytest.fixture(scope="session", autouse=True)
def allure_environment(environment):
    """
    Creates Allure environment.properties once per pytest run.
    """

    allure_results = Path("reports/allure-results")
    allure_results.mkdir(parents=True, exist_ok=True)

    environment_file = allure_results / "environment.properties"

    environment_file.write_text(
        f"Environment={environment.name}\n"
        f"Base_URL={environment.base_url}\n",
        encoding="utf-8"
    )

# ----------------------------------------------------------------------------
# STEP 6: Pytest hook to call the logging handler to log the output
# ----------------------------------------------------------------------------

def pytest_configure(config):

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    if not any(
        isinstance(handler, DailyFileHandler)
        for handler in logger.handlers
    ):
        file_handler = DailyFileHandler(
            log_dir="loggers/logs",
            retention_days=7
        )
        file_handler.setLevel(logging.DEBUG)
        logger.addHandler(file_handler)
    logging.getLogger("faker").setLevel(logging.WARNING)

# ----------------------------------------------------------------------------
# STEP 7: FIXTURE 1 - BROWSER CONTEXT SETUP
# ----------------------------------------------------------------------------
@pytest.fixture(scope="function")
def browser_context(request):
    """
    Creates and manages the Playwright browser context.
    - Reads configuration (browser, headed mode, video settings)
    - Starts the Playwright browser
    - Enables video recording if configured
    - Cleans up automatically after each test
    """
    # Read configuration values
    browser_name = get_config_value(request.config, "browser")
    headed_flag = get_config_value(request.config, "headed")
    video_option = get_config_value(request.config, "video")

    log.info(f"[Playwright Init] Starting browser: {browser_name}")
    log.info(f"[Playwright Init] Headless mode: {not headed_flag} (headed={headed_flag})")

    # Start Playwright
    playwright = sync_playwright().start()

    if isinstance(browser_name, list):
        browser_name = browser_name[0]

    browser_name = browser_name.lower()

    # Launch the specified browser
    if browser_name == "chromium":
        browser = playwright.chromium.launch(headless=not headed_flag)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=not headed_flag)
    elif browser_name == "webkit":
        browser = playwright.webkit.launch(headless=not headed_flag)
    else:
        message = (f"[FAIL] Unsupported browser: {browser_name}")
        log.error(message)
        raise ValueError(message)

    # Create a browser context (optionally with video recording)
    if video_option in ["on", "retain-on-failure"]:
        context = browser.new_context(record_video_dir="reports/videos")
    else:
        context = browser.new_context()

    # Yield the context for use in tests
    yield context

    # Clean up after the test
    log.info("[TEARDOWN] Closing browser context and stopping Playwright...")
    context.close()
    browser.close()
    playwright.stop()


# ----------------------------------------------------------------------------
# STEP 8: FIXTURE 2 - PAGE CREATION AND TEST ARTIFACT MANAGEMENT
# ----------------------------------------------------------------------------
@pytest.fixture(scope="function")
def page(request, browser_context, environment):
    """
    Creates a new browser page for each test.
    - Navigates to the base URL
    - Starts tracing (if enabled)
    - Captures screenshots, traces, and videos for failed tests
    - Attaches all artifacts to Allure report
    """
    # Read test configuration
    base_url = environment.base_url
    screenshot_option = get_config_value(request.config, "screenshot")
    tracing_option = get_config_value(request.config, "tracing")
    video_option = get_config_value(request.config, "video")

    log.info(f"[Page Init] Navigating to: {base_url}")

    # Start tracing if enabled
    if tracing_option in ["on", "retain-on-failure"]:
        log.info("[TRACE] Tracing enabled - capturing screenshots and actions")
        browser_context.tracing.start(screenshots=True, snapshots=True, sources=True)

    # Create and navigate to base URL
    page = browser_context.new_page()
    page.goto(base_url)

    # Yield the page to the test
    yield page

    # ------------------------------------------------------------------------
    # After the test: manage artifacts (screenshots, videos, traces)
    # ------------------------------------------------------------------------
    test_name = request.node.name
    test_failed = hasattr(request.node, "rep_call") and request.node.rep_call.failed

    log.info(f"[RESULT] Test '{test_name}' result: {'[FAIL]' if test_failed else '[PASS]'}")

    # Save and attach trace
    if tracing_option in ["on", "retain-on-failure"]:
        trace_path = f"reports/traces/{test_name}_trace.zip"
        browser_context.tracing.stop(path=trace_path)
        log.info(f"Trace saved: {trace_path}")

        # Attach trace to Allure report if test failed
        if test_failed:
            allure.attach.file(
                trace_path,
                name=f"{test_name}_trace",
                attachment_type=allure.attachment_type.ZIP
            )
            log.info("Trace attached to Allure report")

    # Take screenshot if test failed
    if test_failed and screenshot_option in ["on", "only-on-failure"]:
        screenshot_path = f"reports/screenshots/{test_name}.png"
        page.screenshot(path=screenshot_path)
        log.info(f"Screenshot saved: {screenshot_path}")

        # Attach to Allure report
        allure.attach.file(
            screenshot_path,
            name=f"{test_name}_screenshot",
            attachment_type=allure.attachment_type.PNG
        )
        log.info("Screenshot attached to Allure report")

    # Attach video if available and test failed
    if test_failed and video_option in ["on", "retain-on-failure"]:
        video_path = page.video.path() if page.video else None
        if video_path and Path(video_path).exists():
            allure.attach.file(
                video_path,
                name=f"{test_name}_video",
                attachment_type=allure.attachment_type.WEBM
            )
            log.info("Video attached to Allure report")

# ----------------------------------------------------------------------------
# STEP 9: Login Fixture to send username password values based on ENV type
# ----------------------------------------------------------------------------
@pytest.fixture(scope="function")
def logged_in_page(page, environment):
    """
    Returns Logged in MyAccount Page to tests
    """
    login_page = LoginPage(page)
    home_page = HomePage(page)

    home_page.click_my_account()
    home_page.click_login()

    return login_page.login_with_credentails(email=environment.username, password=environment.password)