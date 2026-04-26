def add(x,y):
  return x+y

print("hello world!")

import torch
import matplotlib.pyplot as plt
def dm01():
    t1 = torch.rand(5,3)
    t2 = torch.sigmoid(t1)
    plt.imshow(t2.numpy())
    plt.show()



if __name__ == '__main__':
    dm01()