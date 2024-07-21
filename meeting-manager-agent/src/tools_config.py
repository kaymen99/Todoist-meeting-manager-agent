from src.tools.transcript import get_transcript
from src.tools.todoist import create_project, create_and_assign_task, get_project
from src.tools.telegram import send_message, receive_message

tools_list = [
    {
        "type": "function",
        "function": {
            "name": "get_transcript",
            "description": "Retrieve the transcript from the recorded Google Meet session.",
            "parameters": {
                "type": "object",
                "properties": {
                    "meeting_id": {
                        "type": "string",
                        "description": "The ID of the Google Meet session."
                    }
                },
                "required": ["meeting_id"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_project",
            "description": "Get the project with the given name.",
            "parameters": {
                "type": "object",
                "properties": {
                    "project_name": {
                        "type": "string",
                        "description": "The name of the project to get."
                    }
                 },
                "required": ["project_name"]
            }
        }
    },
    {
      "type": "function",
      "function": {
            "name": "create_project",
            "description": "Create a new project in Todoist",
            "parameters": {
                "type": "object",
                "properties": {
                    "project_name": {
                        "type": "string",
                        "description": "The name of the project to be created."
                    },
                },
                "required": ["project_name"]
            }
        },
    },
    {
      "type": "function",
      "function": {
            "name": "create_and_assign_task",
            "description": "Create and assign a task given its content to a user with user ID.",
            "parameters": {
                "type": "object",
                "properties": {
                    "project_id": {
                        "type": "string",
                        "description": "The id of the project to create the task in."
                    },
                    "assignee": {
                        "type": "string",
                        "description": "The name of the person to assign the task to."
                    },
                    "content": {
                        "type": "string",
                        "description": "The content of the task to create and assign to."
                    },
                    "due_date": {
                        "type": "string",
                        "description": "The due date of the task in human defined (ex.: 'next Monday', 'Tomorrow')."
                    }
                },
                "required": ["project_id", "assignee", "content"]
            }
          },
      },
      {
          "type": "function",
          "function": {
              "name": "send_message",
              "description": "Send a message to a Telegram group chat.",
              "parameters": {
                  "type": "object",
                  "properties": {
                      "text": {
                          "type": "string",
                          "description": "The message text to send."
                      }
                  },
                  "required": ["text"]
              }
          }
      }
]

available_functions = {
    "get_transcript": get_transcript,
    "get_project": get_project,
    "create_project": create_project,
    "create_and_assign_task": create_and_assign_task,
    "send_message": send_message
}