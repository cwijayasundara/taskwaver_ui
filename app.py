import os
import subprocess

path = 'TaskWeaver/playground/UI/'
os.chdir(path)

subprocess.run(['chainlit', 'run', 'app.py'], check=True)
