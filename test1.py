import numpy as np
import re
import gymnasium as gym

spaces = {}

spaces["image"] = gym.spaces.Box(0, 255, (64,64) + (3,), dtype=np.uint8)

obs = np.zeros((640,480,3))
obs = np.stack([obs])
print(obs.shape)

k = '$dsadsa'
mlp_keys = ".*"
v = (1,2)
if len(v) in (1, 2) and re.match(mlp_keys, k):
    print ('ok')
    
    
def generate_v():
  """生成满足 len(v) in (1, 2) 的变量 v。

  Returns:
    list: 满足条件的列表 v。
  """
  import random

  # 随机选择长度为 1 或 2
  length = random.choice([1, 2])

  # 根据长度生成列表
  if length == 1:
    v = [random.randint(0, 10)]  # 生成包含一个 0 到 10 之间随机整数的列表
  else:
    v = [random.randint(0, 10), random.randint(0, 10)]  # 生成包含两个 0 到 10 之间随机整数的列表

  return v

# 示例调用
v = generate_v()
print(v)
if len(v) in (1, 2):
    print('ok')
    

value = []
for i in range(1000):
    value.append(np.zeros((64,64,3),dtype=np.float32))
value = np.array(value)
print('value.shape',value )




new_value = np.stack(value, axis=0)  # 将数组沿 axis=0 堆叠

print(new_value.shape)

ab = np.zeros((64,64,3))
ab = np.array(ab)
print(ab)