import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_html(url, output_file):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    page_source = driver.page_source
    fileToWrite = open(output_file, "w")
    fileToWrite.write(page_source)
    fileToWrite.close()

print("what the fuck")
