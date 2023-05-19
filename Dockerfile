FROM ccoupe/opencv-cuda:4.6.0-11.7.0-devel-ubuntu

WORKDIR /usr/local/lib/mlshapes/

COPY * /usr/local/lib/mlshapes/
COPY lib/Algo.py lib/
COPY shapes/* shapes/

RUN pip3 install websockets imutils rpyc
    
CMD "/usr/local/lib/mlshapes/mlshapes.sh" 

