from gpiozero import LED
import speech_recognition as sr
from threading import Thread

# Initialize LED
led = LED(18)

# Initialize recognizer and microphone
recognizer = sr.Recognizer()
mic = sr.Microphone()

# Function to listen to voice commands
def listen_commands():
    while True:
        try:
            with mic as source:
                recognizer.adjust_for_ambient_noise(source)
                print("Listening for command...")
                audio = recognizer.listen(source)

            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")

            if "on" in command:
                led.on()
                print("LED is ON")
            elif "off" in command:
                led.off()
                print("LED is OFF")

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError:
            print("Network error, check internet connection")

# Run in a background thread
listener_thread = Thread(target=listen_commands, daemon=True)
listener_thread.start()

# Keep program running
try:
    while True:
        pass
except KeyboardInterrupt:
    print("\nExiting...")
    led.off()