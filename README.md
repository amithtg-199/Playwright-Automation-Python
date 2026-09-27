# 🎭 Playwright Automation with Python

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Playwright-Automation-green.svg?logo=playwright)](https://playwright.dev/python/)
[![Pytest](https://img.shields.io/badge/Framework-Pytest-yellow.svg?logo=pytest)](https://docs.pytest.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-purple.svg)](https://opensource.org/licenses/MIT)

A comprehensive, hands-on repository covering End-to-End Web Automation Testing using **Playwright with Python** and **Pytest**, designed following industry best practices and Page Object Model (POM) architectural design.

---

## 📌 Repository Overview

This repository provides step-by-step implementations ranging from Python fundamentals to advanced enterprise-grade automation frameworks.

### 🗂 Project Structure

```text
Playwright-Automation-Python/
│
├── Playwright_into/                         # Playwright Introduction & Architecture Notes
│   └── Day0-Introdcuction-notes.pdf
│
├── Python_Basics/                           # Core Python Programming for Automation
│   ├── 1_py_variables_basics/               # Variables, Data Types & Type Casting
│   ├── 2_operators_concatinations/          # Arithmetic, Logical & Comparison Operators
│   ├── 3_format_conditional_statements/     # if / elif / else & String formatting
│   ├── 4_match_case_loops/                  # Match-case, while, for loops & loop control
│   ├── 5_strings_part1/                     # String slicing, indexing & methods
│   ├── 6_strings_part2/                     # Advanced string operations & assignments
│   ├── 7_collections_list/                  # Lists, indexing, methods & comprehension
│   ├── 8_collections_tuple_set/             # Tuples & Sets operations
│   ├── 9_collections_dict/                  # Dictionaries, key-value mappings
│   ├── 10_function_variable_scopes/         # Functions, arguments, scopes & return values
│   └── 11_file_operations/                  # File I/O (reading & writing files)
│
├── pytest_intro/                            # Pytest Framework Essentials
│   ├── Day1/                                # Pytest basics, test discovery, assertions
│   └── Day2/                                # Fixtures, markers, and parameterized tests
│
├── playwright_webautomation/                # Comprehensive Playwright Web Automation
│   ├── 1_pw-intro/                          # Playwright architecture, launch options & modes
│   ├── 2_pw_builtin_locators/               # get_by_role, get_by_text, get_by_label, etc.
│   ├── 3_css_locators/                      # CSS Selector strategies & custom selectors
│   ├── 4_xpath_locators/                    # Relative, absolute & axes XPath strategies
│   ├── 5_textbox_radiobutton_checkbox/      # Form input fields, state assertions, check/uncheck
│   ├── 6_dropdowns/                         # Standard select dropdowns & multi-selects
│   ├── 7_bootstraps_hidden_dropdowns/       # Bootstrap, auto-suggest & dynamically hidden dropdowns
│   ├── 8_static_webtables/                  # Extracting rows, columns, table assertions
│   ├── 9_dynmaicwebtables_pagination/       # Dynamic tables, pagination traversal & search
│   ├── 10_jquery_bootstrap_date_pcikers/    # Date pickers (jQuery, Bootstrap, Booking.com)
│   ├── 11_dialogues_frames/                 # Alert, Confirm, Prompt handling & nested iFrames
│   ├── 12_mouse_actions/                    # Hover, right click, double click, drag and drop
│   ├── 13_keyboard_actions_file_uploads/    # Keyboard shortcuts, single & multiple file upload/download
│   ├── 14_browser_context_popups_tabs/      # Browser contexts, multiple tabs, popup auth
│   ├── 15_record_videos_screenshots_flaky_anlysis/ # Screenshots, video capture, tracing & debugging
│   ├── 16_data_driven_testing/              # Data-Driven Testing (DDT) with CSV & Excel
│   ├── 17_pytest_allure_reports/            # Allure report integration & visualization
│   ├── 18_POM_pattern/                      # Page Object Model design principles
│   ├── 19_POM_Framework_part1/              # Enterprise POM Framework implementation - Part 1
│   └── 20_POM_Framework_Part2/              # Enterprise POM Framework implementation - Part 2
│
├── uploads/                                 # Sample test files for upload/download automation
│   ├── test.pdf
│   ├── text.csv
│   └── text1.txt
│
└── README.md
```

---

## 🚀 Key Features & Highlights

- **Modern Locator Strategies**: Full coverage of Playwright's user-facing built-in locators (`get_by_role`, `get_by_label`, `get_by_placeholder`, etc.) alongside CSS & XPath.
- **Advanced UI Interactions**: Handling complex UI patterns such as auto-suggest dropdowns, multi-level iframes, JavaScript alerts/confirms, drag-and-drop, and dynamic web tables with pagination.
- **Robust Multi-Page Handling**: Managing independent `BrowserContext`, isolated sessions, new tabs, and popup windows.
- **Debugging & Diagnostics**: Playwright Tracing, step-by-step video recordings, full-page screenshots, and flaky test analysis.
- **Data-Driven Automation**: Parameterized test executions reading datasets from CSV and Excel.
- **Enterprise POM Architecture**: Modular Page Object Model separation for clean maintenance, reusable components, and scalability.
- **Rich Reporting**: Pytest-HTML and Allure Reporting configurations.

---

## 🛠️ Prerequisites & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/amithtg-199/Playwright-Automation-Python.git
cd Playwright-Automation-Python
```

### 2. Create and Activate Virtual Environment
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies & Playwright Browsers
```bash
pip install pytest playwright pytest-playwright pytest-html allure-pytest pandas openpyxl
playwright install
```

---

## 🧪 Running Tests

### Run all tests with Pytest:
```bash
pytest
```

### Run tests in Headed Mode (see browser UI):
```bash
pytest --headed
```

### Run tests on specific browser (Chromium, Firefox, WebKit):
```bash
pytest --browser chromium --headed
pytest --browser firefox --headed
pytest --browser webkit --headed
```

### Run a specific test module:
```bash
pytest playwright_webautomation/5_textbox_radiobutton_checkbox/test_checkboxes.py -v
```

### View Playwright Trace:
```bash
playwright show-trace playwright_webautomation/15_record_videos_screenshots_flaky_anlysis/trace_sample.zip
```

---

## 📊 Generating Allure Reports

1. Execute tests specifying the Allure results directory:
   ```bash
   pytest --alluredir=allure-results
   ```
2. Serve the interactive Allure report:
   ```bash
   allure serve allure-results
   ```

---

## 👤 Author

- **Amith T G** ([@amithtg-199](https://github.com/amithtg-199))

---

## 📄 License

This repository is licensed under the [MIT License](LICENSE).
