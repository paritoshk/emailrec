USER_PERSONA_TEXT ="""I'm Ava, founder and CEO of GigaMinds, a SF startup. 
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

from pathlib import Path
from openai import OpenAI
client = OpenAI(api_key="sk-YourApiKey")

speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="nova",
  input=USER_PERSONA_TEXT
)

response.stream_to_file(speech_file_path)