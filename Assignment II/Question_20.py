"""Write a Python class to find the three elements that sum to zero
from a list of n real numbers.
Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
Output : [[-10, 2, 8], [-7, -3, 10]]"""


class Numbers(object):
    lst = [-25, -10, -7, -3, 2, 4, 8, 10]

    def check_zero(self):
        n = len(self.lst)
        result = []
        for i in range(0, n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if self.lst[i] + self.lst[j] + self.lst[k] == 0:
                        result.append([self.lst[i], self.lst[j], self.lst[k]])

        return result


print(Numbers().check_zero())
