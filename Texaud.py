from pyttsx3 import init  # Importing init function from pyttsx3 module
from os import system, name  # Importing system and name from os module


# Clear screen functio
def clear():
    system('cls' if name == 'nt' else 'clear')


# Text to speech function
def tts(text=None, i=0):
    engine = init()
    voices = engine.getProperty('voices')  # Get available voices
    engine.setProperty('voice', voices[i].id)  # Choose voice model
    engine.setProperty('rate', 120)  # Change the speed of the voice
    print(" Speaking...")
    engine.say(text)
    engine.runAndWait()
    print(" Finished...")
    save = input("\n Are you want to save?(Y/N)")
    if save == 'y' or save == 'Y':
        path = input("\n Enter File name (eg. audio.mp3): ")  # Getting filename from user
        engine.save_to_file(text, path)  # Save as media file
        engine.runAndWait()
        print(" *Saved")


# Function to read file
def read_file():
    try:
        path = input(" Enter file path: ")
        with open(path) as f:
            r = f.read()
            return r
    except:
        print(" File Not Found!")


# Main program starts here
def main():
    while True:
        print('''
        ███        ▄████████ ▀████    ▐████▀    ▄████████ ███    █▄  ████████▄  
    ▀█████████▄   ███    ███   ███▌   ████▀    ███    ███ ███    ███ ███   ▀███ 
       ▀███▀▀██   ███    █▀     ███  ▐███      ███    ███ ███    ███ ███    ███ 
        ███   ▀  ▄███▄▄▄        ▀███▄███▀      ███    ███ ███    ███ ███    ███ 
        ███     ▀▀███▀▀▀        ████▀██▄     ▀███████████ ███    ███ ███    ███ 
        ███       ███    █▄    ▐███  ▀███      ███    ███ ███    ███ ███    ███ 
        ███       ███    ███  ▄███     ███▄    ███    ███ ███    ███ ███   ▄███ 
       ▄████▀     ██████████ ████       ███▄   ███    █▀  ████████▀  ████████▀  
        
                    Simple Offline Text To Audio Converter
        ''')
        print("\n 1.Typing\n 2.Text File\n 3.Exit")
        ch = input(" Enter your choice: ")
        if ch == '1':  # For typing the text
            print("\n Voices Available: ")
            print(" 1.Male(Default)\n 2.Female")
            vo = input("\n Select voice: ")
            if vo == '2':
                tex = input(" Enter something to say: ")
                tts(tex, i=1)
            else:
                tex = input(" Enter something to say: ")
                tts(tex)
        if ch == '2':  # For read text from file
            print("\n Voices Available: ")
            print(" 1.Male(Default)\n 2.Female")
            vo = input("\n Select voice: ")
            tts(read_file(), i=1) if vo == '2' else tts(read_file(), i=1)
        if ch == '3':  # For exit the program
            exit(0)
        input("\n Press enter to continue...")
        clear()


# Invoking main function
main()
