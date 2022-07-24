from selenium.webdriver.common.by import By
from behave import given, when, then

@given ('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com')


@when ('Search for coffee on amazon')
def search_product(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('coffee')
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()

@then ('Results for coffee shown')
def verify_search_results(context):
    expected_results ='"coffee"'
    actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    assert expected_results == actual_result, f'Expected{expected_results} but got {actual_result}'

