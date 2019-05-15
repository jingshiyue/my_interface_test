#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<>
  Purpose: 
  Created: 2019/3/19
"""
import time
import unittest
from selenium import webdriver
import sys,os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parentdir)
from utils.mylog import mylog
Log = mylog()
logger = Log.get_log().get_logger()
from selenium.webdriver import ActionChains




#########################################################################
class test_baidu(unittest.TestCase):
    """"""

    @classmethod
    def setUp(self):
        logger.debug("open browser")
        self.driver = webdriver.Firefox()
        #self.driver=webdriver.Firefox()
        #profile = webdriver.FirefoxProfile()
        #profile.default_preferences["webdriver_assume_untrusted_issuer"]= 'false'
        #profile.update_preferences()
        #capabilities = webdriver.DesiredCapabilities().INTERNETEXPLORER
        #capabilities['acceptSslCerts'] = True        
        #profile.accept_untrusted_certs=False
        #self.driver = webdriver.Firefox(firefox_profile=profile,desired_capabilities=capabilities)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
    
    #@unittest.skip("不测试百度搜索淘宝")
    def test_login_interface(self):
        """selenium通过百度搜查淘宝，登陆淘宝账号"""
        url ="https://www.baidu.com/"
        self.driver.get(url)
        logger.debug(self.driver.title)
        current_window_handle = self.driver.current_window_handle
        self.driver.find_element_by_xpath("//*[@id='kw']").send_keys("taobao")
        self.driver.find_element_by_xpath("//*[@id='su']").click()
        taobao = self.driver.find_elements_by_partial_link_text("淘宝网")
        for link in taobao:
            if "淘!我喜欢" in link.text:
                taobao = link
                break
        taobao.click()
        logger.info(taobao.text)
        logger.info(self.driver.window_handles)
        for handle in self.driver.window_handles:
            if handle != current_window_handle:
                self.driver.switch_to_window(handle)
                #time.sleep(3)
                #self.driver.find_element_by_xpath("//*[@id='q']").send_keys("鞋子")
                input = self.driver.find_element_by_xpath("//input[@id='q']")
                input.clear()
                self.driver.find_element_by_xpath("//input[@id='q']").send_keys("鞋子")
                #time.sleep(3)
                submit = self.driver.find_element_by_xpath('//button[@type="submit" and @class="btn-search tb-bg"]') 
                submit.click()
                break
        #iframe = self.driver.find_elements_by_xpath('//iframe')
        #logger.debug(len(iframe))
        #if iframe:
            #self.driver.switch_to_frame(iframe)
        time.sleep(5)
        #try:
            #login_before = self.driver.find_element_by_xpath('//i[@id="J_Static2Quick"]')
            #logger.debug(login_before.tag_name)
            #login_before.click()
            #logger.debug("登陆前处理")
        #except:
            #logger.debug("直接登陆")
        try:
            login = self.driver.find_element_by_xpath('//i[@id="J_Quick2Static"]')  
            login.click()
            logger.info("开始登陆...")
        #self.driver.find_elements_by_xpath('//i[@id="J_Quick2Static"]').click()
        except:
            pass
        username = self.driver.find_element_by_xpath('//input[@id="TPL_username_1"]')
        logger.info(username)
        logger.info(username.tag_name)
        username.clear()
        username.send_keys("静似月ing")
        time.sleep(4)
        password = self.driver.find_element_by_xpath('//input[@id="TPL_password_1"]')  
        logger.info(password)
        logger.info(password.tag_name)        
        password.send_keys("zzz123456.")
        time.sleep(4)
        button = self.driver.find_element_by_xpath('//span[@id="nc_1_n1z"]')
        action = ActionChains(self.driver)
        action.click_and_hold(button).perform()
        action.reset_actions()
        action.click_and_hold(button).move_by_offset(258,0).release().perform()
        time.sleep(2)
        loginBt = self.driver.find_element_by_xpath('//button[@id="J_SubmitStatic"]')
        time.sleep(9)
        loginBt.click()
        logger.info("登陆验证")
        
    # def test_taobao(self):
        # self.driver.get("https://www.taobao.com/")
        # cookies = self.driver.get_cookies()
        # for i in cookies:
            # logger.debug(i)
        # input = self.driver.find_element_by_xpath("//input[@id='q']")
        # input.clear()
        # self.driver.find_element_by_xpath("//input[@id='q']").send_keys("帽子")
        time.sleep(3)
        # submit = self.driver.find_element_by_xpath('//button[@type="submit" and @class="btn-search tb-bg"]') 
        # submit.click()        
        # goods = self.driver.find_elements_by_xpath('//div[@class="row row-2 title"]')
        # for item in goods:
            # logger.info(item.text)
        
    # def test_51job(self):
        # todo 
        
    @classmethod
    def tearDown(self):
        logger.debug("close browser")
        #self.driver.quit()
        


if __name__ == '__main__':
    unittest.main()
    
#driver = webdriver.Firefox()
#driver.maximize_window()
#con = driver.get("https://www.baidu.com/")
#print(driver.title)
#print(driver.current_url)
#print(driver.page_source)
#print(driver.current_window_handle)

