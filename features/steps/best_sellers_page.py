from selenium.webdriver.common.by import By
from behave import given, when, then

BEST_SELLERS_LINKS = (By.CSS_SELECTOR, "div._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq ul li")

@given('Open Amazon Best Sellers page')
def open_best_sellers(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('Verify {expected_amount} Best Sellers Links')
def verify_best_sellers_links(context, expected_amount):
    expected_amount = int(expected_amount)
    links = context.driver.find_elements(*BEST_SELLERS_LINKS)

    assert len(links) == expected_amount, \
        f'Expected {expected_amount} links but got {len(links)}'