import os
import openai
from rich.console import Console


class Singleton:
    def __init__(self) -> None:
        self.console = Console()
        try:
            self.token = os.environ["OPENAI_API_KEY"]
        except KeyError:
            self.console.print("No api key found", style="bold red")
            raise SystemExit(1)
        
        
        self.client = openai.Client(api_key=self.token)    
    
    