import sys
import os
import openai
import re

token = os.environ["OPENAI_API_KEY"]

client = openai.Client(api_key=token)


def call(stdin, text):

    result = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You just answer with python regex pattern, nothing else, do not use markdown, the result generated is passed directly into re.match",
            }, 
            {
                "role": "user", "content":f" Generate a regex pattern that match this condition: {text}"
            }
        ],
        model="gpt-4o",
    )
    result = result.choices[0].message.content
    # print(result)
    lines = stdin.split("\n")
    for line in lines:
        res = re.match(result, line)
        if res is not None:
            start, end = res.span()  # get the start and end positions of the match
            # Print the line with the matched characters in color
            colored_line = (
                line[:start] +
                '\033[91m' +  # ANSI code for red
                line[start:end] +
                '\033[0m' +  # ANSI code to reset color
                line[end:]
            )
            print(colored_line)
       
        
        
    # print(type(result))
    # x = re.search("^The.*Spain$", stdin)
    # print(x)
    # print(x)

# total arguments
arg = sys.argv[1]
# print(len(arg))

data = sys.stdin.read()
call(data, arg)
sys.exit(0)