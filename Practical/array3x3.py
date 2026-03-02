import numpy as np

nums = list(map(int, input().split()))
arr = np.array(nums).reshape(3,3)
print(arr)