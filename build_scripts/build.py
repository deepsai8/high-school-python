import os
from dotenv import load_dotenv
import subprocess

# Load the .env file
load_dotenv()

# Run the mkdocs build command
subprocess.run(['mkdocs', 'build'])
