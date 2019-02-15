import matplotlib.pyplot as plt
import random
from time import clock
import time
Nvalue=[]
A=[]
HeapTime=[]

def swap(A, i, j):
	if i!=j :
		A[i], A[j] = A[j], A[i]
def heapify(arr, n, i):
	largest = i
	l = 2 * i + 1
	r = 2 * i + 2


	if l < n and arr[i] < arr[l]:
		largest = l


	if r < n and arr[largest] < arr[r]:
		largest = r


	if largest != i:
		swap(arr,arr[i],arr[largest])


		heapify(arr, n, largest)


def heapSort(arr):
	n = len(arr)


	for i in range(n, -1, -1):
		heapify(arr, n, i)


	for i in range(n-1, 0, -1):
		swap(arr,arr[i],arr[0])
		heapify(arr, i, 0)

if __name__ == "__main__":

	for N in range(100000, 500000, 100000):
		for _ in range(N): A.append(int(random.uniform(0,999)))

		random.shuffle(A)
		start = clock()
		hp=heapSort(A)
		end= clock()
		time=end-start
		HeapTime.append(time)
		Nvalue.append(N)
		print("working..\n")

	print("\n")

	plt.plot(Nvalue,HeapTime)
	plt.xlabel(" N value")
	plt.ylabel("time in (S)")
	plt.title("Heap Sort")
	plt.show()
