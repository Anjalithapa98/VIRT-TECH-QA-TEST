import re
from playwright.sync_api import Page, expect


class SignupPage:
    def __init__(self, page: Page):
        self.page = page

        self.start_button = page.get_by_role(
            "link", name=re.compile(r"get started", re.IGNORECASE)
        ).get_by_role("button", name=re.compile(r"get started", re.IGNORECASE))

        self.next_button = page.get_by_role(
            "button",
            name=re.compile(r"next|continue", re.IGNORECASE)
        )

        self.submit_button = page.get_by_role(
            "button",
            name=re.compile(r"submit|finish|complete", re.IGNORECASE)
        )

        self.first_name_input = page.get_by_label(
            re.compile(r"first name", re.IGNORECASE)
        )
        self.last_name_input = page.get_by_label(
            re.compile(r"last name", re.IGNORECASE)
        )
        self.email_input = page.get_by_label(
            re.compile(r"email address", re.IGNORECASE)
        )
        self.phone_input = page.get_by_label(
            re.compile(r"phone number", re.IGNORECASE)
        )
        self.password_input = page.locator('input[type="password"]').nth(0)
        self.confirm_password_input = page.locator(
            'input[type="password"]'
        ).nth(1)

        self.agency_name_input = page.get_by_placeholder(
            re.compile(r"agency name", re.IGNORECASE)
        )
        self.role_in_agency_input = page.get_by_placeholder(
            re.compile(r"role in agency|your role", re.IGNORECASE)
        )
        self.agency_email_input = page.get_by_placeholder(
            re.compile(r"agency email", re.IGNORECASE)
        )
        self.website_input = page.get_by_placeholder(
            re.compile(r"website", re.IGNORECASE)
        )
        self.address_input = page.get_by_placeholder(
            re.compile(r"address", re.IGNORECASE)
        )

        self.years_experience_input = page.get_by_text(
            "1 year", exact=False
        )
        self.students_recruited_input = page.get_by_placeholder(
            re.compile(r"approximate number|number of students", re.IGNORECASE)
        )
        self.focus_area_input = page.get_by_placeholder(
            re.compile(r"focus area|undergraduate admissions", re.IGNORECASE)
        )
        self.success_metrics_input = page.get_by_placeholder(
            re.compile(r"90%|success metrics", re.IGNORECASE)
        )

        self.career_counseling_checkbox = page.get_by_label(
            re.compile(r"career counseling", re.IGNORECASE)
        )
        self.admission_applications_checkbox = page.get_by_label(
            re.compile(r"admission applications", re.IGNORECASE)
        )
        self.visa_processing_checkbox = page.get_by_label(
            re.compile(r"visa processing", re.IGNORECASE)
        )
        self.test_preparation_checkbox = page.get_by_label(
            re.compile(r"test preparation", re.IGNORECASE)
        )

        self.registration_number_input = page.get_by_label(
            re.compile(r"business registration number", re.IGNORECASE)
        )
        self.certification_input = page.get_by_label(
            re.compile(r"certification details", re.IGNORECASE)
        )

        self.universities_checkbox = page.get_by_label(
            re.compile(r"universities", re.IGNORECASE)
        )
        self.colleges_checkbox = page.get_by_label(
            re.compile(r"colleges", re.IGNORECASE)
        )
        self.vocational_checkbox = page.get_by_label(
            re.compile(r"vocational school", re.IGNORECASE)
        )
        self.other_institution_checkbox = page.get_by_label(
            re.compile(r"other", re.IGNORECASE)
        )

        self.file_uploads = page.locator('input[type="file"]')

        self.terms_checkbox = page.get_by_role("checkbox").filter(
            has=page.get_by_text(
                re.compile(r"terms|conditions", re.IGNORECASE)
            )
        )

        self.success_indicator = page.get_by_text(
            re.compile(r"success|thank you|submitted", re.IGNORECASE)
        )

    def load_application(self):
        self.page.goto("https://authorized-partner.vercel.app/")
        self.page.wait_for_load_state("domcontentloaded")

    def fill_account_setup(
        self,
        first_name: str,
        last_name: str,
        email: str,
        phone: str,
        password: str,
        confirm_password: str
    ):
        self.start_button.click()

        expect(self.first_name_input).to_be_visible(timeout=15000)

        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.email_input.fill(email)
        self.phone_input.fill(phone)
        self.password_input.fill(password)
        self.confirm_password_input.fill(confirm_password)

        self.next_button.click()

    def fill_agency_details(
        self,
        agency_name: str,
        role: str,
        agency_email: str,
        website: str,
        address: str
    ):
        expect(self.agency_name_input).to_be_visible(timeout=15000)

        self.agency_name_input.fill(agency_name)
        self.role_in_agency_input.fill(role)
        self.agency_email_input.fill(agency_email)
        self.website_input.fill(website)
        self.address_input.fill(address)

        self.next_button.click()

    def fill_professional_experience(
        self,
        students: str,
        focus: str,
        metrics: str
    ):
        expect(self.students_recruited_input).to_be_visible(timeout=15000)

        self.students_recruited_input.fill(students)
        self.focus_area_input.fill(focus)
        self.success_metrics_input.fill(metrics)

        self.career_counseling_checkbox.check()
        self.admission_applications_checkbox.check()
        self.visa_processing_checkbox.check()
        self.test_preparation_checkbox.check()

        self.next_button.click()

    def complete_verification_and_submit(
        self,
        reg_number: str
    ):
        expect(self.registration_number_input).to_be_visible(
            timeout=15000
        )

        self.registration_number_input.fill(reg_number)

        self.universities_checkbox.check()
        self.colleges_checkbox.check()
        self.vocational_checkbox.check()

        self.next_button.click()

    def verify_successful_submission(self):
        expect(self.success_indicator).to_be_visible(timeout=15000)