from selenium import webdriver
import re
chrome_path = '/home/scrapbook/tutorial/web-scraping-with-python/Chapter08/chromedriver'

from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless") # Runs Chrome in headless mode.
options.add_argument('--no-sandbox') # # Bypass OS security model
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(chrome_options=options, executable_path=chrome_path)
#driver = webdriver.Chrome(executable_path=chrome_path)

print(type(driver))

driver.get('https://www.python.org')

print("Title: ",driver.title)
print("Current Page URL: ",driver.current_url)
if re.search(r'python.org',driver.current_url):
    driver.save_screenshot("pythonorg.png")
    print("Python Screenshot Saved!")

cookies = driver.get_cookies()
print("Cookies obtained from python.org")
print(cookies)

print(driver.page_source.encode('utf-8').strip())
driver.refresh()

driver.get('https://www.google.com')
print("Title: ",driver.title)
print("Current Page URL: ",driver.current_url)
if re.search(r'google.com',driver.current_url):
    driver.save_screenshot("google.png")
    print("Google Screenshot Saved!")

cookies = driver.get_cookies()
print("Cookies obtained from google.com")
print(cookies)

print("Current Page URL: ",driver.current_url)
driver.back()
print("Page URL (Back): ",driver.current_url)
driver.forward()
print("Page URL (Forward): ",driver.current_url)

driver.close()
driver.quit()
