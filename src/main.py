import sys
from .messages import help_message, version_message
from src.handler import Singleton

def main():
    singleton = Singleton()
    option, prompt = singleton.parse_cli(sys.argv)
        
    if option in {"--help","-h"}:
        singleton.console.print(help_message, style="bold blue")
        sys.exit(0)
        
    if option in {"--version", "-v"}:
        singleton.console.print(version_message, style="bold blue")
        sys.exit(0)
    
    if option in {"--pattern","-p"}:
        singleton.run(prompt, just_pattern=True)
        sys.exit(0)

    if sys.stdin.isatty():
        singleton.console.print("ERROR: No stdin data", style="bold red")
        singleton.console.print(help_message, style="bold blue")
        sys.exit(1)

        
    singleton.run(prompt)
        
    sys.exit(0)
        