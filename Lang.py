import requests
from bs4 import BeautifulSoup

# Define the URL of the website you want to fetch
url = "https://shironet.mako.co.il/html/indexes/performers/heb_0_popular.html"

# Step 1: Send a GET request to the website
response = requests.get(url)

# Step 2: Check if the request was successful (status code 200)
if response.status_code == 200:
    # Step 3: Parse the HTML content of the webpage
    soup = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')

    # Step 4: Extract all text from the webpage
    all_text = soup.get_text()

    # Step 5: Split the text into individual words
    words = all_text.split()
    

    # Step 6: Print the individual words
    for word in words:
        print(word)
    print("חןילחגה")
else:
    print("Failed to fetch the website:", response.status_code)
