"""
This library is not editable by the AI.

Consider it similar to any other imported library.
"""
import difflib
from wasabi import color
from func_timeout import func_timeout
from prompt_toolkit.shortcuts import confirm


def diff_text(a: str, b:str) -> None:
    """
    REF: https://gist.github.com/ines/04b47597eb9d011ade5e77a068389521
    """
    output = []
    matcher = difflib.SequenceMatcher(None, a, b)
    for opcode, a0, a1, b0, b1 in matcher.get_opcodes():
        if opcode == "equal":
            output.append(a[a0:a1])
        elif opcode == "insert":
            output.append(color(b[b0:b1], fg=16, bg="green"))
        elif opcode == "delete":
            output.append(color(a[a0:a1], fg=16, bg="red"))
        elif opcode == "replace":
            output.append(color(b[b0:b1], fg=16, bg="green"))
            output.append(color(a[a0:a1], fg=16, bg="red"))
    print("".join(output))


def evaluate_and_overwrite(txt: str, choices) -> bool:
    """
    Ask the human evaluating the code changes whether or not the changes are allowed.
    If the changes are allowed, run the code.
    If the code runs without error, overwrite the main.py file with the new code.
    """
    for i, choice in enumerate(choices['choices']):
        try:
            print("========= Choice ", i, " ==========")
            diff_text(txt, choice['text'])
            print("===================================")
            answer = confirm("Should this code be ran?")
            if answer:
                func_timeout(10, exec, args=(choice['text'],))
            else:
                continue
        except:
            continue
        else:
            with open('main.py', 'w') as f:
                f.write(choice['text'])
            return True

    return False
