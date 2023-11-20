from api_data_collector import CovidDataCollector
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class DataAnalysis:
    def __init__(self, url):
        self.collector = CovidDataCollector(url)

    def analyze_data(self):
        df = self.collector.collect_data()

        self.show_top_districts(df, 5)
        self.plot_confirmed_vs_recovered(df)
        self.plot_death_rate(df)

    def show_top_districts(self, df, n=5):
        df['confirmed'] = pd.to_numeric(df['confirmed'], errors='coerce')
        
        df = df.dropna(subset=['confirmed'])
        
        top_districts = df.nlargest(n, 'confirmed')[['District', 'confirmed']]
        
        print(f"\nTop {n} Districts with the Highest Confirmed Cases:")
        print(top_districts)

    def plot_confirmed_vs_recovered(self, df):
        plt.figure(figsize=(10, 6))
        sns.barplot(x='District', y='confirmed', data=df, label='Confirmed', color='blue')
        sns.barplot(x='District', y='recovered', data=df, label='Recovered', color='green')
        plt.title('Confirmed vs Recovered Cases by District')
        plt.xlabel('District')
        plt.ylabel('Count')
        plt.xticks(rotation=45, ha='right')
        plt.legend()
        plt.show()

    def plot_death_rate(self, df):
        df['confirmed'] = pd.to_numeric(df['confirmed'], errors='coerce')
        df['deceased'] = pd.to_numeric(df['deceased'], errors='coerce')

        df['death_rate'] = df['deceased'] / df['confirmed'] * 100 if df['confirmed'].any() != 0 else 0

        plt.figure(figsize=(10, 6))
        sns.barplot(x='District', y='death_rate', data=df, color='red')
        plt.title('Death Rate by District')
        plt.xlabel('District')
        plt.ylabel('Death Rate (%)')
        plt.xticks(rotation=45, ha='right')
        plt.show()
