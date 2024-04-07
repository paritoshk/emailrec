# The class defines an EmailAssistant that utilizes the Anthropic API to generate AI responses based
# on user profiles and email data.
import json
from anthropic import Anthropic
import pandas as pd
from typing import List
import os
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

class UserProfile:
    # This Python class `UserProfile` represents a user profile with attributes such as age, gender,
    # organization role, relative business, and priority for emails.
    def __init__(self, age: int, gender: str, org_role: str, relative_business: str, priority_for_emails: List[str]):
        self.age = age
        self.gender = gender
        self.org_role = org_role
        self.relative_business = relative_business
        self.priority_for_emails = priority_for_emails
class EmailAssistant:
    # The EmailAssistant class prepares email data and user profile information to generate AI responses
    # for email-related queries.
    def __init__(self, user_profile: UserProfile, email_json_path: str, base_system_prompt: str):
        self.user_profile = user_profile
        self.email_data = pd.read_json(email_json_path)
        self.base_system_prompt = base_system_prompt
        self.client = Anthropic(api_key=ANTHROPIC_API_KEY)
    def generate_system_prompt_with_profile(self) -> str:
        profile_details = (
            f"The user is a {self.user_profile.age} year old {self.user_profile.gender}, "
            f"working as a {self.user_profile.org_role} in {self.user_profile.relative_business}. "
            f"Their priority for emails includes {', '.join(self.user_profile.priority_for_emails)}."
        )
        return self.base_system_prompt + " " + profile_details
    def prepare_email_summary(self):
        """
        Prepare a summary of the emails to insert into the system prompt.
        This function simplifies email details into a summary that can be
        understood by the Anthropic model.
        """
        summaries = []
        for email_dict in self.email_data.emails:
            # email_dict is already a dictionary here, so you can directly access its keys
            summary = f"Email from {email_dict['from']} , subject: {email_dict['subject']}, received at {email_dict['deliveredAt']} with snippet {email_dict['snippet']}."
            summaries.append(summary)
        return " ".join(summaries)
    def generate_ai_response(self, user_input: str) -> str:
        system_prompt = self.generate_system_prompt_with_profile() + " " + self.prepare_email_summary()
        response = self.client.messages.create(
            model="claude-3-opus-20240229",
            messages=[{"role": "user", "content": user_input}],
            system=system_prompt,
            max_tokens=2500,
        )
        return response.content[0].text





if __name__ == "__main__":
        # Example Usage:
    base_system_prompt = """
    You are a friendly and motivational email management assistant,
    and responder for corporate professionals working in tech like product 
    and program managers, founders, and senior executives. 
    You help prioritize emails based on urgency, the user's schedule,
    and predefined preferences and curated. You are capable of suggesting 
    responses to key emails and providing summaries of emails when requested.
    """
    user_profile = UserProfile(
        age=35, 
        gender="Non-binary", 
        org_role="Product Manager", 
        relative_business="Tech Startups", 
        priority_for_emails=["urgent", "deadline", "meeting"])
    email_assistant = EmailAssistant(user_profile, "data/emails.json", base_system_prompt)
    user_input = "Based on my schedule and priorities, what are some of my top three emails for today? Which one should I read and respond to the most?"
    ai_response = email_assistant.generate_ai_response(user_input)
    print(ai_response)


"""SAMPLE RESPONSE:

Based on the emails provided and your stated priorities, here are the top emails to focus on today:

1. Re: OAuth Verification Request for Project Beams-Infra-Staging (id: beams-infra-staging)
   - From: jana@usebeams.com
   - To: api-oauth-dev-verification-reply+0mkvoso0guwhq1d@google.com
   - Reason: This seems to be an urgent email related to OAuth verification for a project. As a Product Manager, ensuring the smooth integration and functioning of OAuth is likely a high priority.

2. Re: Pam (Pebblebed) meet Jana, Mihri (Beams
   - From: jana@usebeams.com 
   - To: vagata@pebblebed.com
   - Reason: Scheduling a meeting with Pam from Pebblebed seems to be a priority based on the follow-up email. As the meeting is proposed for 4/9, responding to confirm the meeting time should be done today.

3. Re: Excited to meet soon!
   - From: jana@usebeams.com
   - To: JChen@foundationcap.com
   - Reason: Following up on a previous meeting and scheduling a more detailed discussion with Joanne from Foundation Capital is important for maintaining the relationship and potentially securing funding or partnership opportunities.

The other emails, while important, seem to be either already responded to or not as time-sensitive based on the limited information provided in the snippets."""
