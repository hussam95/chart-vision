import torch
import torch.nn as nn
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image

# Create an instance of the model
model = models.resnet18(weights='ResNet18_Weights.DEFAULT')
num_ftrs = model.fc.in_features
model.fc = nn.Linear(num_ftrs, 7)

# Load the state dictionary located at the root of the project
model.load_state_dict(torch.load('..\model_newplusold_data.pth'))

# Define the transform to apply to the input image
test_transforms = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])
    
def predict_image(image_path):
    # Load the input image and apply the transform to it
    image = Image.open(image_path).convert('RGB')
    image_tensor = test_transforms(image)
    image_tensor = image_tensor.unsqueeze(0) # add batch dimension

    # Predict the label of the input image
    model.eval()
    with torch.no_grad():
        output = model(image_tensor)
        probabilities = torch.nn.functional.softmax(output, dim=1)
        _, predicted = torch.max(probabilities, 1)

    # Get the predicted label as a string
    chart_patterns = ['Breakout Pattern', 'DB', 'DT', 'FF',
                      'TR', 'Wedge Bottom', 'Wedge Top']
    prediction = chart_patterns[predicted.item()]

    return prediction
