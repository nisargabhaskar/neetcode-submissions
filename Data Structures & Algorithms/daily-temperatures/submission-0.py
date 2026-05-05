class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)):
            count = 0
            flag = 0
            for j in range(i+1,len(temperatures)):
                if temperatures[i]<temperatures[j]:
                    count += 1
                    flag = 1
                    break
                count +=1
            count = 0 if flag == 0 else count
            res.append(count) 
        return res