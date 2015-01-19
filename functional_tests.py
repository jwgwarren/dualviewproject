from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
    
    def tearDown(self):
        self.browser.quit()
    
    def test_no_parameters(self):
        self.browser.get('http://localhost:8000')
        self.assertIn( 'Dual View', self.browser.title)
        
        #self.fail('Finish the test!')
        
#     def test_show_single_image(self):
#         self.browser.get('http://localhost:8000?ctrImgId=7705')
#         left_panel=self.browser.find_element_by_id('control')
#         
#     def test_show_dual_image(self):
#         self.browser.get('http://localhost:8000?ctrImgId=6778&expImgId=7068')
#         left_panel=self.browser.find_element_by_id('control')
#         right_panel=self.browser.find_element_by_id('experiment')
        
if __name__ == '__main__':
    unittest.main()