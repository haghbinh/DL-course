import torch
import torch.nn as nn

# Define a simple model
model = nn.Linear(10, 1)  # Linear model with 10 inputs, 1 output

# Create a random input tensor
x = torch.randn(1, 10)  # A single input of shape (1, 10)

# Without torch.no_grad() (during training)
output = model(x)
print(f"Output (with gradient tracking): {output}")
print(f"Requires Grad: {output.requires_grad}")  # This will be True

# With torch.no_grad() (during evaluation or inference)
with torch.no_grad():
    output_no_grad = model(x)
    print(f"Output (no gradient tracking): {output_no_grad}")
    print(f"Requires Grad: {output_no_grad.requires_grad}")  # This will be False
