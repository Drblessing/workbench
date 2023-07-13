import torch
import torchvision.models as models

model = models.resnet18()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
compiled_model = torch.compile(model, backend="aot_eager")

x = torch.randn(16, 3, 224, 224)
optimizer.zero_grad()
out = compiled_model(x)
out.sum().backward()
optimizer.step()
