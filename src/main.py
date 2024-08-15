import sys
import re
from .messages import help_message, version_message
from src.settings import Singleton
import openai

def main():
    handler = Singleton()

    def generate_pattern(prompt: str):
        """
        Generate a regex pattern that match the given condition

        Args:
            prompt str: The condition to match in natural language

        Returns:
            str: The generated regex pattern
        """
        try:
            result = handler.client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": "You just answer with python regex pattern, nothing else, do not use markdown, the result generated is passed directly into re.match",
                    }, 
                    {
                        "role": "user", "content":f" Generate a regex pattern that match this condition: {prompt}"
                    }
                ],
                model="gpt-4o",
            )
            result = result.choices[0].message.content
            handler.console.print("Regex Pattern:", result, style="bold violet")
            return result
        except openai.error.InvalidRequestError:
            handler.console.print("Invalid request", style="bold red")
            sys.exit(1)
        except openai.error.APIConnectionError:
            handler.console.print("API connection error", style="bold red")
            sys.exit(1)
        except openai.error.AuthenticationError:
            handler.console.print("Authentication error", style="bold red")
            sys.exit(1)
        except openai.error.RateLimitError:
            handler.console.print("Rate limit error", style="bold red")
            sys.exit(1)
        

    if len(sys.argv) > 1:
        arg = sys.argv[1]
    else:
        handler.console.print("ERROR: No argument given", style="bold red")
        handler.console.print(help_message, style="bold blue")
        sys.exit(1)
        
    if arg == "--help" or arg == "-h":
        handler.console.print(help_message, style="bold blue")
        sys.exit(0)
        
    if arg == "--version" or arg == "-v":
        handler.console.print(version_message, style="bold blue")
        sys.exit(0)

    if sys.stdin.isatty():
        handler.console.print("ERROR: No input data", style="bold red")
        handler.console.print(help_message, style="bold blue")
        sys.exit(1)

        
    pattern = generate_pattern(arg)

    for line in sys.stdin.readlines():
        res = re.match(pattern, line)
        if res is not None:
            handler.console.print(line, end="", style="bold green")
        
    sys.exit(0)
        