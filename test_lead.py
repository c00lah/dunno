from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import unittest


class Test(unittest.TestCase):
    
    def testLead(self):
        url = 'https://core.futuresimple.com/sales/users/login?__hstc=102910175.f4c8734c99c91211bc34018cd1f9abef.1409389917421.1410123632593.1410125657789.5&__hssc=102910175.1.1410125657789&__hsfp=1403601843'
        leads_url = 'https://app.futuresimple.com/leads'
        lead_status_settings_url = 'https://app.futuresimple.com/settings/leads/lead-status'
        email = 'c00lah@hotmail.com'
        pswrd = 'ololo!!!111'
        browser = webdriver.Firefox()
        browser.get(url)

        login = browser.find_element_by_xpath("//div/form/fieldset/div/div/input[@id='user_email']")
        login.send_keys(email)
        password = browser.find_element_by_xpath("//div/form/fieldset/div/div/input[@id='user_password']")
        password.send_keys(pswrd)
        password.send_keys(Keys.RETURN)
        browser.implicitly_wait(5)
        browser.get(leads_url)
        skip = browser.find_element_by_xpath("//div/div/div/div/a[@class='btn btn-large welcome-button skip gray']")
        skip.click()
        browser.get(leads_url+'/new')
        last_name = browser.find_element_by_xpath("//div/div/div[@id='container']/div/div[@class='edit-view-container container-fluid']/div/div/form/div/fieldset/div[@class='lead-fields']/div/div/div/input[@id='lead-last-name']")
        last_name.send_keys('Test')
        save = browser.find_element_by_xpath("//div/div/div/div/div/div/div/div[@class='edit-buttons span4']/button")
        save.click()
        status = browser.find_element_by_xpath("//div/div/div/div[@id='content-container']/div/div[@class='row-fluid lead-details']/div/div/div/ul/div/div/a/span")
        new_lead_url = browser.current_url
        self.assertEqual(status.text, 'New')
        browser.get(lead_status_settings_url)
        lead_status = browser.find_element_by_xpath("//div/div/div[@id='container']/div[@class='row-fluid']/div[@id='main-container']/div/div[@class='tab-content settings-content longer-labels form-horizontal']/div[@id='lead-status']")
        lead_status.click()
        lead_status_edit_new_button = lead_status.find_element_by_xpath(".//div/div/div[@data-named-object-id='1188704']/div/div/button")
        lead_status_edit_new_button.click()
        lead_status_edit_new = lead_status.find_element_by_xpath(".//div/div/div/form/fieldset/div[@for='name']/div/input")
        lead_status_edit_new.clear()
        lead_status_edit_new.send_keys('Whatever')
        lead_status_edit_new.send_keys(Keys.RETURN)
        browser.get(new_lead_url)
        browser.implicitly_wait(5)
        status = browser.find_element_by_xpath("//div/div/div/div[@id='content-container']/div/div[@class='row-fluid lead-details']/div/div/div/ul/div/div/a/span")
        self.assertEqual(status.text, 'Whatever')