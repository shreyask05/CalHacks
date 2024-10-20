from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def get_html(url, output_file):
    print("url: " + url)
    options = Options()
    options.headless = True

    # Ensure 'chromedriver' is accessible, or provide the path to it
    driver = webdriver.Firefox(options=options)

    # Load the web page
    driver.get(url)
    print("got url")
    # Get the page source (HTML)
    page_source = driver.page_source

    # Save the HTML content to the file using a context manager
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(page_source)

    # Close the browser session
    driver.quit()

    print("HTML successfully saved.")


# Example usage:
# get_html('https://example.com', 'output.html')

