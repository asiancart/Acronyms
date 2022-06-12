import sys

try:
    import pyttsx3
except ImportError:
    print('The pyttsx3 module needs to be installed to run this')
    print('program. On Windows, open a Command Prompt and run:')
    print('pip install pyttsx3')
    print('On macOS and Linux, open a Terminal and run:')
    print('pip3 install pyttsx3')
    sys.exit()


tts = pyttsx3.init()

print('Text To Speech Talker, by asiancart')

while True:
    text = input('> ')
    if text.upper() == 'QUIT':
        print('Thanks for playing.')
        sys.exit()

    tts.say(text)
    tts.runAndWait()