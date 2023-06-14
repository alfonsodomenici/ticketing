#/bin/sh
docker build -t ticketing .
docker rm -f   ticketing
docker run -d --name blog -p5000:5000 ticketing