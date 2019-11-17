import torch
import torch.nn as nn


import torchvision
import torchvision.transforms as transforms
import torchvision.models as models

class NeuralNet():
    def __init__(self, model, optimizer, scheduler, criterion, device):
        self.model = model.to(device)
        self.optimizer = optimizer
        self.scheduler = scheduler
        self.criterion = criterion.to(device)
        self.device = device

    def __call__(self, data):
        self.model.eval()
        return self.model(data)

    def learn(self, X, y):
        self.model.train()

        output = self.model(X)
        loss = self.criterion(output,y)

        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()
        self.scheduler.step()
        return loss, output

    def train(self, epochs, trainloader, testloader):
        self.model.train()
        acc_per_epoch = []
        for epoch in range(epochs):
            correct = 0
            total = 0
            ave_loss = 0
            for batch_idx, (x,target) in enumerate(trainloader):
                x = x.to(self.device)
                target = target.to(self.device)
                loss, output = self.learn(x, target)
                total += target.size(0)
                ave_loss = ave_loss * 0.9 + loss.item() * 0.1
                _, predicted = torch.max(output.data, 1)
                correct += (predicted == target).sum().item()
                if(batch_idx+1) % trainloader.batch_size == 0 or (batch_idx+1) == len(trainloader):
                    accuracy = 100 * correct / total
                    print('==>>> epoch: {}, batch index: {}, train loss {:.6f}, accuracy: {}'.format(epoch,batch_idx+1,ave_loss,accuracy))
            test_acc = self.validate(testloader)
            acc_per_epoch.append((accuracy,test_acc))
            print('Epoch', epoch, 'train_acc', accuracy, 'test_acc', test_acc)

    def validate(self, testloader):
        self.model.eval()
        correct = 0
        total = 0
        with torch.no_grad():
            for data in testloader:
                images, labels = data
                images = images.to(self.device)
                labels = labels.to(self.device)
                outputs = self.model(images)
                _, predicted = torch.max(outputs.data, 1)
                total += labels.size(0)
                correct += (predicted == labels).sum().item()
        print('Accuracy of the network on the test images: %d %%' % (100 * correct / total))
        return 100 * correct / total
