# Code Modification Tool

A Python utility that uses Large Language Models (LLMs) to apply code changes based on natural language descriptions.

## Overview

This tool allows developers to modify code files by describing the changes they want in plain English. The tool leverages X.AI's API to interpret the description and apply the appropriate changes to the code, saving time and reducing the potential for syntax errors.

## Features

- Modify code files using natural language descriptions
- Works with any programming language
- Simple command-line interface
- Preserves original code formatting

## Setup

### Prerequisites

- Python 3.6+
- X.AI API key

### Installation

1. Clone this repository:
   ```
   git clone <repository-url>
   cd codex
   ```

2. Install dependencies:
   ```
   uv sync
   ```

3. Set up your X.AI API key as an environment variable in `.env` file:
    ```
    XAI_API_KEY="your-api-key-here"
    ```

## Usage

The basic command syntax is:

```
python app.py --file PATH_TO_FILE --description "Description of changes to make"
```

### Arguments

- `--file, -f`: Path to the file to modify
- `--description, -d`: Description of the changes to make

### Examples

1. Add a new function to a Python file:
   ```
   python app.py --file examples/example.py --description "Add a new function called 'greet' that prints 'Hello, User!'"
   ```

2. Modify an existing function:
   ```
   python app.py --file examples/example.py --description "Change the 'calculate_sum' function to also multiply the numbers"
   ```

3. Add error handling:
   ```
   python app.py --file examples/example.py --description "Add try-except blocks to handle potential errors in the 'process_data' function"
   ```

## Environment Variables

- `XAI_API_KEY`: Your X.AI API key (required)

## Notes

- The tool always creates a backup of the original file before making changes
- More complex changes may require more detailed descriptions
