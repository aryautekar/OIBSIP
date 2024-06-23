import requests

api_key="2f9a70922170ee7d66aee7cdd7cac1b8"

user_input=input("Enter your City Name:")
#print(user_input)
complete_url="https://api.openweathermap.org/data/2.5/weather?q="+ user_input + "&appid=" + api_key
#print(complete_url)
weather_data=requests.get(complete_url)

country=weather_data.json()["sys"]["country"]
weather=weather_data.json()["weather"][0]["main"]
temperature= round(weather_data.json()["main"]["temp"])
humidity=round(weather_data.json()["main"]["humidity"])
wind=float(weather_data.json()["wind"]["speed"])

print("************************************")
print("THE WEATHER REPORT FOR "+country+","+user_input+": ")
print("CURRENT WEATHER: ",weather)
temp=int(temperature-273.15)
print("TEMPERATURE: ",temp, "°C")
print("HUMIDITY: ",humidity)
print("WIND: ",wind)
