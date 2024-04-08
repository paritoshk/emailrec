
from pathlib import Path
from openai import OpenAI
import os
OPENAI_API_KEY = os.getenv("OPEN_AI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

USER_PERSONA_TEXT_AVA ="""I'm Ava, founder and CEO of GigaMinds, a SF startup. 
We're a team of 10, hustling to make AI dreams a reality. 
My days are a whirlwind of coding, steering the ship, and chasing funding.
Right now, my focus is on securing our next round. 
We're deep into developing MindWave AI and forging partnerships. 
Based in the heart of San Francisco, I'm always buzzing with ideas. 
When I'm not working, you'll find me 
splashing colors at my best friend's atelier, experimenting with coffee,
or dancing at a good rave - so make sure I don't miss out when my favorite DJs
are playing in town. 
I am a 28 years old female."""
USER_PERSONA_TEXT_MAX = """I'm Max, a 35-year-old software engineer, a tech company near Seattle. 
I am a senior developer at BinaryBeats, a Series A stage remote first company. 
My role here is to ensure our tech is firing on all cylinders, 
from debugging to pushing the boundaries of innovation. Currently, 
my focus is on optimizing our app's performance, 
diving deep into projects that involve revamping UI/UX and integrating cutting-edge AI technology.
I'm based remotely in a cozy rural area of Washington.
Outside of the coding realm, you'll find me shredding on my skateboard, 
or getting lost in the latest tech gadgets."""
class TextToSpeechConverter:
    def __init__(self, api_key, output_dir="data"):
        self.client = OpenAI(api_key=api_key)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)  # Ensure output directory exists
    def convert_to_speech(self, text, output_filename):
        # Define the full path for the output file
        output_file_path = self.output_dir / f"{output_filename}.mp3" 
        # Create the audio speech
        response = self.client.audio.speech.create(
            model="tts-1",
            voice="onyx",
            input=text
        )
        # Save the binary audio content to the file
        response.stream_to_file(output_file_path)
        return None


# Usage
if __name__ == "__main__":
    OPENAI_API_KEY = os.getenv("OPEN_AI_API_KEY")
    tts_converter = TextToSpeechConverter(api_key=OPENAI_API_KEY)
    greeting_message = """  Welcome to EmailWand, your personal email concierge! 
                            I'm here to help you navigate through your busy inbox with ease. 
                            Let's focus on what matters most today. 
                            For starters, you might want to ask, 'What are my top three emails for today?'"""
    tts_converter.convert_to_speech(greeting_message, "greeting_message")