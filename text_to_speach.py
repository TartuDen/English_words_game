from gtts import gTTS
import os

def pronounce_text(text):
    # print(text)
    if "/" in text:
        text = text.split("/")[0]
        # text = text.strip("/")
    elif "[" in text:
        text = text.split("[")[0]
    else:
        text = text.strip("-")
    text_to_speak =text +"."
    tts = gTTS(text=text_to_speak, lang='en')
    tts.save("output.mp3")

    # Play the audio using a system command (platform-dependent)
    if os.name == "nt":  # for Windows
        os.system("start output.mp3")
    else:  # for macOS and Linux
        os.system("xdg-open output.mp3")
    return

if __name__ == "__main__":
    text_to_pronounce = "Hello, I am a Python program. Nice to meet you!"
    pronounce_text(text_to_pronounce)
