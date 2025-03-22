import time

from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    time.sleep(15)
    page.set_default_timeout(40000)
    page.wait_for_load_state()
    page.locator("text='Log In'").click()
    time.sleep(30)
    # page.click("button:has-text('Log In')", timeout=60000)
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_test_id("siteMembersDialogLayout").get_by_test_id("buttonElement").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").fill("testingit@gmail.com")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("123123123")
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
    page.get_by_role("button", name="testingit account menu").click()
    page.get
    assert page.is_visible("text=My Orders")
    page.get_by_role("link", name="My Orders").click()
    # pa

    # # ---------------------
    # context.close()
    # browser.close()


with sync_playwright() as playwright:
    run(playwright)
