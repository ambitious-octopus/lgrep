import sys
import os
import openai
import re
from rich.console import Console

console = Console()
token = os.environ["OPENAI_API_KEY"]
client = openai.Client(api_key=token)

def generate_pattern(prompt: str):
    """
    Generate a regex pattern that match the given condition

    Args:
        prompt str: The condition to match in natural language

    Returns:
        str: The generated regex pattern
    """
    result = client.chat.completions.create(
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
    return result
    

if len(sys.argv) > 1:
    arg = sys.argv[1]
else:
    console.print("No argument given", style="bold red")
    sys.exit(1)

if sys.stdin.isatty():
    console.print("No input data", style="bold red")
    sys.exit(1)
    

    
pattern = generate_pattern(arg)

for line in sys.stdin.readlines():
    res = re.match(pattern, line)
    if res is not None:
        console.print(line, end="", style="bold green")
    
sys.exit(0)
    