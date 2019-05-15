# -*- coding:utf-8 -*- 
import time
import unittest
from selenium import webdriver
import sys,os
from appium import webdriver
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parentdir)
from utils.mylog import mylog
from utils import config
from selenium.webdriver.support import expected_conditions as EC
Log = mylog()
logger = Log.get_log().get_logger()


########################################################################
class test_kaoyanbang(unittest.TestCase):
    """"""
    @classmethod
    def setUpClass(cls):
        data = config.yaml_conf().data
        desired_caps = config.yaml_conf().desired_caps
        cls.driver=webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub',desired_caps)
        logger.debug(time.time())
        cls.driver.wait_activity("com.tal.kaoyan.ui.activity.SplashActivity", 10)   
        logger.debug(time.time())
        cls.driver.implicitly_wait(5)
        logger.debug("启动考研帮...")
    
    @unittest.skip('跳过')
    def test_login(cls):
        logger.debug("login...")
        try:
            cls.driver.find_element_by_id('android:id/message').click()
            logg.debug( cls.driver.find_element_by_id('android:id/message').text)
            logger.debug('取消更新')
        except:
            pass
        try:
            skp = cls.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.LinearLayout')
            logger.debug(skp.text)
            logger.debug('跳过')
        except:
            pass
        
        name = 'zhou173302591'
        password = 'zzz123456'
        #input_name = cls.driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext')
        input_name = cls.driver.find_element_by_xpath('//android.widget.EditText[1]')
        input_name.clear()
        input_name.send_keys(name)
        input_password = cls.driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext')
        input_password.send_keys(password)
        cls.driver.find_element_by_id('com.tal.kaoyan:id/login_login_btn').click()
        logger.debug('登陆完成')
    
    def test_toast(cls):
        # 等主页面activity出现
        #driver.wait_activity(".base.ui.MainActivity", 10)   
        
        from selenium.webdriver.support.ui import WebDriverWait
        cls.driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').clear()
        cls.driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').send_keys('zhou17330259')
        
        cls.driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys('zxw2018')
        cls.driver.find_element_by_id('com.tal.kaoyan:id/login_login_btn').click()
        
        
        #error_message="用户名或密码错误，你还可以尝试4次"
        error_message="账号不存在"
        limit_message="验证失败次数过多，请15分钟后再试"
        
        message='//*[@text=\'{}\']'.format(error_message)
        # message='//*[@text=\'{}\']'.format(limit_message)
        #toast_element=WebDriverWait(cls.driver,20).until(lambda x:x.find_element_by_xpath(message))
        toast_element = WebDriverWait(cls.driver, 3, 0.1).until(EC.presence_of_element_located(("xpath",message)))
        cls.assertEqual(toast_element.text, error_message)
        logger.debug(toast_element.text)

    @classmethod
    def tearDownClass(cls):
        logger.debug("完成了")
        
        
        
if __name__ == '__main__':
    unittest.main()