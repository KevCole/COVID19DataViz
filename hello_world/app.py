import pandas as pd
from datetime import datetime

url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us.csv"
jh_url = "https://raw.githubusercontent.com/datasets/covid-19/master/data/time-series-19-covid-combined.csv"



# tells panda to read data from NYT & JHop respectively
nyt_data = pd.read_csv(url, low_memory=False)
jhop_data = pd.read_csv(jh_url, low_memory=False)

    # change data series name to 'Data'
nyt_data.rename(columns={'date': 'Date'}, inplace=True)

    # drop unnecessary columns in John Hopkins Data set

jhop_data.drop(['Lat', 'Long', 'Confirmed', 'Deaths', 'Province/State'], axis=1, inplace=True)

    # select only US data
jhop_us_data = jhop_data[jhop_data['Country/Region'] == 'US']

    # merge data
combined = pd.merge(nyt_data, jhop_us_data, left_on="Date", right_on="Date", how="left")


    # drop Country/Region from combined
combined.drop(['Country/Region'], axis=1, inplace=True)

    # drop first row due to off by one issue
combined.drop(combined.index[0], inplace=True)

    # convert date to object
for index, row in combined.iterrows():
    dt = datetime.strptime(row[0], '%Y-%m-%d')
    row[0] = dt.strftime('%b-%d-%Y')
