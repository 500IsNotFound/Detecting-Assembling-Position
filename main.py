import os
from Classification.eval import predict

os.system(f"python yolov5/detect.py --weights yolov5/runs/train/exp/weights/best.pt --category {predict('Classification/datasets/test/', 'Classification/weights/weight.h5')}")