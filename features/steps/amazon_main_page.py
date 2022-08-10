from selenium.webdriver.common.by import By
from behave import given, when, then




ORDERS_BTTN = (By.ID, 'nav-link-accountList-nav-line-1')
INPUT_BOX = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.ID, 'nav-search-submit-button')
HAM_MENU = (By.ID, 'nav-hamburger-menu')
FOOTER_LINKS = (By.CSS_SELECTOR, 'table.navFooterMoreOnAmazon td a')
BEST_SELLERS_LINKS = (By.CSS_SELECTOR, "div._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq ul li")



@given ('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com')


@when ('Search for {search_word} on amazon')
def search_product(context, search_word):
    context.driver.find_element(*INPUT_BOX).send_keys(search_word)
    context.driver.find_element(*SEARCH_ICON).click()


@when('Click Orders')
def click_orders(context):
        context.driver.find_element(*ORDERS_BTTN).click()

@when ('Click on cart')
def search_product(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href*='/gp/cart/view.html?']").click()

@then('Verify hamburger menu is present')
def verify_hamburger_menu(context):
    context.driver.find_element(*HAM_MENU)

@then('Verify {expected_amount} footer links are shown')
def verify_footer_links_present(context, expected_amount):
    expected_amount = int(expected_amount) # '38' => 38
    links = context.driver.find_elements(*FOOTER_LINKS)

    assert len(links) == expected_amount, \
    f'Expected {expected_amount} links but got {len(links)}'


@when('Click Best Sellers Button')
def best_sellers_button(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href='/gp/bestsellers/?ref_=nav_cs_bestsellers']").click()


