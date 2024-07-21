import os
from dotenv import load_dotenv
from src.agent import Agent
from src.prompts import meeting_manager_prompt
from src.tools_config import tools_list, available_functions

load_dotenv()

# Use LLAMA3 with Groq but can be raplace with any other LLM (see LiteLLM docs)
model = "groq/llama3-70b-8192"

meeting_manager = Agent("Meeting Manager", model, tools_list, available_functions, meeting_manager_prompt)

if __name__ == "__main__":
    # agent is expecting the meeting id to be able to extract transcript
    query = "Meeting id: 2"

    # invoke agent to handle projects and tasks assignement
    print("Handling Meeting assignements...")
    meeting_manager.invoke(query)