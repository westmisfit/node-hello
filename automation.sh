# this script file will run on misfit-cloud-builder server, don't run on local

# set DOCKER_IMAGE will enable build docker image, and run integration tests on container
export DOCKER_IMAGE="forhot2000/node-hello"
# set DOCKER_PUSH false will ignore docker push
# export DOCKER_PUSH="false"

# overwrite docker run command
function docker_run () {
    if [[ "$GIT_BRANCH" = "master" ]]; then
        docker run -d -e NODE_ENV=production ${DOCKER_IMAGE}:${IMAGE_TAG}
    elif [[ "$GIT_BRANCH" = "develop" ]]; then
        docker run -d -e NODE_ENV=staging ${DOCKER_IMAGE}:${IMAGE_TAG}
    fi
}

# overwrite integreation test, this function will executed after docker container run
function integration_test () {
    check_url "http://${CONTAINER_IP}:8080/"
}
