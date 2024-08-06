import torch
from torch import nn

if __name__=="__main__":

    # 入力のテンソル
    _in = torch.ones((32,1024))

    # linear 32 * 256
    fc1 = nn.Linear(in_features = 1024, out_features = 256, bias = True)
    print(repr(fc1(_in).size()))

    # linear 32 * 2048
    fc2 = nn.Linear(in_features = 1024, out_features=2048, bias=True)
    print(repr(fc2(_in).size()))

    out = fc1(_in)
    print(repr(out.view(-1,16,16).size()))