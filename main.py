from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.theguardian.com")

# headlines = driver.find_elements(By.CSS_SELECTOR, ".PagePromo-title span")
# print("APNEWS HEADLINES: ")
# for headline in headlines:
#     print(headline.text)

# headlines = driver.find_elements(By.CSS_SELECTOR, ".cluster__stories__WrBsf li a")
# print("REUTERS HEADLINES: ")
# for headline in headlines:
#     print(headline.text)

# headlines = driver.find_elements(By.CSS_SELECTOR, ".zones_zones__YedWY section section section div")
# print("BLOOMBERG HEADLINES: ")
# for headline in headlines:
#     print(headline.text)

# headlines = driver.find_elements(By.CSS_SELECTOR, ".dcr-yyvovz ul")
# print("GUARDIAN HEADLINES:")
# for headline in headlines:
#     print(headline.text)

# close single/active tab
# driver.close()

# quit entire browser
driver.quit()

# TO GET ALL HEADLINES
# def getUrls(targeturl):
#     driver = webdriver.Chrome(options="chrome_options")
#     driver.get("http://www."+targeturl+".com")
#     # perform your taks here
#     if targeturl == "apnews":
#         headlines = driver.find_elements(By.CSS_SELECTOR, ".PagePromo-title span")
#         print("APNEWS HEADLINES: ")
#         for headline in headlines:
#             print(headline.text)
#     elif targeturl == "reuters":
#         headlines = driver.find_elements(By.CSS_SELECTOR, ".cluster__stories__WrBsf li a")
#         print("REUTERS HEADLINES: ")
#         for headline in headlines:
#             print(headline.text)
#     elif targeturl == "bloomberg":
#         headlines = driver.find_elements(By.CSS_SELECTOR, ".zones_zones__YedWY section section section div")
#     driver.quit()

# for i in range(3):
#     webPage = ['apnews','reuters','bloomberg','theguardian']
#     for i in webPage:
#         print i;
#         getUrls(i)