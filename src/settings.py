import os
import openai
from rich.console import Console
from src.messages import key_not_found_message


class Singleton:
    def __init__(self) -> None:
        self.console = Console()
        try:
            self.token = os.environ["OPENAI_API_KEY"]
        except KeyError:
            self.console.print(key_not_found_message, style="bold red")
            raise SystemExit(1)
        
        self.client = openai.Client(api_key=self.token)
        
        
    def check_openai_api_key(self):
        try:
            self.client.models.list()
        except openai.AuthenticationError:
            return False
        else:
            return True
    
    