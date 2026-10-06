import os
import subprocess
import sys
from pathlib import Path


UNIT_ROOT = Path(__file__).resolve().parents[1]


def find_exercise_file(file_name, directory="exercises"):
    """Finds and returns the path to the specified file in either 'src/exercises' or 'src/lessons'."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    while True:
        target_dir = os.path.join(current_dir, 'src', directory)
        file_path = os.path.join(target_dir, file_name)

        if os.path.exists(file_path):
            return file_path

        parent_dir = os.path.dirname(current_dir)
        if parent_dir == current_dir:
            raise FileNotFoundError(f"Could not find {file_name} in the 'src/{directory}' directory")
        
        current_dir = parent_dir


def run_program(file_name, inputs, directory="exercises"):
    """Executes a Python file from either 'src/exercises' or 'src/lessons' with the given inputs."""
    file_path = find_exercise_file(file_name, directory=directory)
    
    process = subprocess.Popen(
        [sys.executable, file_path],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=UNIT_ROOT,
        text=True
    )
    
    input_string = "\n".join(map(str, inputs)) + "\n"
    stdout, stderr = process.communicate(input=input_string)
    
    return stdout.strip(), stderr
