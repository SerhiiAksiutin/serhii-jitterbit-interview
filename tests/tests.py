import unittest
import pdb

from selenium import webdriver


class SleneumTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Firefox()
        # pdb.set_trace()
        self.addCleanup(self.driver.quit)

    def testValidLogin(self):
    	self.driver.get('http://the-internet.herokuapp.com/login')
    	self.driver.find_element_by_id("username").send_keys('tomsmith')
    	self.driver.find_element_by_id("password").send_keys('SuperSecretPassword!')
    	self.driver.find_element_by_tag_name("button").click()
    	self.assertEqual('You logged into a secure area!\n×', self.driver.find_element_by_id("flash-messages").text)

    def testInvalidLogin(self):
    	self.driver.get('http://the-internet.herokuapp.com/login')
    	self.driver.find_element_by_id("username").send_keys('tomsmith')
    	self.driver.find_element_by_id("password").send_keys('tomsmith!')
    	self.driver.find_element_by_tag_name("button").click()
    	self.assertEqual('Your password is invalid!\n×', self.driver.find_element_by_id("flash-messages").text)

    def testDropdown(self):
    	self.driver.get('http://the-internet.herokuapp.com/dropdown')
    	self.driver.find_element_by_id("dropdown").click()
    	self.options = self.driver.find_elements_by_tag_name("option")
    	self.options[-1].click()
    	self.assertTrue(self.options[-1].is_selected())

    def testTabelEdit(self):
    	self.driver.get('http://the-internet.herokuapp.com/tables')
    	self.driver.find_element_by_xpath('//*[@id="table2"]/tbody/tr[3]/td[6]/a[1]').click()
    	self.tags = self.driver.find_elements_by_css_selector("#table2 > tbody > tr")
    	for i in self.tags:
    		if i.find_element_by_css_selector('.email').text == 'jdoe@hotmail.com':
    			i.find_element_by_css_selector('td.action > a:nth-child(1)').click()
    	self.assertEqual('http://the-internet.herokuapp.com/tables#edit', self.driver.current_url)

if __name__ == '__main__':
    unittest.main(verbosity=2)
