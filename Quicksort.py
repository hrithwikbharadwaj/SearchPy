import matplotlib.pyplot as plt
import random
from time import clock
import time
Nvalue=[]
A=[]
Quicktime=[]

def swap(A, i, j):
	if i!=j :
		A[i], A[j] = A[j], A[i]

def partition(arr,low,high):
    i = ( low-1 )
    pivot = arr[high]

    for j in range(low , high):

        if   arr[j] <= pivot:

            i = i+1
            swap(arr,i,j)

    swap(arr,i+1,high)
    return ( i+1 )


def quickSort(arr,low,high):
    if low < high:


        pi = partition(arr,low,high)


        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
if __name__ == "__main__":

	for N in range(100000, 500000, 100000):
		for _ in range(N): A.append(int(random.uniform(0,999)))

		random.shuffle(A)
		start = clock()
		quikcy=quickSort(A,0,N-1)
		end= clock()
		time=end-start
		Quicktime.append(time)
		Nvalue.append(N)
		print("working..\n")

	print("\n")

	plt.plot(Nvalue,Quicktime)
	plt.xlabel(" N value")
	plt.ylabel("time in (S)")
	plt.title("Quick Sort")
	plt.show()
