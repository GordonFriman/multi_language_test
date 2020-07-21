import time


# link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_basket_button(browser, language):
    browser.get(f'http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/')
    time.sleep(3)
    assert browser.find_element_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket")
