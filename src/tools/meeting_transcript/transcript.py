from pydantic import Field
from src.tools.base_tool import BaseTool
from .utils import transcript1, transcript2

# use dummy but realistic transcripts for testing the agent behaviour
# We'll implement later functions to extract transcript from: Google Meet, Discord or whatsAPP/Telegram
def get_transcript(meeting_id):
  """
  Retrieve the transcript from the recorded Google Meet session.
  """
  if meeting_id == "1":
    return transcript1
  elif meeting_id == "2":
    return transcript2
  

class GetTranscript(BaseTool):
    """
    A tool that retrieve the transcript from the recorded Google Meet session.
    """
    meeting_id: str = Field(description='The ID of the Google Meet session.')
    
    def run(self):
        return get_transcript(self.meeting_id)