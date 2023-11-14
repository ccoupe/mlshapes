Mlshapes 

```
Use nvidia-docker on Stoic.
$ docker build -t ccoupe/mlshapes .

$ docker run -dp 4439:4439 --name=mlshapes -e TZ=America/Boise ccoupe/mlshapes
```