class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        k = 0
        temp = list(flowerbed)
        print(temp)
        for i in range(len(flowerbed)):
            if(k==n):
                break
            if(i==len(flowerbed)-1):
                if(temp[i-1]!=1 and temp[i]!=1):
                    temp[i] = 1
                    k+=1
            elif(i==0):
                if(temp[i+1]!=1 and temp[i]!=1):
                    temp[i] = 1
                    k+=1
            else:
                if(temp[i-1]!=1 and temp[i+1]!=1 and temp[i]!=1):
                    temp[i] = 1
                    k+=1
        print(temp)
        if k == n:
            return True
        else:
            return False