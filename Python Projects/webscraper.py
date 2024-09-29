import requests
from bs4 import BeautifulSoup
import csv

# Define the URL
url = 'https://realpython.com/tutorials/'

# Make a request to the website
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Extract and print search results
tutorials = soup.find_all('div', class_='card')

# Open a CSV file for writing
with open('tutorials.csv', 'w', newline='', encoding='utf-8') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)
    
    # Write the header row
    csvwriter.writerow(['Title', 'Link'])
    
    # Write the data rows
    for tutorial in tutorials:
        title = tutorial.find('h2').text.strip() if tutorial.find('h2') else 'No title found'
        link = tutorial.find('a')['href'] if tutorial.find('a') else 'No link found'
        csvwriter.writerow([title, f"https://realpython.com{link}"])

print("Data has been written to tutorials.csv")