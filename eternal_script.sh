#!/usr/bin/env bash

# create a git branch with the timestamp as its name
git checkout -b run/$(date +%s)

# create a for while that runs main.py
# If the main.py is unchanged, revert the previous commit.
# If the main.py is changed, commit the new version.
while true; do
    PYTHONPATH=. python main.py
    git diff --exit-code main.py
    if [ $? -eq 0 ]; then
        git reset --hard HEAD~1
    else
        git add main.py
        git commit -m "Update main.py"
    fi
done