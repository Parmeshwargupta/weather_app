import requests
import json
# city = input("enter the city name : ")
# url = f"https://api.weatherapi.com/v1/current.json?key=08579ab1def04fc5a3733504231405&q={city}"
# r = requests.get(url)
# # print(r.text)
# # print(type(r.text))
# wdic = json.loads(r.text)
# print(wdic["current"]["temp_c"])
import pyttsx3

if __name__ == '__main__':
    text_to_speech = pyttsx3.init()
    while(True):
        text_to_speech.say("enter the city name")
        text_to_speech.runAndWait()

        city = input("enter the city name : ")
        # text_to_speech.say(f"enter the city name")
        text_to_speech.say(city)
        url = f"https://api.weatherapi.com/v1/current.json?key=08579ab1def04fc5a3733504231405&q={city}"
        r = requests.get(url)
        # print(r.text)
        # print(type(r.text))
        wdic = json.loads(r.text)
        # print(wdic["current"]["temp_c"])
        word = wdic["current"]["temp_c"]
        if word == 'q':
            break
        print(f"Todays tempreture of {city} is : {word}")
        text_to_speech.say(f"Todays tempreture of {city} is {word}")
        text_to_speech.runAndWait()
        print()
