class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ansSet = []
        d = {}
        for i in range(len(nums)):
            d[i] = nums[i]
        
            
        print('dictionary--',d)
        for firstnum in (nums):
            print('firstnum', firstnum, nums.index(firstnum))
            st = nums.index(firstnum)
            lst2 = nums[(st+1):]
            for secondnum in (lst2):
                print('second  num..', secondnum)
                if firstnum + secondnum == target:
                    ansSet.append([nums.index(firstnum), d.index(secondnum)])
                    return ansSet
                    
# lst = [2, 7, 11, 5]
# tgt = 9
lst = [0,4,3,0]
tgt = 0
# lst = raw_input('enter the list')
problem = Solution()
print(problem.twoSum(lst, tgt))


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lst =[]
        for i,v in enumerate(nums):
            print('i and v:', i,v)
            k = i+1
           
            for j in range(k, len(nums)):
                if v+nums[j] == target:
                    print('v: ',v,'i:',i,'j:',j)
                    lst.append(i)
                    lst.append(j)
                  
        print('lst:',lst)
        return lst

       