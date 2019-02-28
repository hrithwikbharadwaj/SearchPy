import timeit as t
import random
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
low=1
high=10
a=[]
x=[]
time_m=[]
time_q=[]
time_s=[]
time_b=[]
time_i=[]
time_h=[]

def swap(A, i, j):
	if i!=j :
		A[i], A[j] = A[j], A[i]
def selectionSort(A):
    count1=0
    for i in range(len(A)):

        min_idx = i
        for j in range(i+1, len(A)):
            count1=count1+1
            if A[min_idx] > A[j]:
                min_idx = j


        A[i], A[min_idx] = A[min_idx], A[i]
    return count1

def merge_sort(arr):
    if len(arr) >1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0


        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1


        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1

        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1
def partition(arr,low,high):
    i = ( low-1 )
    pivot = a[low]

    for j in range(low , high):


        if   arr[j] <= pivot:


            i = i+1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )

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
def quick_sort(arr,low,high):
    if low < high:


        pi = partition(arr,low,high)


        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)


def heapify(arr, n, i,):
	largest = i
	l = 2 * i + 1
	r = 2 * i + 2


	if l < n and arr[i] < arr[l]:
		largest = l


	if r < n and arr[largest] < arr[r]:
		largest = r


	if largest != i:
		swap(arr,arr[i],arr[largest])



		heapify(arr, n, largest,)


def heapSort(arr):
	n = len(arr)


	for i in range(n, -1, -1):
		heapify(arr, n, i,)
    for i in range(n-1, 0, -1):
		swap(arr,arr[i],arr[0])

		heapify(arr, i, 0,)


def bubbleSort(arr):
    n = len(arr)
    count2=0

    for i in range(n):


        for j in range(0, n-i-1):


            count2=count2+1
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return count2
if __name__ == "__main__":
    for N in range (1,500,100):
        for i in range(0,N):
            a.append(random.randint(1,100))

        start=t.default_timer()
        merge_sort(a)
        end=t.default_timer()
        print('Merge Sort: \nTime for sorting %d elements is %f' %(len(a),end-start))
        time_m.append(end-start)
        random.shuffle(a)
        start=t.default_timer()
        quick_sort(a,0,len(a)-1)
        end=t.default_timer()
        print('Quick Sort: \nTime for sorting %d elements is %f' %(len(a),end-start))
        time_q.append(end-start)
        random.shuffle(a)
        start=t.default_timer()
        selectionSort(a)
        end=t.default_timer()
        print('Selection Sort: \nTime for sorting %d elements is %f' %(len(a),end-start))
        time_s.append(end-start)
        random.shuffle(a)
        start=t.default_timer()
        bubbleSort(a)
        end=t.default_timer()
        print('Bubble Sort: \nTime for sorting %d elements is %f' %(len(a),end-start))
        time_b.append(end-start)
        random.shuffle(a)
        start=t.default_timer()
        insertionsort(a)
        end=t.default_timer()
        print('Insertion Sort: \nTime for sorting %d elements is %f' %(len(a),end-start))
        time_i.append(end-start)

        random.shuffle(a)
        start=t.default_timer()
        heapSort(a)
        end=t.default_timer()
        print('Insertion Sort: \nTime for sorting %d elements is %f' %(len(a),end-start))
        time_h.append(end-start)

        x.append(N)
    plt.figure(figsize=(10,8))
    plt.plot(x, time_s,'g',label='Selection Sort')
    plt.plot(x, time_b,'y',label='Bubble Sort')
    plt.plot(x, time_m,'r',label='Merge Sort')
    plt.plot(x, time_q,label='Quick Sort')
    plt.plot(x, time_i,label='Insertion Sort')
    plt.plot(x, time_h,label='Heap Sort')
    plt.legend(loc='upper left')
        # naming the x axis
    plt.xlabel('Input')
        # naming the y axis
    plt.ylabel('Time')
    plt.grid()
    plt.scatter(x,time_s)
    plt.scatter(x,time_b)
    plt.scatter(x,time_m)
    plt.scatter(x,time_q)
    plt.scatter(x,time_i)
    plt.scatter(x,time_h)

    plt.title('Sort')

    plt.show()
