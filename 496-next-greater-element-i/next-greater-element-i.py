class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def find(x):
            i=nums2.index(x)
            while True:
                if x<nums2[i+1]:
                    return nums2[i+1]
                else:
                    i+=1
        l=[]
        for i in nums1:
            k=nums2[nums2.index(i)+1::]
            if k==[]:
                l.append(-1)
            elif i<max(k):
                l.append(find(i))
            else:
                l.append(-1)
        return l

        