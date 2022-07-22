from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(executable_path='/home/nima/Working/Selenium/chromedriver')
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("http://google.com")
