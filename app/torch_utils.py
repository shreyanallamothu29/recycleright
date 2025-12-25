import torch
import torchvision.models as models
import torch.nn as nn
import torchvision.transforms as transforms
from PIL import Image
import io

class ResNet50Classifier(nn.Module):
    def __init__(self, num_classes=10, pretrained=True):
        super().__init__()

        # load ResNet50
        weights = models.ResNet50_Weights.IMAGENET1K_V1 if pretrained else None
        self.backbone = models.resnet50(weights=weights)

        # freeze all layers
        for p in self.backbone.parameters():
            p.requires_grad = False

        # replace final classifier
        in_features = self.backbone.fc.in_features
        self.backbone.fc = nn.Linear(in_features, num_classes)

        # unfreeze classifier
        for p in self.backbone.fc.parameters():
            p.requires_grad = True

        # unfreeze last ResNet block (layer4)
        for p in self.backbone.layer4.parameters():
            p.requires_grad = True

    def forward(self, x):
        return self.backbone(x)

model_0 = ResNet50Classifier(num_classes = 10)
PATH = "test_model.pth"
model_0.load_state_dict(torch.load(PATH))

classes = ['battery', 'biological', 'cardboard', 'clothes', 'glass', 'metal', 'paper', 'plastic', 'shoes', 'trash']

# image -> tensor
def transform_image(image_bytes):
    transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()])

    image = Image.open(io.BytesIO(image_bytes))
    return transform(image).unsqueeze(0)

# predict
def get_prediction(image_tensor):
    model_0.eval()
    with torch.no_grad():
        logits = model_0(image_tensor)
        probs = torch.nn.functional.softmax(logits, dim=1)
        max_idx = int(torch.argmax(probs, dim=1).item())
        return classes[max_idx]