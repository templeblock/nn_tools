import torch
import torch.nn as nn
from torchvision.models import resnet
import pytorch_analyser

"""
resnet 101: 8G MAC
resnet 50: 4G MAC
resnet 18: 1.8G MAC
"""

if __name__ == '__main__':
    resnet18 = resnet.resnet18()
    input_tensor = torch.ones(1, 3, 224, 224)
    blob_dict, tracked_layers = pytorch_analyser.analyse(resnet18, input_tensor)
    pytorch_analyser.save_csv(tracked_layers, '/tmp/analysis.csv')
