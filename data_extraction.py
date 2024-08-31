from bs4 import BeautifulSoup
import requests


url = "https://brainlox.com/courses/category/technical"

response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

courses = []
for course in soup.find_all('div', class_='courses-content'):
    title = course.find('h3').get_text(strip=True)
    description = course.find('p').get_text(strip=True)
    courses.append({
        'title': title,
        'description': description
    })

for course in courses:
    print(f"Title: {course['title']}\nDescription: {course['description']}\n")
