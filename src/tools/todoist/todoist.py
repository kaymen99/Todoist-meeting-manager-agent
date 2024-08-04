from pydantic import Field
from src.tools.base_tool import BaseTool
from .utils import get_project, create_project, create_and_assign_task

class GetProject(BaseTool):
    """
    A tool that retrieve the project with the given name.
    """
    project_name: str = Field(description='The name of the project to get.')

    def run(self):
        return get_project(self.project_name)

class CreateProject(BaseTool):
    """
    A tool that create a new project in Todoist.
    """
    project_name: str = Field(description='The name of the project to be created.')

    def run(self):
        return create_project(self.project_name)

class CreateAndAssignTask(BaseTool):
    """
    A tool that create and assign a task given its content to a user with user ID.
    """
    project_id: str = Field(description='The id of the project to create the task in.')
    assignee: str = Field(description='The name of the person to assign the task to.')
    content: str = Field(description='The content of the task to create and assign to.')
    due_date: str = Field(description='The due date of the task in human defined (ex.: "next Monday", "Tomorrow").')

    def run(self):
        return create_and_assign_task(self.project_id, self.assignee, self.content, self.due_date)