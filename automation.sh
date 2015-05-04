# this script file will run on misfit-cloud-builder server, don't run on local

# set DOCKER_IMAGE will enable build docker image, and run integration tests on container
export DOCKER_IMAGE="forhot2000/node-hello"

# overwrite docker run command
function docker_run () {
	if [[ "$GIT_BRANCH" = "master" ]]; then
    	CONTAINER_ID=$(docker run -d -e NODE_ENV=production ${DOCKER_IMAGE}${IMAGE_TAG})
	elif [[ "$GIT_BRANCH" = "develop" ]]; then
    	CONTAINER_ID=$(docker run -d -e NODE_ENV=staging ${DOCKER_IMAGE}${IMAGE_TAG})
	fi
}

# overwrite integreation test, this function will executed after docker container run
function integration_test () {
    check_url "http://$CONTAINER_ID:8080/"
}

# overwrite integreation test, this function will executed without docker container
# function integration_test_without_docker () {
#     echo "run integration test without docker..."
# }
