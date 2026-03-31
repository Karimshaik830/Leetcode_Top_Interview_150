def removeDuplicates(nums):
    i=1
    for j in range(i,len(nums)):
        if nums[j]!=nums[i-1]:
            nums[i]=nums[j]
            i+=1
    return i
nums=[1,1,2]
print(removeDuplicates(nums))