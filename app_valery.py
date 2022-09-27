import requests
import pandas as pd
import streamlit as st

url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/3hourly"

querystring ={"lat":"3.8801","lon":"-77.0312"}

headers = {
	"X-RapidAPI-Key": "19371bb78bmsha38002b17dbf6c7p198e30jsn6f6685e527ab",
	"X-RapidAPI-Host": "weatherbit-v1-mashape.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

tekst = response.json()
df = pd.DataFrame.from_dict(tekst)


df_data = pd.DataFrame(df['data'].values.tolist(), index=df.index)
df2 = pd.concat([df, df_data], axis=1).drop('data', axis=1)
df_data = pd.DataFrame(df2['weather'].values.tolist(), index=df.index) 
df2 = pd.concat([df2, df_data], axis=1).drop('weather', axis=1)

st.title('hoi')
check1 = st.checkbox ("Temperature")
check2 = st.checkbox ("UV")           
check3 = st.checkbox ("Snow")                                   

st.dataframe(df2)
st.line_chart(data=df2, x='datetime', y='temp', width=0, height=0, 
              use_container_width=True)

print(df2.info())

