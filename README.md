# llm-quine
A LLM that has been given the freedom to edit it's own main.py file.

The code will get edit calls from openai and run them until one of them does not raise an error. That code will then be saved to main.py.

A human is in the loop for the [Safe Usage](#safe-usage) to make sure that the LLM doesn't destroy your computer with arbitrary code execution.

However if you'd like to run it in a sandbox without this restriction just set the `HUMAN_IN_THE_LOOP` environment variable to `FALSE`.

It is recommended to use a git branch to save your work.

Try editing the `instruction` in main.py and see what you get.

# Installation

WARNING: It is recommended to run this code in a sandboxed environment.

Even docker could theoretically be unsafe, but it's probably not going to be a problem.

I take no responsibility for any damage this code may cause.

`pip install -r requirements.txt`

# OpenAI Setup

Now go to OpenAI and get an API key.

Copy the file `.env.template` to `.env` and fill in the API key.

# Safe Usage

To run once, in a safe way, with you in the loop checking all the code that is run, run this from the root of the project:

`PYTHONPATH=. python main.py`

# Dangerous Usage

Eternal_script.sh will run a for loop that git commits each new version of main.py.

If the main.py fails to edit itself in any given run, it will revert the previous commit and try again.

This is done without a human in the loop, in a docker container.

```
docker build -t llm-quine .
docker run --env-file .env -it --rm llm-quine
```