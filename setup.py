import subprocess
from os import system

if __name__ == "__main__":
    # set up for the program
    subprocess.run("python -m venv .\\.venv")
    # activate the python environment
    system('''.\\.venv\\Scripts\\activate && python -m pip install -r .\\requirements.txt && python main.py''')