import requests
from bs4 import BeautifulSoup as bs


url = "https://www.stark.dk/bosch-0615990m1u-gsr-18v-55-skruemaskine?id=2660-7440868"

import requests
from bs4 import BeautifulSoup

# Replace 'url' with the URL of the webpage you want to scrape
url = 'https://example.com'  # Replace with your website's URL

# Send an HTTP request and get the webpage content
response = requests.get(url)

if response.status_code == 200:
    html_content = response.content

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Use BeautifulSoup to locate the <h2> element with the product information
    product_info_element = soup.find('h2')

    if product_info_element:
        product_info = product_info_element.text
        print(product_info)
    else:
        print('Product information not found')
else:
    print('Failed to fetch the webpage. Status code:', response.status_code)
