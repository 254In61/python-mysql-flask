#!/usr/bin/bash

function build_docker_image(){
    echo "" && echo "==> Build docker image to use" && echo ""
    docker build -t client-ubuntu-image:latest .

    echo "" && echo "==> Confirm image has been built" && echo ""
    docker images
}

function build_run_containers(){
    echo "" && echo "==> Build containers and test code" && echo ""
    ansible-playbook build-run-container.yml
    
}

function destory_containers(){
    echo "" && echo "==> Destroy the docker containers" && echo ""
    ansible-playbook destroy-container.yml
}

build_docker_image
build_run_containers
destory_containers