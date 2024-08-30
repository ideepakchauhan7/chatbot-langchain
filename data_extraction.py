

# from langchain.document_loaders import URLLoader
from bs4 import BeautifulSoup
import requests

# URL from which data needs to be extracted
url = "https://brainlox.com/courses/category/technical"

# Using requests to fetch the webpage content
response = requests.get(url)
html_content = response.text

# Parsing the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Extract relevant content (e.g., course titles and descriptions)
courses = []
for course in soup.find_all('div', class_='courses-content'):
    title = course.find('h3').get_text(strip=True)
    description = course.find('p').get_text(strip=True)
    courses.append({
        'title': title,
        'description': description
    })

# Print extracted data
for course in courses:
    print(f"Title: {course['title']}\nDescription: {course['description']}\n")
