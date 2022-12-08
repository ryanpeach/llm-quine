#!/usr/bin/env bash

# create a git branch with the timestamp as its name
git checkout -b run/$(date +%s)

# Get the sha of the last commit
sha=$(git rev-parse HEAD)
n_tries=0

# create a for while that runs main.py
# If the main.py is unchanged, revert the previous commit.
# If the main.py is changed, commit the new version.
while true; do
    PYTHONPATH=. python main.py > /dev/null
    git diff --exit-code main.py
    if [ $? -eq 0 ]; then
        # If the current commit is not the first commit,
        # and we have tried 10 times, revert the previous commit.
        if [ $(git rev-parse HEAD) != $sha && $n_tries -eq 10 ]; then
            git reset --hard HEAD~1
            n_tries=0
        else
            n_tries=$((n_tries+1))
        fi
    else
        echo "=========== Found a change ==========="
        cat main.py
        echo "====================================="
        git add main.py
        git commit -m "Update main.py"
    fi
done