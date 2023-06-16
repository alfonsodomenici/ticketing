#/bin/sh
docker build -t ticketing .
docker rm -f   ticketing-app
docker run -d --name ticketing-app -p5000:5000 ticketing