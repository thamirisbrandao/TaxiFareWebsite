import streamlit as st
import datetime
import pandas as pd
import requests
import numpy as np
'''
# TaxiFareModel front
'''

st.markdown('''
My first web page
''')

d = st.date_input("Insert the date", datetime.date(2019, 7, 6))
t = st.time_input('Insert the time', datetime.time(8, 45))
lon_get = st.number_input('Insert longitude')
lat_get = st.number_input('Insert latitude')
dlon_get = st.number_input('Insert dropoff longitude')
dlat_get = st.number_input('Insert dropoff latitude')
pass_get = st.selectbox('Insert passenger count', list(range(1, 9)))

@st.cache
def get_map_data():

    return pd.DataFrame(
            np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
            columns=['lat', 'lon']
        )

df = get_map_data()

st.map(df)

url = f'https://taxifare.lewagon.ai/predict?pickup_datetime={d} {t}&pickup_longitude={lon_get}&pickup_latitude={lat_get}&dropoff_longitude={dlon_get}&dropoff_latitude={dlat_get}&passenger_count={pass_get}'

response = requests.get(url).json()

st.write(response['fare'])

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''