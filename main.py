from dotenv import load_dotenv
from src.agents.agent import Agent
from src.prompts import meeting_manager_prompt
from src.tools.meeting_transcript.transcript import GetTranscript
from src.tools.todoist.todoist import GetProject, CreateProject, CreateAndAssignTask
from src.tools.telegram.telegram import SendTelegramMessage

load_dotenv()

# Use LLAMA3 with Groq but can be raplace with any other LLM (see LiteLLM docs)
model = "groq/llama3-70b-8192"
# model = "groq/llama-3.1-70b-versatile"
# model = "gemini/gemini-1.5-flash"

# agent tools
tools_list = [
    GetTranscript,
    GetProject,
    CreateProject,
    CreateAndAssignTask,
    SendTelegramMessage
]

# Initiate the meeting manager agent
meeting_manager = Agent("Meeting Manager", model, tools_list, system_prompt=meeting_manager_prompt)

if __name__ == "__main__":
    # agent is expecting the meeting id to be able to extract transcript
    query = "Meeting id: 1"

    # invoke agent to handle projects and tasks assignement
    print("Handling Meeting assignements...")
    meeting_manager.invoke(query)