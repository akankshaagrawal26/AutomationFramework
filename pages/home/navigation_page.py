import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class NavigationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _my_courses = "All Courses"
    _all_courses = "My Courses"
    _practice = "Practice"
    _user_settings_icon = "userAcctTab_MainMenu"


    def navigateToAllCourses(self):

        self.elementClick(locator=self._all_courses, locatorType="link")

    def navigateToMyCourses(self):
        self.elementClick(locator=self._my_courses, locatorType="link")

    def navigateToPractice(self):
        self.elementClick(locator=self._practice, locatorType="link")

    def navigate_to_user_settings(self):
        self.waitForElement(locator=self._user_settings_icon, pollFrequency=0.5)
        self.elementClick(locator=self._user_settings_icon)