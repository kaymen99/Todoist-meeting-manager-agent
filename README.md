# TODOIST Meeting Manager Agent

I built an AI-powered system to streamline project and task management in Todoist using transcripts from Google Meet, WhatsApp, or Telegram. This project automates the process of creating projects, identifying and assigning tasks from team conversations, ensuring accurate task tracking and project management in the Todoist app.

## Features

- **Transcript Extraction**: Automatically retrieve and analyze transcripts from Google Meet, WhatsApp, or Telegram.
- **Project and Task Identification**: Detect and categorize projects and tasks from the conversation transcripts.
- **Todoist Integration**: Verify, create, and update projects and tasks in Todoist.
- **Team Communication**: Use Telegram to contact the team in order to clarify task details and confirm assignments.

### Agent Available Tools

- **Todoist API**: i leveraged the Todoist API to build functions that simplify the creation of new projects and the assignement of task to the team members, these are the main functions used (can be found under `tools/todoist`): `create_and_assign_task`, `create_project`, `get_project`
- **Transcript Extraction**: The agent will be able to extract transcript of team conversations or meetings from a specified source (setup beforhand) like Google Meet, whatsApp or Telegram. A single function `get_transcript` is built for this and it can be changed to integrate with any  of the aforementioned sources.

- **Telegram API**: The agent will also have the possibility to communicate with the team through Telegram group chat with the `send_message` function, in order to seek some clarification during tasks assignements or to ask permissions for the creation of new projects.

## How to Run

### Prerequisites

- Python 3.9+
- Groq API key
- Todoist API key
- Create a Telegram Bot
- Necessary Python libraries (listed in `requirements.txt`)

### Setup

1. **Clone the repository:**

   ```sh
   git clone https://github.com/kaymen99/ai-agents-projects/meeting-manager-agent.git
   cd ai-agents-projects/meeting-manager-agent
   ```

2. **Create and activate a virtual environment:**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Create a Telegram Bot (just ask GPT how to create a Telegram Bot)**

5. **Create a Todoist account [here](https://todoist.com) and obtain an API key**

6. **Set up environment variables:**

   Create a `.env` file in the root directory of the project and add your API keys:

   ```env
   TODOIST_API_KEY=your_todoist_api_key
   GROQ_API_KEY=your_groq_api_key
   TELEGRAM_TOKEN=your_telegram_bot_token
   CHAT_ID=chat_id_with_your_bot
   ```

### Running the Application

1. **The agent requires the meeting id to start, which can be updated in the `main.py` script the run the agent with:**

   ```sh
   python main.py
   ```

Currently the project is still under development, the `get_transcript` function is not yet connected with a real conversations source (Google Meet, whatsApp,...), the function retrieve sample transcripts generated using chatGPT (which can be found in `tools/transcript`).

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## Contact

If you have any questions or suggestions, feel free to contact me at `aymenMir10001@gmail.com`.