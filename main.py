from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    a=[]
    flag=0
    for i in range(len(nums)):
        for j in range(i+1,len(nums),1):
            if (nums[i]+nums[j])==target:
                a.append(i)
                a.append(j)
                flag=1
                break
        if flag==1:
            break
                
                
    return a


