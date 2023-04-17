#!/bin/bash
DOCKER_BUILDKIT=1
PYTHON_VERSION=$1

if [ -z "$PYTHON_VERSION" ]; then
  echo "Please provide a Python version as an argument. For example: ./layer_build.sh 3.7"
  exit 1
fi

docker build --build-arg PYTHON_VERSION=$PYTHON_VERSION -t my-lambda-layer .
docker run --name temp-container my-lambda-layer &
sleep 3
docker cp temp-container:/var/task/python /tmp/python
docker stop temp-container
docker rm temp-container


du -sh /tmp/python
ls -lh /tmp/python | wc -l
zip -r /tmp/python_layer.zip /tmp/python

ls -lh /tmp/python_layer.zip

S3=lambda-artifacts-f87dd42ec0fb11e5
# sam package --output-template-file packaged.yaml --s3-bucket $S3
# sam deploy --template-file packaged.yaml --stack-name my-lambda-layer --capabilities CAPABILITY_IAM

