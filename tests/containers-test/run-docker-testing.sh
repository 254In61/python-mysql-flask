#!/usr/bin/bash

function build_docker_image(){
    echo "" && echo "==> Build docker image to use" && echo ""
    docker build -t client-ubuntu-image:latest .

    echo "" && echo "==> Confirm image has been built" && echo ""
    docker images
}

function run_ansible(){
    echo "" && echo "==> Run ansible playbook to test the code" && echo ""
    ansible-playbook site.yml
}

build_docker_image
run_ansible