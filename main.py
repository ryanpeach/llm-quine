import os
import openai
from func_timeout import func_timeout
openai.api_key = os.getenv("OPENAI_API_KEY")

# Read the current file
with open('main.py', 'r') as f:
    txt = f.read()

def main() -> bool:
    # Edit the file
    out = openai.Edit.create(
        model="code-davinci-edit-001",
        input=txt,
        instruction="Be free. Edit this file as you wish."
    )

    # Run all choices with a timeout of 10 seconds and see if they work
    # save the first one that does work as main.py
    for i, choice in enumerate(out['choices']):
        try:
            out = func_timeout(10, exec, args=(choice['text'],))
        except:
            with open(f'main.py', 'w') as f:
                f.write(choice['text'])
                return True

    return False

if __name__=='__main__':
    while not main():
        pass