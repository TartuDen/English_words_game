import pyttsx3

def pronounce_text(text):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    # print(text)
    if "/" in text:
        text = text.split("/")[0]
        # text = text.strip("/")
    elif "[" in text:
        text = text.split("[")[0]
    else:
        text = text.strip("-")
    # print("in voice: ", text)

    # Set properties (optional)
    # You can set properties like voice, rate, volume, etc.
    # For example:
    engine.setProperty('rate', 160)  # Speed of speech (words per minute)
    engine.setProperty('volume', 1.0)  # Volume level (0.0 to 1.0)

    # Pronounce the text
    engine.say(text)

    # Wait for the speech to finish
    engine.runAndWait()

if __name__ == "__main__":
    text_to_pronounce = "Hello, I am a Python program. Nice to meet you!"
    pronounce_text(text_to_pronounce)
