"""
题目:编写一个程序，查找所有此类数字，它们可以被7整除，
但不能是5的倍数(在2000和3200之间(均包括在内))
"""

answer = []
for i in range(2000, 3201):
    if i % 7 == 0:
        if i % 5 != 0:
            answer.append(i)

for i in answer:
    print(i)