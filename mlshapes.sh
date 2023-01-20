#!/usr/bin/env bash
source ~/anaconda3/etc/profile.d/conda.sh
conda activate py3
cd /usr/local/lib/mlshapes/
python3 shape_server.py --port 4439
