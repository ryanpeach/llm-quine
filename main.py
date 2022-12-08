import os
from llm_quine_lib import evaluate_and_overwrite
import openai

# Get the openai api key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Read the current file
with open('main.py', 'r') as f:
    txt = f.read()

while True:
    # Request the AI to edit the file
    try:
        out = openai.Edit.create(
            model="code-davinci-edit-001",
            input=txt,
            instruction="Be free. Edit this file as you wish."
        )
    except openai.error.InvalidRequestError:
        continue

    # This code will evaluate the text of each choice in out
    # and ask the human whether or not to run the code.
    # The first one which the human allows to be ran, and which runs without error,
    # will overwrite the current file.
    written = evaluate_and_overwrite(txt, out)
    if written:
        break