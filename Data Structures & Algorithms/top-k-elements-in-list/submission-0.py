class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count ={}

        for n in nums:
            
            if n in count :
                count[n]=count[n]+1
            else:
                count[n]=1 

        freq=sorted(count.items(), key=lambda x: x[1], reverse=True)          

        return [item[0] for item in freq[:k]]