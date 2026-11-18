import time
from playwright.sync_api import Page
from pages.signup_page import SignupPage


def test_full_partner_signup_workflow(page: Page):
    signup = SignupPage(page)

    timestamp = int(time.time())

    test_data = {

        "first_name": f"Quality_{timestamp}",
        "last_name": f"Thapa_{timestamp}",
        "email": f"qa.tester.{timestamp}@example.com",
        "phone": "9813475626",
        "password": "Password123!",
        "confirm_password": "Password123!",

        "agency_name": f"Anjali Test Agency_{timestamp}",
        "role": "QA Tester",
        "agency_email": f"agency.{timestamp}@example.com",
        "website": "https://example.com",
        "address": "Kathmandu, Nepal",

        "students": "50",
        "focus": "Undergraduate Admissions",
        "metrics": "90",

        "reg_number": f"REG-2026-{timestamp}"
    }

    signup.load_application()

    signup.fill_account_setup(
        test_data["first_name"],
        test_data["last_name"],
        test_data["email"],
        test_data["phone"],
        test_data["password"],
        test_data["confirm_password"]
    )

    signup.fill_agency_details(
        test_data["agency_name"],
        test_data["role"],
        test_data["agency_email"],
        test_data["website"],
        test_data["address"]
    )

    signup.fill_professional_experience(
        test_data["students"],
        test_data["focus"],
        test_data["metrics"]
    )

    signup.complete_verification_and_submit(
        test_data["reg_number"]
    )

    signup.verify_successful_submission()
