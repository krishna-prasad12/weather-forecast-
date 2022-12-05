import requests
import json



def get_data(city,days):
    key="c699da52bfaa4b4831613abd17dfa5f7"
    url=f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={key}"

    request=requests.get(url)
    data=request.json()
    # return data
    new_data=data['list']
    days=8*days   #each day 8 times with 3 hr interval in 24 hrs
    new_data=new_data[:days]
    print(new_data)
    return new_data

    # new_filt=[new_d['main']['temp'] for new_d in new_data]
    # new_sky=[new_d['weather'][0]['main'] for new_d in new_data]
    # print(new_sky)
    # print(data)
    # print(len(data))














if __name__=='__main__':
    get_data('Thrissur',3)

