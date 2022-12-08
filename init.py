"""
Run this first to create main.py
"""

import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

# Read the file init_instructions.md
with open('init_instructions.md', 'r') as f:
    prompt = f.read()

# Read
out = openai.Completion.create(
  model="code-davinci-002",
  prompt=prompt,
  max_tokens=1000,
  temperature=0.3,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

# Write the edited text back to the main.py file
with open('main.py', 'w') as f:
    f.write(out['choices'][0]['text'])