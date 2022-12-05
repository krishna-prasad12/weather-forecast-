import streamlit as kp
import plotly.express as px
from backend import get_data


kp.title('Weather API For Any Region')
city=kp.text_input('enter city name')
days=kp.slider('select the days for forecast',min_value=1,max_value=5)
option=kp.selectbox('enter the type of view',('Temperature','Sky'))
temps=f'The temperature for {days}day in {city} is: '
kp.subheader(temps)
try:
    if city:
        new_data = get_data(city,days)
        if option=='Temperature':
            temperature = [new_d['main']['temp'] for new_d in new_data]
            date=[new_d['dt_txt'] for new_d in new_data]
            figure=px.line(x=date,y=temperature,labels={'x':'date','y':'temperature'})
            kp.plotly_chart(figure)
        if option=='Sky':
            lis_im = {'Clear': 'images/clear.png','Clouds': 'images/cloud.png', 'Rain': 'images/rain.png',
                       'Snow': 'images/snow.png'}
            new_sky = [new_d['weather'][0]['main'] for new_d in new_data]
            date = [new_d['dt_txt'] for new_d in new_data]
            new_date=[dat[12:] for dat in date]
            skys=[lis_im[condition] for condition in new_sky]
            kp.image(skys,width=100,caption=new_date)
except KeyError:
    kp.write('enter valid place')
