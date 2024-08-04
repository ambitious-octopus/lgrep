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

