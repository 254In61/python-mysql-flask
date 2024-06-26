#!/usr/bin/bash

# function installRequirements(){
#    echo "" && echo "==== install python requirements..."
#    pip install -r requirements.txt
# }

function runGit(){
    echo "" && echo "=== Run git"
    git status
    git add modules/
    git add scripts/
    git add tests/
    git add .gitignore
    git add README.md
    git add run-*
    git add requirements.txt
    git commit -m "Updates @ $(date)"
    git push
    git status
}

runGit
