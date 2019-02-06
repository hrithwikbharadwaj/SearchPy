import matplotlib.pyplot as plt
import random
from time import clock
import time
Selsort=[]
Nvalue=[]

btime=[]

itime=[]
mergetime=[]

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
def merge(left,right):
    result = []
    i,j = 0, 0
    while i<len(left) and j< len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    result += left[i:]
    result += right[j:]
    return result


def mergeSort(lst):
    if(len(lst) <= 1):
        return lst
    mid = int(len(lst)/2)
    left = mergeSort(lst[:mid])
    right = mergeSort(lst[mid:])
    return merge(left,right)

if __name__ == "__main__":
	count2=1
	for N in range(1000000, 9900000, 1000000):
		A = [x for x in range(0,N+1)]
		int(random.uniform(0,99999))
		random.shuffle(A)
		start = clock()
		sssort=selectionsort(A)
		end= clock()
		time=end-start
		Selsort.append(time)
		Nvalue.append(N)
		print("Selection Sort Done\n")
		random.shuffle(A)
		print("Array Shuffled")
		start = clock()

		bsort=bubblesort(A)
		end= clock()
		time2=end-start
		btime.append(time2)
		print("Bubble Sort Done\n")

		random.shuffle(A)
		print("Array Shuffled")
		start = clock()
		iisort=insertionsort(A)
		end= clock()
		time3=end-start
		itime.append(time3)
		print("Insertion Sort Done\n")
		random.shuffle(A)
		print("Array Shuffled")
		start = clock()
		merges=mergeSort(A)
		end= clock()
		time4=end-start
		mergetime.append(time4)
		print("Merge Sort Done\n")

		print("Working...\n")
		print("Thanks for using Hrithwik's Sorting xD \nCount=",count2)
		count2+=1
	print(Nvalue)
	print("\n")
	print(Selsort)
	plt.plot(Nvalue,Selsort)
	plt.title("Selection Sort")
	plt.xlabel(" N value  (from 10lkhs)")
	plt.ylabel("time in (S)")
	plt.show()

	plt.plot(Nvalue,btime)
	plt.xlabel(" N value  (from 10lkhs)")
	plt.ylabel("time in (S)")
	plt.title("Bubble Sort")
	plt.show()

	print("\n")
	print(btime)
	plt.plot(Nvalue,itime)
	plt.xlabel(" N value  (from 10lkhs)")
	plt.ylabel("time in (S)")
	plt.title("Insertion Sort")
	plt.show()

	print("\n")
	print(itime)
	plt.plot(Nvalue,mergetime)
	plt.xlabel(" N value  (from 10lkhs)")
	plt.ylabel("time in (S)")
	plt.title("Merge Sort")
	plt.show()

	print("\n")
	print(mergetime)
