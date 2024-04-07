# emailrec
Recommendation system for email answering using voice commands, flow engineering and RAG with LLMs and Elevenlabs
### SRC

#### Objective

The objective of this project is to create an Email Assistant using the Anthropic API. This assistant aims to help users, particularly those in corporate environments such as tech product managers, founders, and senior executives, to prioritize their emails. It identifies top emails based on urgency, the user's schedule, and predefined preferences, offering suggestions for responses and summaries of key emails.

#### Architecture

The project consists of two main classes:

- `UserProfile`: Manages user-specific information that influences email prioritization, including age, gender, organizational role, business relevance, and priority keywords for filtering emails.
- `EmailAssistant`: Handles the interaction with the Anthropic API to generate personalized email recommendations based on the user profile and a summary of emails provided in JSON format.

The interaction flow is as follows:

1. The `UserProfile` instance is created with specific attributes of the user.
2. The `EmailAssistant` is initialized with the `UserProfile`, the path to the email data in JSON format, and a base system prompt.
3. The assistant prepares a detailed prompt incorporating the user's profile and a summary of the emails.
4. Using this prompt, it requests the Anthropic API to analyze the emails and suggest prioritization based on the user's needs.
5. The API's response is processed and presented to the user, offering insights into which emails should be addressed first.

#### Code Overview

The code is structured around the two classes (`UserProfile` and `EmailAssistant`) and a main block that demonstrates their usage:

- `UserProfile` captures essential details about the user which might affect email prioritization.
- `EmailAssistant` utilizes these details along with the email data to interact with the Anthropic API, leveraging natural language processing to aid in email management.

**Improvements and Documentation:**

- **UserProfile Class:**
  - **Purpose:** Stores user-related information to customize email prioritization.
  - **Attributes:** Age, gender, organizational role, business sector, and a list of keywords for prioritizing emails.
  - **Usage:** Instantiated with user details to reflect preferences and needs in email management.

- **EmailAssistant Class:**
  - **Purpose:** Manages the processing of email data and interaction with the Anthropic API for generating prioritized email lists and suggestions.
  - **Key Methods:**
    - `generate_system_prompt_with_profile`: Creates a detailed prompt for the API, incorporating user profile information.
    - `prepare_email_summary`: Summarizes email data to be included in the API prompt.
    - `generate_ai_response`: Generates a prioritized list of emails and suggestions by interacting with the Anthropic API.
  - **API Interaction:** Uses the Anthropic API key (retrieved from environment variables for security) to request analysis and recommendations.

#### Running the Project

1. Ensure the Anthropic API key is set as an environment variable (`ANTHROPIC_API_KEY`).
2. Place the email JSON data in the specified path (`data/emails.json`).
3. Update the `UserProfile` instantiation in the main block with actual user details.
4. Run the script to see the prioritized emails and recommendations based on the user's profile and provided email data.

This project demonstrates the potential of integrating advanced AI capabilities into daily workflows, specifically for email management, leveraging user-specific data to tailor recommendations and enhance productivity.