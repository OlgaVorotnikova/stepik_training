#import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_is_present(browser):
    browser.get(link)
#    time.sleep(15)
    buttons = browser.find_elements_by_css_selector("button.btn.btn-lg.btn-primary.btn-add-to-basket")
    assert len(buttons) > 0, "Button was not found!"