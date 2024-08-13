from src import __version__

help_message = """

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
                                         


lgrep is a tool that generates a regex pattern from a natural language condition and uses it to filter lines from stdin.


Usage: command | lgrep 'condition'
     Examples:
          - cat file.txt | lgrep 'lines that contain the word "error"'
          - ls | lgrep 'files that are not directories'
          - find . | lgrep 'filter images'

Options:
     -h, --help: show this help message
     -v, --version: show lgrep version
     -s, --settings: show lgrep settings


Created by: Francesco Mattioli
"""

version_message = f"""

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
                                         
lgrep version {__version__}
"""

key_not_found_message = """
OPENAI_API_KEY not found in environment variables. 

To set it, add 'export OPENAI_API_KEY=your_openai_api_key_here' to your shell configuration file (e.g., ~/.bashrc or ~/.zshrc) and run 'source ~/.bashrc' or restart your terminal.

Example:

     echo 'export OPENAI_API_KEY=your_openai_api_key_here' >> ~/.bashrc
     source ~/.bashrc
 
"""