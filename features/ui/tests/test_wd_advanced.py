from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import selenium1.utilities as utils
from selenium.common.exceptions import NoSuchElementException
import pytest


# AGENDA: 
    # methods for performing keyboard and mouse actions using ActionChains class
    # simulating mouse operations such as draand driop and double click
    # Running JacaScript code
    # capturing screenshots and movies of test runs

print(utils.get_timestamp())

@pytest.mark.screenshots
def test_take_screenshots(browser):
    """takes screenshots if no element found"""

    url = "http://the-internet.herokuapp.com/login"
    browser.get(url)

    # Steps to automate:
    # use existing scipt
    # use try except 
    # get timestamp
    # save screenshot with driver.save_screenshot(file) , use this path "./screenshots/timestamp.png"
    # log each step with print


    try:
        # use the following Login steps we created previously
        print("loggin page started..")
        username = browser.find_element_by_xpath("//input[@id='username']")
        passwrod = browser.find_element_by_xpath("//input[@id='password']")
        login = browser.find_element_by_xpath("//i[@class='fa fa-2x fa-sign-in']")
        username.send_keys("tomsmith")
        passwrod.send_keys("SuperSecretPassword!")
        login.click()
        print("logged in, taking screenshot")
        sleep(10)
        filepath = "./screenshots/"+ utils.get_timestamp() +".png"
        browser.save_screenshot(filepath)
        print('test completed!')

    except NoSuchElementException:
        print("Something went wrong!")
        filepath = "./screenshots/error-"+ utils.get_timestamp() +".png"
        browser.save_screenshot(filepath)
        raise

@pytest.mark.popupwindow
def test_popup_window(browser):
    """ Switching to new window and switch back."""

    url = "https://learn.letskodeit.com/p/practice"
    browser.get(url)

    # Steps to automate:
    # get current handle
    # find element to click
    # get all handles with driver.window_handles
    # loop all handles and go to the handle that is not parent
    # find element - search box and enter something
    # submit,  take a screenshot, use break
    # switch back to main window
    # log each step with print
    parentHandle = browser.current_window_handle
    element = browser.find_element_by_xpath("//button[@id='openwindow']")
    element.click()
    print("new window opened, getting the handles")
    handles = browser.window_handles  # returns the list of all window handles

    for handle in handles:
        if handle != parentHandle:
            browser.switch_to.window(handle)
            print('switching to new window')
            search = browser.find_element_by_xpath("//input[@id='search-courses']")
            search.send_keys("python")
            search.submit()
            sleep(5)
            print('search successfully executed, taking screenshot')
            filepath = "./screenshots/window-"+ utils.get_timestamp() +".png"
            browser.save_screenshot(filepath)
    
    browser.switch_to.window(parentHandle)
    print('switched back to original window')
    sleep(5)

@pytest.mark.executejs
def test_execute_js(browser):
    """ Demonstates executing some javaScript code with selenium."""

    url = "https://learn.letskodeit.com/p/practice"
    browser.get(url)
    browser.execute_script("window.location = 'https://learn.letskodeit.com/p/practice';")

    # element = browser.find_element_by_id('name')
    element = browser.execute_script("return document.getElementById('name');")
    element.send_keys('Hello')

    # Scroll down
    browser.execute_script("window.scrollBy(0, 1300);")
    sleep(5)

    # Scroll up
    browser.execute_script("window.scrollBy(0, -1300);")
    sleep(5)

@pytest.mark.hoveraction
def test_hover_action(browser):
    """ Demonstates Mouse over action using ActionChains class."""

    url = "https://learn.letskodeit.com/p/practice"
    browser.get(url)

    # Steps to automate:
    # find element to hover
    # create actions object of ActionChains(driver) class
    # perform move_to_element(element) action
    # click the element that appears on hover
    # log each step with print
    browser.execute_script("window.scrollBy(0, 1000);")
    sleep(5)
    element = browser.find_element_by_xpath("//button[@id='mousehover']")
    actions =  ActionChains(browser)
        # Sample action from ActionChains
            # actions.key_down(Keys.CONTROL)
            # actions.send_keys('c')
            # actions.key_up(Keys.CONTROL).perform()
    actions.move_to_element(element).perform()
    topButton = browser.find_element_by_xpath("//a[contains(text(),'Top')]")  # "//a[text()='Top']"
    sleep(5)
    topButton.click()
    sleep(10)
    assert "#top" in browser.current_url
    assert "https://learn.letskodeit.com/p/practice#top" == browser.current_url


@pytest.mark.draganddrop
def test_drag_and_drop(browser):
    """ Demonstrates Drag and Drop mouse action using ActionChains class."""

    url = "https://jqueryui.com/droppable/"
    browser.get(url)

    # Steps to automate:
    # locate draggable element
    # locate droppable element
    # create an object of ActionChains(driver) class
    # perform drag_and_drop action
        # Alternative: perform click_and_hold(element1).move_to_element(element2).release action
    # log each step with print
    print("locating the both elements")
    sleep(3)
    element1 = browser.find_elfement_by_xpath("//*div[@id='draggable']")
    element2 = browser.find_element_by_xpath("//*div[@id='droppable']")

    # element1 = browser.find_element_by_id('draggable')
    # element2 = browser.find_element_by_id('droppable')

    # element1 = browser.find_element_by_css_selector('#draggable')
    # element2 = browser.find_element_by_css_selector('#droppable')
    
    print('creationg actions and performing drag and drop')
    actions = ActionChains(browser)
    sleep(3)
    actions.drag_and_drop(element1, element2).perform()
    sleep(5)
    # assert browser.find_element_by_xpath("//p[contains(text(),'Dropped!')]").is_displayed()
    assert element2.text == "Dropped!"