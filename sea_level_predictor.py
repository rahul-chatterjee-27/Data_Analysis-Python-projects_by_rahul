import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Import data
    df = pd.read_csv('epa-sea-level.csv')

    # Scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Line of best fit (all data)
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = np.arange(df['Year'].min(), 2051)
    plt.plot(years_extended, res.intercept + res.slope * years_extended, 'r')

    # Line of best fit (from 2000)
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = np.arange(2000, 2051)
    plt.plot(years_recent, res_recent.intercept + res_recent.slope * years_recent, 'g')

    # Labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save and return
    plt.savefig('sea_level_plot.png')
    return plt.gca()