import requests
from bs4 import BeautifulSoup
import csv

# Replace 'url' with the actual URL of the website you want to scrape
url = "https://www.turnitin.com/help_pages/instructor_faq.asp?r=87.6295589277586#3"
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the questions and answers on the page using appropriate HTML tags and attributes
    # For example, if questions are in <h2> tags and answers are in <p> tags, you can use:
    questions = soup.find_all('dt')
    answers = soup.find_all('dd')

    # Open a CSV file for writing
    with open('data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        # Create a CSV writer object
        csvwriter = csv.writer(csvfile)

        # Write header row
        csvwriter.writerow(['Question', 'Answer'])

        # Write data to the CSV file
        for question, answer in zip(questions, answers):
            csvwriter.writerow([question.text.strip(), answer.text.strip()])

    print('Data has been scraped and saved to data.csv.')
else:
    print(f'Failed to retrieve the webpage. Status code: {response.status_code}')
