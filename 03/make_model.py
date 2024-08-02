import torch
from torch.nn import Module

class MyModel(Module):
    
    def __init__(self, arg1: int, arg2: str):
        super().__init__() #継承元の関数を引き継ぐため必須
        self.arg1 = arg1
        self.arg2 = arg2

    def forward(self, x): #forwardで入力から出力までの処理、引数にモデルの入力
        return x

if __name__=="__main__":
    # インスタンス作成
    mymodel = MyModel(arg1=1234, arg2="tus")

    # forward 呼び出し
    _input = torch.ones((2, 3))
    out1 = mymodel(_input)
    out2 = mymodel.forward(_input)
    print("===== method1 ======")
    print(repr(out1))
    print("===== method2 ======")
    print(repr(out2))