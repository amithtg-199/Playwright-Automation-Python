# 🛒 OpenCart Test Automation Framework (Playwright + Pytest)

A robust, scalable, enterprise-grade test automation framework built for the **OpenCart** e-commerce web application using **Playwright** with **Python** and **Pytest**.

---

## 🏗️ Architecture & Design Pattern

The framework strictly adheres to the **Page Object Model (POM)** design pattern with complete separation between page elements, business actions, test data, and test scripts.

```text
22_pytest_framework_opencart/
├── config/
│   ├── .env.example              # Sample environment configurations
│   ├── config.py                 # Core path and test configuration constants
│   └── environments.py           # Multi-environment config loader (dev, uat, preprod)
├── pages/                        # Page Object Model classes
│   ├── home_page.py              # Navigation, headers, search bar & currencies
│   ├── login_page.py             # User login locators & interactions
│   ├── logout_page.py            # Account logout actions & confirmation checks
│   ├── my_account_page.py        # Account dashboard options & validations
│   ├── product.py                # Product detail page, quantity, add to cart
│   ├── registration_page.py      # Account registration form handling
│   ├── search_results.py         # Product search listings & filter validations
│   └── shoping_cart_page.py      # Cart view, item checkout & price checks
├── testdata/                     # Test data fixtures
│   ├── logindata.csv             # CSV dataset
│   ├── logindata.json            # JSON dataset
│   └── logindata.xlsx            # Excel dataset
├── tests/                        # Test Suites
│   ├── test_add_product_to_cart.py
│   ├── test_login.py
│   ├── test_registration.py
│   ├── test_search_product.py
│   └── test_view_cart.py
├── utility/                      # Framework Utilities
│   ├── load_test_data.py         # Universal data loader (CSV, JSON, Excel)
│   ├── logging_config.py         # Logger setup with console & file rotation
│   └── random_data_generator.py  # Dynamic synthetic test data (Faker)
├── conftest.py                   # Pytest hooks, fixtures & browser setup
├── pytest.ini                    # Pytest flags, markers, timeouts & options
├── requirements.txt              # Project dependencies
└── Readme.md                     # Documentation
```

---

## ⚡ Features

- **Page Object Model (POM)**: Isolated, reusable component & page definitions.
- **Multi-Environment Ready**: Seamless switching between `dev`, `uat`, and `preprod` environments via typed dataclasses.
- **Data-Driven Testing (DDT)**: Integrated data loaders for CSV, JSON, and Excel formats.
- **Synthetic Data Generation**: Realistic user data creation using `Faker`.
- **Pytest Markers**: Tag tests using `@pytest.mark.sanity`, `@pytest.mark.regression`, `@pytest.mark.datadriven`, `@pytest.mark.end_to_end`, or `@pytest.mark.smoke`.
- **Debugging & Artifacts**: Automatic capture of failure screenshots, video recordings, and Playwright execution traces (`retain-on-failure`).
- **Allure & HTML Reporting**: Comprehensive test execution metrics and visual dashboards.

---

## 🚀 Setup & Execution

### 1. Install Dependencies
```bash
pip install -r requirements.txt
playwright install
```

### 2. Configure Environment
Copy `.env.example` in `config/` to `.env` and configure appropriate credentials and URLs:
```bash
cp config/.env.example config/.env
```

### 3. Run Tests

- **Run Sanity Suite**:
  ```bash
  pytest -m "sanity"
  ```

- **Run Regression Suite**:
  ```bash
  pytest -m "regression"
  ```

- **Run in Headed Mode**:
  ```bash
  pytest --headed
  ```

- **Run on Specific Environment**:
  ```bash
  pytest --env=uat
  ```

- **Run in Parallel**:
  ```bash
  pytest -n auto
  ```

### 4. View Reports
```bash
allure serve reports/allure-results
```
