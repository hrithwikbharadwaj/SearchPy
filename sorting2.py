import matplotlib.pyplot as plt
import random
from time import clock
import time
Selsort=[]
Nvalue=[]
bn=[]
btime=[]
isort=[]
itime=[]
def swap(A, i, j):
	if i!=j :
		A[i], A[j] = A[j], A[i]


def selectionsort(A):
	n = len(A)
	for i in range(n-1):
		minval = A[i]
		minid = i
		for j in range(i+1,n):
			if A[j] < minval:
				minval = A[j]
				minid = j
			yield A
		swap(A, i, minid)
		yield A


def bubblesort(A):
	n = len(A)
	flag = 1
	for i in range(n-1):
		if not flag:
			break;
		flag = 0
		for j in range(n-i-1):
			if A[j] > A[j+1]:
				swap(A, j, j+1)
				flag = 1
			yield A

def insertionsort(A):
	n = len(A)
	for i in range(1,n):
		val = A[i]
		j = i-1
		while j>=0 and A[j] > val:
			swap(A, j, j+1)
			j -= 1
		A[j+1] = val
		yield A

if __name__ == "__main__":
	for N in range(1000000, 9900000, 1000000):
		A = [x for x in range(0,N+1)]
		int(random.uniform(0,99999))
		start = clock()
		sssort=selectionsort(A)
		end= clock()
		time=end-start
		Selsort.append(time)
		Nvalue.append(N)
		random.shuffle(A)
		start = clock()

		bsort=bubblesort(A)
		end= clock()
		time2=end-start
		btime.append(time2)
		bn.append(N)
		random.shuffle(A)
		start = clock()
		iisort=insertionsort(A)
		end= clock()
		time3=end-start
		itime.append(time3)
		isort.append(N)
		print("Working...\n")
		print("Thanks for using Hrithwik's Sorting xD \n")
	print(Nvalue)
	print("\n")
	print(Selsort)
	plt.plot(Nvalue,Selsort)
	plt.show()
	plt.plot(bn,btime)
	plt.show()
	print(bn)
	print("\n")
	print(btime)
	plt.plot(isort,itime)
	plt.show()
	print(isort)
	print("\n")
	print(itime)
