!git clone https://github.com/ultralytics/yolov5  # clone
%cd yolov5
%pip install -qr requirements.txt  # install

import torch
import utils
display = utils.notebook_init() 

!unzip -q ../train_data.zip -d ../

#!python detect.py --weights yolov5s.pt --img 640 --conf 0.25 --source data/images
#display.Image(filename='runs/detect/exp/zidane.jpg', width=600)
!python detect.py --weights runs/train/exp2/weights/last.pt --img 640 --conf 0.25 --source ../test_images/

# Train YOLOv5s
!python train.py --img 640 --batch 2 --epochs 60 --data custom_data.yaml --weights yolov5s.pt --cache

# !python detect.py --weights runs/train/exp/weights/last.pt  --img 640 --conf 0.25 --source ../clothes_test.mp4
# change weights and source to your own data.
