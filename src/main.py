import sys
import re
from .messages import help_message, version_message
from src.settings import Singleton
import openai

def main():
    handler = Singleton()

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

        
    handler.run(arg)
        
    sys.exit(0)
        