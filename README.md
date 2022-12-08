# llm-quine
A LLM that writes itself.

First I asked `chatGPT`:

    Call this file main.py

    ```python
    import os
    import openai
    openai.api_key = os.getenv("OPENAI_API_KEY")
    openai.Edit.create(
    model="text-davinci-edit-001",
    input="What day of the wek is it?",
    instruction="Fix the spelling mistakes"
    )
    ```

    Replace input with the file read text of main.py

    Replace instruction with "Improve yourself"

    Write the output to main.py