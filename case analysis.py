import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator


cases_world = pd.read_csv('owid-covid-data.csv')
vaccine_world = pd.read_csv('vaccinations.txt', delimiter=",")


# Canada
def relations_location(location):
    cases = cases_world[cases_world['location']==location]
    vaccine = vaccine_world[vaccine_world['location']==location]
    start_vaccinated = cases[cases['date'] >= vaccine['date'].iloc[0]]
    x = vaccine['date']
    y1 = start_vaccinated['new_cases']
    y2 = vaccine['people_vaccinated']
    y3 = vaccine['people_fully_vaccinated']
    if len(x) != len(y1):
        if len(x) > len(y1):
            x = x.iloc[0:len(y1)]
        else:
            y1 = y1.iloc[0:len(x)]
    x_major_locator = MultipleLocator(7)
    ax = plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)
    plt.xticks(rotation=90)
    plt.plot(x, np.abs(y1), color='r')
    plt.plot(x, y2/500, color='b')
    plt.plot(x, y3/500, color='g')
    plt.legend(['new_cases_daily', 'people_vaccinated_every500', 'people_fully_vaccinated_every500'], loc='upper left')


relations_location('South Korea')
