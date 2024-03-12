from selenium import webdriver
from selenium.webdriver.common.by import By

# Start a new instance of Chrome WebDriver
driver = webdriver.Chrome()

# Test Case 1: Verify Wikipedia title
def test_wikipedia_title():
    driver.get("https://www.wikipedia.org")
    assert "Wikipedia" in driver.title

# Test Case 2: Search functionality
def test_search_functionality():
    driver.get("https://www.wikipedia.org")
    search_box = driver.find_element(By.ID, "searchInput")
    search_box.send_keys("Python programming language")
    search_box.submit()
    assert "Python programming language" in driver.page_source

# Test Case 3: Verify footer links
def test_footer_links():
    driver.get("https://www.wikipedia.org")
    footer_links = driver.find_elements(By.CSS_SELECTOR, "#footer a")
    for link in footer_links:
        assert "wikipedia.org" in link.get_attribute("href")

# Run the test cases
test_wikipedia_title()
test_search_functionality()
test_footer_links()

# Close the browser
driver.quit()
