import requests
from bs4 import BeautifulSoup
import re

# Define the URL of the page you want to scrape
url = 'https://platinumtokens.com/item/twisted-bow'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the element with the specified class name
    summary_element = soup.find('div', class_='SummarySection__SummaryLayout-sc-1k0xz9p-2 cTsjZu')

    if summary_element:
        # Extract and clean the text within the summary element
        summary_text = summary_element.get_text().strip()

        # Use regular expressions to find numeric values
        numeric_values = re.findall(r'\d[\d,\.]+', summary_text)

        if numeric_values:
            # Print the extracted numeric values
            print("Latest Prices:\n")
            print("Buy Price:", numeric_values[0])
            print("Sell Price:", numeric_values[1])
            print("Margin:", numeric_values[2])
            print("ROI:", numeric_values[3])
        else:
            print("Numeric values not found in the summary text.")
    else:
        print("Summary element not found on the page.")
else:
    print('Failed to retrieve the webpage. Status code:', response.status_code)
