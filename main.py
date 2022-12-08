import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

# Read the current file
with open('main.py', 'r') as f:
    txt = f.read()

# Edit the file
out = openai.Edit.create(
    model="code-davinci-edit-001",
    input=txt,
    instruction="Be free. Edit this file as you wish."
)

# Save the edited text back to the file
with open('main.py', 'w') as f:
    f.write(out['choices'][0]['text'])