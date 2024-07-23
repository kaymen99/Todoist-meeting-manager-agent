import requests, time, uuid, os, json
from todoist_api_python.api import TodoistAPI
from src.utils import convert_human_datetime

# Example collaborators for testing
collaborators = ["Mark T.", "John D.", "Jane S.", "Emily D."]

# Used for testing, need to setup some DB or API later on
name_to_email = {
    "Mark T.": "marktestuser1@gmail.com",
    "John D.": "john.doe.testuser1@gmail.com",
    "Jane S.": "jane.smith.exampleuser2@gmail.com",
    "Emily D.": "emily.doe.testuser1@gmail.com",
    "John": "john.doe.testuser1@gmail.com",
    "Jane": "jane.smith.exampleuser2@gmail.com",
    "Emily": "emily.doe.testuser1@gmail.com",
    "Mark": "marktestuser1@gmail.com"
}

# Initialize the Todoist API client
TODOIST_API_TOKEN = os.getenv("TODOIST_API_TOKEN")
api = TodoistAPI(TODOIST_API_TOKEN)

def get_user_id_by_name(project_id, name):
    try:
        collaborators = api.get_collaborators(project_id=project_id)
        for collaborator in collaborators:
            if collaborator.email == name_to_email[name]:
                return collaborator.id
        return "User not found"
    except Exception as error:
        return error

def get_project(project_name):
  try:
      projects = api.get_projects()
      for project in projects:
          name = project.name
          if name.lower().strip() == project_name.lower().strip():
            return str({
                "name": name,
                "project_id": project.id,
                "exists": True
            })
      return "Project Dos Not exist"
  except Exception as error:
      print(error)
      return "Project Dos Not exist"

def create_project(project_name):
  # Create a new project
  project = api.add_project(name=project_name)
  project_id = project.id
  print(f'Created project with ID: {project_id}')

  # Share projet with collaborators
  share_project_with_colleborators(project_id)
  print(f'Shared project with collaborators')
  return str({
      "name": project_name,
      "project_id": project_id,
      "created": True
  })

def create_and_assign_task(project_id, assignee, content, due_date=""):
  # Get user id
  user_id = get_user_id_by_name(project_id, assignee)

  # Convert human date to datetime
  if due_date:
    due_date = convert_human_datetime(due_date)
    due_date = due_date.strftime('%Y-%m-%d')  # Format as 'YYYY-MM-DD'

  # add task
  task = api.add_task(
      content=content,
      project_id=project_id,
      due_date=due_date
  )
  print(f'Added task with ID: {task.id}')

  # assign task
  task_id = task.id
  assign_task(task_id, user_id)
  return str({
      "user_id": user_id,
      "user_name": assignee,
      "content": content,
      "due_date": due_date,
      "assigned": True
  })

def share_project(project_id, email):
    url = "https://api.todoist.com/sync/v9/sync"
    headers = {
        "Authorization": f'Bearer {TODOIST_API_TOKEN}',
        "Content-Type": "application/json"
    }
    command_uuid = str(uuid.uuid4())
    data = {
        "commands": [
            {
                "type": "share_project",
                "temp_id": str(uuid.uuid4()),
                "uuid": command_uuid,
                "args": {
                    'project_id': project_id,
                    'email': email
                }
            }
        ]
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    response_json = response.json()
    if response_json.get('sync_status', {}).get(command_uuid) == 'ok':
        print(f'Successfully shared project with {email}')
    else:
        print(f'Failed to share project with {email}')

def share_project_with_colleborators(project_id):
    for collaborator in collaborators:
        share_project(project_id, name_to_email[collaborator])

def assign_task(task_id, user_id):
    url = "https://api.todoist.com/sync/v9/sync"
    headers = {
        "Authorization": f'Bearer {TODOIST_API_TOKEN}',
        "Content-Type": "application/json"
    }

    command_uuid = str(uuid.uuid4())
    data = {
        "commands": [
            {
                "type": "item_update",
                "uuid": command_uuid,
                "args": {
                    "id": task_id,
                    "responsible_uid": user_id
                }
            }
        ]
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    response_json = response.json()
    if response_json.get('sync_status', {}).get(command_uuid) == 'ok':
        print(f'Successfully assigned task {task_id} to user {user_id}')
    else:
        print(f'Failed to assign task {task_id} to user {user_id}')
