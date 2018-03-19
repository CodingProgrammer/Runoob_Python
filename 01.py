'''
题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。
'''
#myown
from itertools import permutations
for each in permutations('1234', 3):
    print(''.join(each))

#others generator
def f02():
    for i in range(123,433):
        if (set('567890') & set(str(i))==set()) and (len(set(str(i)))==3):
            yield i

for i in f02():
    print(i)