from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# Chrome options to use a proxy
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=http://user:pass@endpoint:port')

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL of the web page
url = "https://github.com/Smartproxy/Smartproxy"

# Open the web page
driver.get(url)

# Set an implicit wait time to wait for JavaScript to render
driver.implicitly_wait(10)  # Wait for 10 seconds

# Get the page HTML source
page_source = driver.page_source

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(page_source, "html.parser")

# Find all elements with the class "react-directory-commit-message"
commit_messages = soup.find_all(class_="react-directory-commit-message")

# Open a file for writing
with open("commit_messages.txt", "w") as file:
    # Loop through the results and write them to the file
    for commit_message in commit_messages:
        file.write(commit_message.text.strip() + "\n")

# Close the driver
driver.quit()
