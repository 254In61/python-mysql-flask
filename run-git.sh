#!/usr/bin/bash

function installRequirements(){
   echo "" && echo "==== install python requirements..."
   pip install -r requirements.txt
}

function reformatWithBlack() {
    echo "" && echo "==== reformat code with the uncompromising black..."
    black mymodules/
    black scripts/
}

function linterCheckWithPylint() {
    echo "" && echo "=== Search for drama moments with the pesky pylint"
    pylint mymodules/
    pylint scripts/
    pylint tests/
}

function runGit(){
    echo "" && echo "=== Run git"
    git status
    git add CICD/
    git add Modules/
    git add Scripts/
    git add Tests/
    git add .gitignore
    git add README.md
    git add run-git.sh
    git commit -m "Updates @ $(date)"
    git push
    git status
}

installRequirements
reformatWithBlack
linterCheckWithPylint
runGit
