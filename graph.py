import random
from time import clock
import time
import matplotlib.pyplot as plt
Linear_Time=[]
N_Value=[]
Binary_time=[]
N_bin=[]
N_inter=[]
interpolation_time=[]



def linearsearch(A):
    print("Enter the number to be searched")
    x=(random.uniform(0,99999))
    for i in range(N):
        if(A[i]==x):
            loc=1
            break
        else:
            loc=0
    if(loc==1):
        print("Element Found")
    else:
        print("Element not found")
def Binary_Search(A,x):
    low=0
    upper=len(A)-1

    while low <= upper:
        mid = (low+upper) //2

        if A[mid]== x:
            return True
        else:
            if A[mid] < x:
                low= mid+1
            else:
                upper=mid-1
    return False

def interpolationSearch(A,x):
    # Find indexs of two corners
    lo = 0
    hi = (len(A) - 1)

    # Since Aay is sorted, an element present
    # in Aay must be in range defined by corner
    while lo <= hi and x >= A[lo] and x <= A[hi]:
        # Probing the position with keeping
        # uniform distribution in mind.
        pos  = lo + int(((float(hi - lo) /
            ( A[hi] - A[lo])) * ( x - A[lo])))

        # Condition of target found
        if A[pos] == x:
            return pos

        # If x is larger, x is in upper part
        if A[pos] < x:
            lo = pos + 1;

        # If x is smaller, x is in lower part
        else:
            hi = pos - 1;

    return -1



if __name__ == "__main__":

    for N in range(10000, 1000000, 50000):
            A = [x for x in range(1,N+1)]
            int(random.uniform(0,99999))
            random.shuffle(A)

            title = "Linear Search"
            start = clock()
            generator = linearsearch(A)
            end= clock()
            time=end-start
            Linear_Time.append(time)
            N_Value.append(N)
            start = clock()
            print("Enter the number to be searched")
            x=int(random.uniform(0,99999))

            Bin_result=Binary_Search(A,x)
            if Binary_Search(A,x):
                print("Found")
            else:
                print("Not Found")
            end= clock()
            time2=end-start
            N_bin.append(N)
            Binary_time.append(time2)
            start = clock()
            interpolation_Result=interpolationSearch(A,x)
            end = clock()
            time3=end-start
            N_inter.append(N)
            interpolation_time.append(time3)
    plt.plot(N_Value,Linear_Time)
    plt.show()
    plt.plot(N_bin,Binary_time)
    plt.show()
    plt.plot(N_inter,interpolation_time)
    plt.show()
