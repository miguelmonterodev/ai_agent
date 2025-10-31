import os
from google.genai import types

def get_file_content(working_directory, file_path):
    abs_dir_path = os.path.abspath(working_directory)
    abs_file_path = os.path.join(abs_dir_path, file_path)
    if not abs_file_path.startswith(abs_dir_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    with open(abs_file_path, "r") as file:
        content = file.read()
        file.seek(0)
        truncated_content = file.read(10000)
        if len(content) > 10000:
            return truncated_content + f'[...File "{file_path}" truncated at 10000 characters]'
        return content

# Function Declaration
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Reads and returns the first 10000 characters of the content from a specified file within the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file whose content should be read, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)