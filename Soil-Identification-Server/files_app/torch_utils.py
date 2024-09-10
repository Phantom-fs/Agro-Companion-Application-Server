import torch
import torch.nn as nn
import torchvision.transforms as transforms

from torchvision import models
from torchvision.models import MobileNet_V3_Large_Weights

from PIL import Image
import io

import numpy as np

# ENSEMBLE MODEL AND ITS WILL BE MADE AVAILABLE UPON REQUEST
# EXAMPLE CODE FOR MOBILENET V3 LARGE is provided below

# --------------------------------------------------------------------------------
# CLASS LABELS

class_labels = ['Alluvial Soil', 'Arid Soil', 'Black Soil', 'Laterite Soil', 'Mountain Soil', 'Red Soil', 'Yellow Soil']

# --------------------------------------------------------------------------------
# LOAD MODEL

# Load the model on CPU
model = models.mobilenet_v3_large(weights=MobileNet_V3_Large_Weights.IMAGENET1K_V2)
device = torch.device('cpu')
model.to(device)

# Modify the last linear layer
num_ftrs = model.classifier[3].in_features
model.classifier[3] = nn.Linear(num_ftrs, 7)

# Load the model state dict on CPU
model.load_state_dict(torch.load('files_app/MobileNetV3.pth', map_location=device))

# Set model to evaluation mode
model.eval()

# --------------------------------------------------------------------------------
# PREPROCESS IMAGE

def preprocess(image_bytes):
    # 1 load image
    image = Image.open(io.BytesIO(image_bytes))
    
    image = np.array(image)
    
    image = Image.fromarray(image)
    
    # 11 transform function
    transform = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.ToTensor()
    ])
    
    return transform(image).unsqueeze(0)

# --------------------------------------------------------------------------------
# PREDICT THE SOIL TYPE

def prediction(img_tensor):   
    with torch.no_grad():
        pred = model(img_tensor)
    
    # top 3 predictions and their probabilities
    preds = torch.nn.functional.softmax(pred, dim=1).squeeze().tolist()
    preds = list(zip(class_labels, preds))
    
    # top 3 probabilities
    top3 = sorted(preds, key=lambda x: x[1], reverse=True)[:3]
    
    # top 3 labels
    top3_labels = [x[0] for x in top3]
    
    # top 3 probabilities
    top3 = [x[1] for x in top3]
    
    return top3_labels, top3