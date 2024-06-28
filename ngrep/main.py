import sys
import os
import openai
import re

token = os.environ["OPENAI_API_KEY"]

client = openai.Client(api_key=token)

def generate_pattern(prompt):
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
    

arg = sys.argv[1]

if sys.stdin.isatty():
    print("No input data")
    sys.exit(1)
    

    
pattern = generate_pattern(arg)

for line in sys.stdin.readlines():
    res = re.match(pattern, line)
    if res is not None:
        print(line, end="")
    
sys.exit(0)
    