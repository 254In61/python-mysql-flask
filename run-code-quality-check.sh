#!/usr/bin/bash

# function installRequirements(){
#    echo "" && echo "==== install python requirements..."
#    pip install -r requirements.txt
# }

function reformatWithBlack() {
    echo "" && echo "==== reformat code with the uncompromising black..." && echo ""
    black modules/
    black scripts/
}

function linterCheckWithPylint() {
    echo "" && echo "=== Search for drama moments with the pesky pylint" && echo ""
    pylint modules/
    pylint scripts/
    pylint tests/
}

reformatWithBlack
linterCheckWithPylint

