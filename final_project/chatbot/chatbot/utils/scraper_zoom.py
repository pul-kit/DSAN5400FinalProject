import requests
import csv
from bs4 import BeautifulSoup

# Replace 'url' with the actual URL of the website you want to scrape
url = "https://uis.georgetown.edu/zoom/faq/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all <h4> tags
    h4_tags = soup.find_all('h4')

    # Create a list to store question-answer pairs
    qa_pairs = []

    # Iterate over <h4> tags and find corresponding answers
    for h4_tag in h4_tags:
        question = h4_tag.text.strip()

        # Find the next siblings until the next <h4> tag
        answer_elements = []
        next_element = h4_tag.find_next_sibling()
        while next_element and next_element.name != 'h4':
            answer_elements.append(str(next_element))
            next_element = next_element.find_next_sibling()

        # Combine the answer elements into a single string
        answer_html = ''.join(answer_elements).strip()

        # Use BeautifulSoup to extract text without HTML tags
        answer_text = BeautifulSoup(answer_html, 'html.parser').get_text(separator='\n')

        # Store the question-answer pair in the list
        qa_pairs.append([question, answer_text])

    # Save data to a CSV file
    with open('data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)

        # Write header row
        csvwriter.writerow(['Question', 'Answer'])

        # Write data to the CSV file
        csvwriter.writerows(qa_pairs)

    print('Data has been scraped and saved to data.csv.')

else:
    print(f'Failed to retrieve the webpage. Status code: {response.status_code}')
