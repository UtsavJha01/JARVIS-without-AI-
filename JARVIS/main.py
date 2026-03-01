import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import time

newsapi = "YOUR_NEWSAPI_KEY_HERE"  # Replace with your NewsAPI key

def speak(text):
    try:
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.setProperty("volume", 1.0)
        engine.say(text)
        engine.runAndWait()
        engine.stop()
    except Exception as e:
        print(f"TTS error: {e}")

def process_command(command):
    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "open instagram" in command:
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")
    elif "open linkedin" in command:
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com/in/utsavjha01/")
    elif "play" in command:
        speak("Playing music")
        try:
            song_name = command.lower().split("play ")[1].strip()
            music_dict = getattr(musicLibrary, "music", None)
            if music_dict and song_name in music_dict:
                url = music_dict[song_name]
                webbrowser.open(url)
                speak(f"Playing {song_name}")
            else:
                speak("Song not found in library")
                if music_dict:
                    print(f"Available songs: {list(music_dict.keys())}")
                else:
                    print("No music library available")
        except IndexError:
            speak("Please specify a song name")
    elif "news" in command or "what is the news" in command:
        speak("Fetching the latest news")
        response = requests.get(
            f"https://newsapi.org/v2/everything?q=apple&from=2026-02-27&to=2026-02-27&sortBy=popularity&apiKey={newsapi}"
        )
        if response.status_code == 200:
            news_data = response.json()
            articles = news_data.get("articles", [])
            if articles:
                speak("Here are the top news headlines:")
                for article in articles:
                    speak(article["title"])
            else:
                speak("No news articles found.")
    elif "what time is it" in command or "time" in command:
        current_time = time.strftime("%I:%M %p")
        speak(f"The current time is {current_time}")
    else:
        speak("Sorry, I didn't understand that command.")

if __name__ == "__main__":
    recognizer = sr.Recognizer()
    speak("Initializing Jarvis, your personal assistant.")
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Listening for the wake word 'Jarvis'...")
            while True:
                try:
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                    command = recognizer.recognize_google(audio).lower()
                    print(f"Recognized: {command}")
                    if "jarvis" in command:
                        speak("Yes, how can I assist you?")
                        print("Jarvis is listening for your command...")
                        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                        command = recognizer.recognize_google(audio).lower()
                        process_command(command)
                except sr.UnknownValueError:
                    print("Could not understand audio")
                except sr.WaitTimeoutError:
                    continue
                except sr.RequestError as e:
                    print(f"API error: {e}")
                except Exception as e:
                    print(f"Error: {e}")
    except OSError as e:
        print(f"Microphone error: {e}")
        speak("Microphone not available. Exiting.")