import os
import openai
import sys
import re
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
        
    def run(self, prompt):
        try:
            result = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": "You just answer with regex pattern, nothing else, do not use markdown, the result generated is passed directly into re.match",
                    }, 
                    {
                        "role": "user", "content":f" Generate a regex pattern that match this condition: {prompt}"
                    }
                ],
                model="gpt-4o",
            )
            pattern = result.choices[0].message.content
            self.console.print("Regex Pattern:", result, style="bold violet")
            return result
        except openai.error.InvalidRequestError:
            self.console.print("Invalid request", style="bold red")
            sys.exit(1)
        except openai.error.APIConnectionError:
            self.console.print("API connection error", style="bold red")
            sys.exit(1)
        except openai.error.AuthenticationError:
            self.console.print("Authentication error", style="bold red")
            sys.exit(1)
        except openai.error.RateLimitError:
            self.console.print("Rate limit error", style="bold red")
            sys.exit(1)
        
        for line in sys.stdin.readlines():
            res = re.match(pattern, line)
        if res is not None:
            self.console.print(line, end="", style="bold green")
        
        
    def check_openai_api_key(self):
        try:
            self.client.models.list()
        except openai.AuthenticationError:
            return False
        else:
            return True
    
    