import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://etrendgigs.com/user/login?signup",wait_until="domcontentloaded",timeout=60000)
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("mi_techy")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("854112")
    page.get_by_role("button", name="Login").click()
    page.get_by_text("×").nth(2).click()
    page.get_by_role("button", name="Earn More").click()
    page.get_by_role("button", name="Go To Social Task    ").click()
    page.get_by_role("button", name="Activate Now!").click()
    page.goto("chrome-error://chromewebdata/")
    page.get_by_role("button", name="Reload").click()
    page.locator("#buttons").click()
    page.get_by_role("button", name="Reload").click()
    page.goto("chrome-error://chromewebdata/")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
