
NAME=$1
PORT=$2
MODE=$3

IMAGE=python-api
sudo docker build -t $IMAGE .
sudo docker stop $NAME && sudo docker rm $NAME
sudo docker run --restart always --name $NAME -e MODE=$MODE -p $PORT:8080 -d $IMAGE