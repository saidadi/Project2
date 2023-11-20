import requests
import pandas as pd

class CovidDataCollector:
    def __init__(self, url):
        self.url = url
    """
    ### COVID-19 Data:
    The COVID-19 data includes information about COVID-19 cases in different districts.
    Fields:
    - 'District': Name of the district
    - 'notes': Additional notes
    - 'active': Active cases
    - 'confirmed': Confirmed cases
    - 'migratedother': Migrated cases
    - 'deceased': Number of deaths
    - 'recovered': Recovered cases
    - 'delta': Changes in cases

    Questions:
    1. Which district has the highest number of confirmed cases?
    2. What is the overall death rate in the analyzed districts?
    """
    def make_request(self):
        response = requests.get(self.url)
        return response.json()

    def create_dataframe(self, api_data):
        data = api_data['Tamil Nadu']['districtData']
        df = pd.DataFrame(data).T.reset_index().rename(columns={'index': 'District'})
        return df

    def collect_data(self):
        api_data = self.make_request()
        df = self.create_dataframe(api_data)
        return df
