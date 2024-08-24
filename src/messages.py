from src import __version__

logo = """
 /$$                                        
| $$                                        
| $$  /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$ 
| $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$
| $$| $$  \ $$| $$  \__/| $$$$$$$$| $$  \ $$
| $$| $$  | $$| $$      | $$_____/| $$  | $$
| $$|  $$$$$$$| $$      |  $$$$$$$| $$$$$$$/
|__/ \____  $$|__/       \_______/| $$____/ 
     /$$  \ $$                    | $$      
    |  $$$$$$/                    | $$      
     \______/                     |__/       

"""


help_message = f"""

{logo}      
                                         

lgrep is a tool that generates a regex pattern from a natural language condition and uses it to filter lines from stdin.


Usage: command | lgrep 'condition'
     Examples:
          - cat file.txt | lgrep 'the word "error"'
          - ls | lgrep 'python-related files'
          - find . | lgrep 'filter images'

Options:
     -h, --help: show this help message
     -v, --version: show lgrep version
     -p, --pattern: show only the generated regex pattern
     

"""

version_message = f"""

{logo}   
                                         
lgrep version {__version__}
"""

key_not_found_message = """
OPENAI_API_KEY not found in environment variables. 

To set it, add 'export OPENAI_API_KEY=your_openai_api_key_here' to your shell configuration file (e.g., ~/.bashrc or ~/.zshrc) and run 'source ~/.bashrc' or restart your terminal.

Example:

     echo 'export OPENAI_API_KEY=your_openai_api_key_here' >> ~/.bashrc
     source ~/.bashrc
 
"""