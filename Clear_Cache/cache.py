from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import sched, time
import threading
s = sched.scheduler(time.time, time.sleep)

#This code was aimed for clearing cache during an online streaming automatically (incase there is limited time straming) , so that one dont need to clear the cache manually

def get_clear_browsing_button(driver):
    """Find the "CLEAR BROWSING BUTTON" on the Chrome settings page."""
    return driver.find_element_by_css_selector('* /deep/ #clearBrowsingDataConfirm')


def clear_cache(driver, timeout=60):
    """Clear the cookies and cache for the ChromeDriver instance."""
    # navigate to the settings page
    print("Hi")
    driver.execute_script('''window.open("chrome://settings/", "www.hotstar.com");''')
    driver.get('chrome://settings/clearBrowserData')

    # wait for the button to appear
    wait = WebDriverWait(driver, timeout)
    wait.until(get_clear_browsing_button)

    # click the button to clear the cache
    get_clear_browsing_button(driver).click()

    # wait for the button to be gone before returning
    wait.until_not(get_clear_browsing_button)
    #driver.switch_to.window(driver.window_handles[1])
    #driver.switch_to_window(driver.window_handles[1])

driver = webdriver.Chrome()

while True:
    clear_cache(driver)
    time.sleep(850)
#s.enter(60, 1, clear_cache(driver), (s,))
#s.run()

