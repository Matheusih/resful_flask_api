import torch
import torch.nn as nn
import torchvision.models as models

from .neural_net import NeuralNet
from .cifar10 import trainloader, testloader

def initNeuralNet():
    model=models.vgg16(pretrained=True)
    optimizer = torch.optim.SGD(model.parameters(), lr=0.001, momentum=0.9, weight_decay=5e-4)
    scheduler = torch.optim.lr_scheduler.MultiStepLR(optimizer, milestones=[150,250], gamma=0.1)
    criterion = nn.CrossEntropyLoss()
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    return NeuralNet(model, optimizer, scheduler, criterion, device)

def sampleTrain(neuralNet, epochs=10):
    neuralNet.train(epochs, trainloader, testloader)