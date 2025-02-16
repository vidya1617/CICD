#!/bin/bash
docker pull vidya1617/uploaddata:latest
docker stop mycontainer || true
docker rm mycontainer || true
docker run -d --name mycontainer -p 80:5000 vidya1617/uploaddata:latest
