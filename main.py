#@codefever.exe
import pyttsx3
from PyDictionary import PyDictionary
import datetime

#for speak function
engine=pyttsx3.init("sapi5")
#sapi5 helps to enhance sppech-text recognition
#get some properties of pyttsx3
voices=engine.getProperty('voices')
engine.getProperty('rate')
engine.getProperty('volume')
#change the rate of reading a/q to you  
# suggestion : put it <150
engine.setProperty('rate', 160)
#this changes the volume level 
engine.setProperty('volume',180 )
engine.setProperty('voices' , voices[0].id)

#function to speak the given 'audio' parameter
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#Function to wish/greet user according to time
def wish():
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour>12:
        speak("Good morning sir, Please enter the word to get meaning")

    elif hour<12 and hour>18:
        speak("Good afternoon sir, Please enter the word to get meaning")

    else:
        speak("Good evening sir, Please enter the word to get meaning")


def meaning(word):
    #creating instance of PyDictionary
    dict = PyDictionary()
    meaning=dict.meaning(word)
    synonyms = dict.synonym(word)
    antonyms = dict.antonym(word)
    try:
        #iterating the value return by 'meaning' dictionary
        noun_meaning=meaning['Noun'][0]
        
        print(f'{word} means {noun_meaning}')
        print(f'Synonmys are {synonyms[0] && synonyms[0]}, {synonyms[1] && synonyms[1]}, {synonyms[2] && synonyms[2]}')
        speak(f'Antonyms are {antonyms[0] && antonyms[0]} {antonyms[1] && antonyms[1]} {antonyms[2] && antonyms[2]}')

        speak(f'{word} means {noun_meaning}')
        speak(f'Synonmys are {synonyms[0] && synonyms[0]} {synonyms[1] && synonyms[1]} {synonyms[2] && synonyms[2]}')
        speak(f'Antonyms are {antonyms[0] && antonyms[0]} {antonyms[1] && antonyms[1]} {antonyms[2] && antonyms[2]}')
    except Exception as e:
        speak('unable to get the meaning please try another word')
        print('unable to get the meaning.please try another word')
    

wish()
while True:
    word=input('Please enter the word to get meaning : \n')
    if word!='':
        meaning(word)
    else:
        speak('please enter something to continue...')
