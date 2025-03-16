"""
Code Modification Tool

This script uses LLMs to apply changes to code files based on natural language descriptions.

Usage:
    python app.py --file PATH_TO_FILE --description "Description of changes to make"

Arguments:
    --file, -f        Path to the file to modify
    --description, -d Description of the changes to make

Example:
    python app.py --file examples/example.py --description "Add a new function called 'greet' that prints 'Hello, User!'"

Environment Variables:
    XAI_API_KEY       Your X.AI API key
"""

from openai import OpenAI
import os
import argparse

# Function to read the content of the file
def read_file(file_path):
    """Read the content of the specified file."""
    with open(file_path, 'r') as file:
        return file.read()

# Function to write the updated content back to the file
def write_file(file_path, content):
    """Write the updated content back to the specified file."""
    with open(file_path, 'w') as file:
        file.write(content)

# Function to generate the updated file content using the LLM
def generate_updated_content(original_content, user_description):
    """Send the file content and user description to the LLM and get the updated content."""
    # Construct the prompt for the LLM
    prompt = f"""
    You are an AI code editor. Below is the content of a file and a description of changes requested by the user. 
    Please provide the updated version of the file content based on the user's description.

    **Original File Content:**
    ```
    {original_content}
    ```

    **User's Description of Changes:**
    {user_description}

    **Updated File Content:**
    Output the entire updated file content below, enclosed in triple backticks (```). Only include the code, no explanations or comments.
    """
    
    XAI_API_KEY = os.getenv("XAI_API_KEY")
    if not XAI_API_KEY:
        raise ValueError("XAI_API_KEY environment variable is not set")
    
    client = OpenAI(
        api_key=XAI_API_KEY,
        base_url="https://api.x.ai/v1",
    )
    
    completion = client.chat.completions.create(
        model="grok-2-latest",
        messages=[
            {
                "role": "system",
                "content": "You are an AI programming assistant. Help modify the provided code according to user requirements."
            },
            {
                "role": "user",
                "content": prompt
            },
        ],
    )

    # Extract the updated content from the response
    updated_content = completion.choices[0].message.content.strip()
    
    # Extract the code block between triple backticks
    if updated_content.startswith("```") and updated_content.endswith("```"):
        updated_content = updated_content[3:-3].strip()
    
    return updated_content

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Apply code changes using LLM based on natural language description")
    parser.add_argument("--file", "-f", required=True, help="Path to the file to modify")
    parser.add_argument("--description", "-d", required=True, help="Description of the changes to make")
    return parser.parse_args()

# Main function to apply changes and write them back to the file
def apply_changes(file_path, user_description):
    """Apply the user's requested changes to the file."""
    # Step 1: Read the original file content
    original_content = read_file(file_path)
    
    # Step 2: Generate the updated content using the LLM
    updated_content = generate_updated_content(original_content, user_description)
    
    # Step 3: Write the updated content back to the file
    write_file(file_path, updated_content)
    
    print(f"File '{file_path}' has been updated successfully.")

# Example usage
if __name__ == "__main__":
    args = parse_arguments()
    apply_changes(args.file, args.description)