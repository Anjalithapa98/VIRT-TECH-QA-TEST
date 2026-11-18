# Vrit Technologies – QA Automation Assessment

# Project Overview

This project automates the Partner Signup workflow of the Vrit Technologies Authorized Partner application using Python, Playwright, and Pytest.

The automation follows the Page Object Model (POM) design pattern to keep page locators and test execution logic organized and maintainable.

# Application Under Test

**Application:** Vrit Technologies
**URL:** https://authorized-partner.vercel.app/

# Technologies Used

-Python
-Playwright
-Pytest
-Pytest-HTML
-Page Object Model (POM)

# Project Structure

VIRT TECH/
pages/
   __init__.py
   signup_page.py
tests/
    test_signup.py
README.md
requirements.txt
report.html

# Test Scenario

The automation covers the following signup workflow:

1. Navigate to the application.
2. Open the signup form.
3. Complete Account Setup.
4. Enter Agency Details.
5. Complete Professional Experience.
6. Complete Verification and Preferences.
7. Submit the application.
8. Verify the successful submission message.

# Installation and Setup

## 1. Clone the repository

bash
git clone YOUR_GITHUB_REPOSITORY_URL


## 2. Navigate to the project directory

bash
cd VIRT TECH


## 3. Install dependencies

bash
pip install -r requirements.txt


## 4. Install Playwright browser

bash
python -m playwright install chromium


## Running the Tests

Run the test in headed mode:

bash
python -m pytest tests/test_signup.py -v --headed


Run the test in headless mode:

bash
python -m pytest tests/test_signup.py -v


## Test Report

Generate an HTML test report using:

bash
python -m pytest tests/test_signup.py -v --html=report.html --self-contained-html

Open `report.html` in a browser to view the execution results.

## Design Pattern

This project follows the Page Object Model (POM):
signup_page.py: Contains page locators and signup workflow methods.
test_signup.py: Contains the test scenario and final assertion.

AUTHOR
Anjali Thapa
