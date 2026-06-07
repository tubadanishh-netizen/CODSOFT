import urllib.request #urllib.request lets python fetch data from the internet
import json #json helps Python read the weather data that comes back
def get_weather(city): #this is a function that fetches live weather from any city
    api_key="8d5672426cf16954e5c38eb0a64c7034" #API key from Openweathermap
    city=city.strip()
    url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    #build the website link that gives us weather data and units=metric means we get celsius instead of Farenheit
    try: #try block gets the weather - if anything oes wrong, jump to except block. It opens the url to read the response
        response=urllib.request.urlopen(url)
        data=json.loads(response.read()) #converts the response into python readable data
        temp=data["main"]["temp"] #extracts just the temperature from the data
        desc=data["weather"][0]["description"] #extracts the weather description
        return f"The weather in {city} is {temp}degrees C with {desc}." #returns a suitable sentence with the weather info
    except: #if something went wrong like wrong city name or no internet etc, this block will catch that error
        return "Sorry, I couldn't find weather for that city."
    
        

def chatbox(): #main chatbox function
    print("Hello! I am a simple chatbox.")
    print("Type 'quit' to exit.")

    while True: #keeps loopin forever until user types quit
        user_input=input("You: ").lower() #takes input from te user and converts it into lowercase

        if user_input=="quit": #if user types quit, say and stop the loop
            print("Chatbox:Goodbye! Have a nice day!")
            break
        elif "hello" in user_input or "hi" in user_input or "hey" in user_input:
            print("TSbox: Hi there! How are you?")
        elif "how are you" in user_input:
            print("TSbox:I'm doing great! Thanks for asking.")
        elif "your name" in user_input:
            print("TSbox: My name is TSBot!")
        elif "age" in user_input:
            print("TSbox: I'm a brand new bot.")
        elif "help" in user_input:
            print("Chatbox: I can answer basic questions. Try asking my name!")
        elif "fine" in user_input or "good" in user_input:
            print("TSbox: That's great to hear!")
        elif "bad" in user_input or "sad" in user_input or "upset" in user_input or "feeling down" in user_input:
            print("TSbox: I'm sorry to hear that. I hope you feel better!")
        elif "thanks" in user_input or "thank you" in user_input:
            print("TSbox: You're welcome!")
        elif "weather" in user_input or "weather in" in user_input: 
            city=user_input.replace("weather in", "")#removing weather in from weather in {city} for the API
            city=city.strip()
            print("TSbot: " + get_weather(city))
        else:
            print("TSbot:I'm sorry, I don't understand that yet.")

chatbox()#start the chatbox
