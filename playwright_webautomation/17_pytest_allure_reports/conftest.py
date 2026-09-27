from pathlib import Path
import pytest
from slugify import slugify
import allure
import os

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    
    if report.when == "call":
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            
            # Check if 'page' or 'context' is available in the test
            if "page" in item.funcargs:
                page = item.funcargs["page"]
                context = page.context
                
                # --- 1. Screenshot ---
                screenshot_dir = Path("screenshots")
                screenshot_dir.mkdir(exist_ok=True)
                screen_file = str(screenshot_dir / f"{slugify(item.nodeid)}.png")
                page.screenshot(path=screen_file)
                
                if pytest_html:
                    extra.append(pytest_html.extras.png(screen_file))
                
                allure.attach.file(
                    screen_file,
                    name="Failure Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )
                
                # --- 2. Video ---
                try:
                    video = page.video
                    if video:
                        video_path = video.path()
                        if video_path and Path(video_path).exists():
                            allure.attach.file(
                                video_path,
                                name="Failure Video",
                                attachment_type=allure.attachment_type.WEBM
                            )
                except Exception as e:
                    print(f"Could not attach video: {e}")

                # --- 3. Trace (.zip) ---
                try:
                    os.makedirs("traces", exist_ok=True)
                    trace_file = Path("traces") / f"{slugify(item.nodeid)}_trace.zip"
                    
                    # Stop tracing and save it directly to the traces folder
                    context.tracing.stop(path=str(trace_file))
                    
                    if trace_file.exists():
                        allure.attach.file(
                            str(trace_file),
                            name="Playwright Trace",
                            attachment_type=allure.attachment_type.ZIP
                        )
                except Exception as e:
                    print(f"Could not attach trace: {e}")

    report.extra = extra