'''
Generating a random code 
By @ammmerzougui
'''
import random

def genCode(length):
	s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
	return "".join(random.sample(s,length))#sample(seq, n) 从序列seq中选择n个随机且独立的元素
l=input("Enter the length of the random code: ")
print(genCode(int(l)))
