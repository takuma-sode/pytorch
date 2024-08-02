import numpy as np

data = np.array([
  [[65, 70], [56, 80], [78, 68], [90, 85], [60, 75]],
  [[70, 75], [54, 88], [82, 64], [88, 83], [58, 78]],
  [[67, 72], [52, 82], [80, 66], [86, 80], [59, 74]]
])

print(data.shape) #データ形状を確認
print(data.mean(axis = 1)) # クラスごと科目別平均点
print(np.max(data[:,2,1])) # 全クラスの番号3番の学生での2科目目の最高得点
print(np.max(np.max(data, axis = 1),axis = 0) - np.min(np.min(data, axis = 1),axis = 0)) #全クラスの各科目の最高得点と最低得点の差
print(np.sum(data[:,:,0]>=80,axis = 1)) #各クラスの1科目目が80点以上の人数
print(np.sum(np.sum(data, axis=2)>135))
print(np.sum((data[:,:,0]-np.mean(data[:,:,0]))*(data[:,:,1]-np.mean(data[:,:,1])))/15 \
      / np.sqrt(np.sum((data[:,:,0]-np.mean(data[:,:,0]))**2)/15)  \
      / np.sqrt(np.sum((data[:,:,1]-np.mean(data[:,:,1]))**2)/15))