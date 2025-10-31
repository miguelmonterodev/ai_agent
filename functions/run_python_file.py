import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    abs_dir_path = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_dir_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    if not abs_file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    process = subprocess.run(
        args=["python", file_path, *args], 
        cwd=abs_dir_path, 
        timeout=30, 
        capture_output=True,
        text=True,
        )
    out= process.stdout
    err = process.stderr
    errcode = process.returncode
    if errcode != 0:
        return f'{err}'
    if out == None:
        return "No output produced."
    return (f"STDOUT: {out} STDERR: {err}")

# Function Declaration
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file within the working directory and returns the output from the interpreter.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Optional arguments to pass to the Python file.",
                ),
                description="Optional arguments to pass to the Python file.",
            ),
        },
        required=["file_path"],
    ),
)