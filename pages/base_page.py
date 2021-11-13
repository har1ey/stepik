import math

from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver

from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser: WebDriver, url: str):
        self.browser = browser
        self.url = url
        # не используем - timeout используется в проверке наличия элемента
        # self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    # проверка с ожиданием timeout на наличие элемента
    def is_element_present(self, how, what, timeout=4):
        try:
            # self.browser.find_element(how, what)
            WebDriverWait(self.browser, timeout). \
                until(EC.presence_of_element_located((how, what)))
        except (TimeoutException, NoSuchElementException):
            return False

        return True

    # проверка с ожиданием timeout на отсутствие элемента
    # упадет, как только увидит искомый элемент. Не появился: успех, тест зеленый.
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    # проверка на исчезновение элемента в течении timeout
    # будет ждать до тех пор, пока элемент не исчезнет.
    def is_dissapeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException) \
                .until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def go_to_basket_page(self):
        basket_link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        basket_link.click()

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def should_be_btn_basket(self):
        assert self.is_element_present(*BasePageLocators.BASKET_LINK), "Button of basket not presented"

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
