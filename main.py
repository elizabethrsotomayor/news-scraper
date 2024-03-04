from selenium import webdriver
from selenium.webdriver.common.by import By
from flask import Flask, render_template

app = Flask(__name__)

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.cnn.com")
#
# headlines = driver.find_elements(By.CSS_SELECTOR, ".container__headline span")
# print([headline.text for headline in headlines if len(headline.text) > 20])

# close single/active tab
# driver.close()

# quit entire browser
# driver.quit()


# TO GET ALL HEADLINES
def getUrls(targeturl):
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("http://www." + targeturl + ".com")

    if targeturl == "apnews":
        global apnews_headlines
        # TODO: Get all headlines since this only finds a few.
        apnews_headlines = driver.find_elements(By.CSS_SELECTOR, ".PagePromo-title a span")
        apnews_headlines = [headline.text for headline in apnews_headlines]
    elif targeturl == "reuters":
        global reuters_headlines
        reuters_headlines = driver.find_elements(By.CSS_SELECTOR, ".cluster__stories__WrBsf li a")
        reuters_headlines = [headline.text for headline in reuters_headlines]
    elif targeturl == "cnn":
        global cnn_headlines
        cnn_headlines = driver.find_elements(By.CSS_SELECTOR, ".container__headline span")
        cnn_headlines = [headline.text for headline in cnn_headlines if len(headline.text) > 20]
    elif targeturl == "theguardian":
        global theguardian_headlines
        theguardian_headlines = driver.find_elements(By.CSS_SELECTOR, ".dcr-yyvovz ul")
        theguardian_headlines = [headline.text for headline in theguardian_headlines]
    driver.quit()


webPage = ['apnews', 'reuters', 'cnn', 'theguardian']
for i in webPage:
    getUrls(i)

@app.route("/")
def hello_world():
    return render_template("index.html", apnews_headlines=apnews_headlines,
                           reuters_headlines=reuters_headlines, cnn_headlines=cnn_headlines,
                           theguardian_headlines=theguardian_headlines)

if __name__ == "__main__":
    app.run(debug=True)
