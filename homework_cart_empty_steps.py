from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target main page')
def go_to_target(context):
    context.driver.get('https://www.target.com/')

@when('Click on cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()
    sleep(6)
    # context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")

@then('Verify your cart is empty message is shown')
def verify_cart_is_empty(context):
    expected_text = 'Your cart is empty'
    actual_element = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")
    actual_text = actual_element.text
    print(actual_text)
    assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'
    #
    print('Test case passed')
