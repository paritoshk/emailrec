from openai import OpenAI
import os
OPENAI_API_KEY = os.getenv("OPEN_AI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)
class GetUserData:
    def __init__(self):
        OPENAI_API_KEY = os.getenv("OPEN_AI_API_KEY")
        self.client = OpenAI(api_key=OPENAI_API_KEY)
    def transcribe_audio(self, audio_file_path):
        """Transcribe the provided audio file to text."""
        with open(audio_file_path, "rb") as audio_file:
            transcription = self.client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
                response_format="text"
            )
        return transcription
    def extract_user_profile(self, transcription:str):
        """Use GPT4-Turbo to extract user profile information from the transcription in a JSON format."""
        system_prompt = """"  You're an intelligent assistant tasked with extracting specific information from a user's 
            spoken words transcribed to text. Based on the transcription, generate a structured summary 
            including age, gender, organizational role, industry or business, and a list of priorities for emails. 
            The 'Priority for Emails' should include any additional data that wasn't categorized.
            YOU MUST return a summary in JSON format  Include any additional data that was not categorized as last element of
            'Priority for Emails List'. like this additional_data = ['...additional_data_HERE']
            Format the summary example as follows, if you cannot determine try guessing:\n"
            "USER_PROFILE={\"Age\": [age], \"Gender\": [gender], \"Organizational_Role\": [org_role], "
            "\"Industry_Business\": [industry_or_business], \"Priority_for_Emails\": [priorities, including additional_data]}.\n\n"""""    
        user_prompt = f"""Transcription:{transcription}"""
        completion = self.client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.05,
            max_tokens=300,  # Adjust based on your expected output length
            response_format={"type": "json_object"}  # Ensure this parameter is used correctly according to API documentation
        )
        extracted_info= completion.choices[0].message.content
        return extracted_info
        
if __name__ == "__main__":
    user_data_getter = GetUserData()
    # Path to your audio file
    audio_file_path = "data/AVA_PERSONA.mp3"
    # Step 1: Transcribe Audio
    transcription_result = user_data_getter.transcribe_audio(audio_file_path)
    transcription_text = transcription_result # Adjust based on actual key in response
    print("Transcription:", transcription_text)
    # Step 2: Extract User Profile
    extracted_info = user_data_getter.extract_user_profile(transcription_text)
    print("Extracted User Profile Information:", extracted_info)