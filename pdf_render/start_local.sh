if ! [ -f .local ]; then
echo "You need to create .local file from .local.template and fill in your docker registry credentials" && exit
fi

echo ".local exists" && source .local

docker-compose -f docker-compose.yml -f docker-compose.local.yml build

docker-compose -f docker-compose.yml -f docker-compose.local.yml up

