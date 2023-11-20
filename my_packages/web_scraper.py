import requests
import pandas as pd
from bs4 import BeautifulSoup

class GuardianJobsScraper:
    def __init__(self, url):
        self.url = url
    """
    ### Guardian Jobs Data:
    The Guardian Jobs data contains job listings from the Guardian Jobs website.
    Fields:
    - 'Title': Job title
    - 'Location': Job location
    - 'Salary': Salary information
    - 'Company': Recruiting company
    - 'Description': Job description

    Questions:
    1. What are the most common job titles in the dataset?
    2. How many jobs offer a salary in a specific range?
    """
    def fetch_data(self):
        response = requests.get(self.url)
        return response.text

    def parse_data(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        job_data = []

        job_elements = soup.find_all('div', class_='lister__details')

        for job_element in job_elements:
            title_element = job_element.find('h3', class_='lister__header')
            title = title_element.text.strip() if title_element else None

            location_element = job_element.find('li', class_='lister__meta-item--location')
            location = location_element.text.strip() if location_element else None

            salary_element = job_element.find('li', class_='lister__meta-item--salary')
            salary = salary_element.text.strip() if salary_element else None

            company_element = job_element.find('li', class_='lister__meta-item--recruiter')
            company = company_element.text.strip() if company_element else None

            description_element = job_element.find('p', class_='lister__description')
            description = description_element.text.strip() if description_element else None

            job_info = {'Title': title, 'Location': location, 'Salary': salary, 'Company': company, 'Description': description}
            job_data.append(job_info)

        return job_data


    def create_dataframe(self, scraped_data):
        return pd.DataFrame(scraped_data)

    def scrape_data(self):
        html_content = self.fetch_data()
        data = self.parse_data(html_content)
        df = self.create_dataframe(data)
        return df
