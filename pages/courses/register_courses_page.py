import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time

class RegisterCoursesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ################
    ### Locators ###
    ################
    _search_box = "search-courses"
    _search_button = "search-course-button"
    _course = "//div[contains(@class,'course-listing-title') and contains(text(),'{0}')]"
    _all_courses = "course-listing-title"
    _enroll_button = "enroll-button-top"
    # _cc_num = "cc_field"
    # _cc_exp = "cc-exp"
    # _cc_cvv = "cc_cvc"
    _cc_num = "//input[@name='cardnumber' and @class='InputElement is-empty']"
    _cc_exp = "//input[@name='exp-date' and @class='InputElement is-empty']"
    _cc_cvv = "//input[@name='cvc' and @class='InputElement is-empty']"
    _submit_enroll = "//div[@id='new_card']//button[contains(text(),'Enroll in Course')]"
    _enroll_error_message = "//div[@id='new_card']//div[contains(text(),'The card number is not a valid credit card number.')]"
    _click_icon = "//a[@class='navbar-brand header-logo']/img"

    ############################
    ### Element Interactions ###
    ############################

    def enterCourseName(self, name):
        self.sendKeys(name, locator=self._search_box)

    def clickOnSearchButton(self):
        self.elementClick(locator=self._search_button)

    def selectCourseToEnroll(self, fullCourseName):
        courseElement = self.waitForElement(self._course.format(fullCourseName), locatorType="xpath")
        result = self.isElementDisplayed(element=courseElement)
        if result:
            self.elementClick(locator=self._course.format(fullCourseName), locatorType="xpath")
        return result

    def clickOnEnrollButton(self):
        self.elementClick(locator=self._enroll_button)

    def enterCardNum(self, num):
        self.log.info("before frame")
        self.driver.switch_to.frame("__privateStripeFrame4")
        self.log.info("after frame")
        self.sendKeys(num, locator=self._cc_num, locatorType="xpath")
        self.driver.switch_to.default_content()

    def enterCardExp(self, exp):
        self.driver.switch_to.frame("__privateStripeFrame5")
        self.sendKeys(exp, locator=self._cc_exp, locatorType="xpath")
        self.driver.switch_to.default_content()

    def enterCardCVV(self, cvv):
        self.driver.switch_to.frame("__privateStripeFrame6")
        self.sendKeys(cvv, locator=self._cc_cvv, locatorType="xpath")
        self.driver.switch_to.default_content()

    def clickEnrollSubmitButton(self):
        self.elementClick(locator=self._submit_enroll, locatorType="xpath")

    def enterCreditCardInformation(self, num, exp, cvv):
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)

    def enrollCourse(self, num="", exp="", cvv=""):
        self.clickOnEnrollButton()
        self.webScroll(direction="down")
        self.enterCreditCardInformation(num, exp, cvv)
       # self.clickEnrollSubmitButton()

    def verifyEnrollFailed(self):
        messageElement = self.waitForElement(self._enroll_error_message, locatorType="xpath")
        result = self.isElementDisplayed(element=messageElement)
        return result

    def clickOnIcon(self):
        self.webScroll(direction="up")
        self.elementClick(locator=self._click_icon, locatorType="xpath")

