# -*- coding: utf-8 -*-
"""
Created on Fri Feb 01 11:43:11 2019

@author: user
"""
import matplotlib.pyplot as plt
import random
from time import clock
import time
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
    
    lo = 0
    hi = (len(A) - 1)

    
    while lo <= hi and x >= A[lo] and x <= A[hi]:
        
        pos  = lo + int(((float(hi - lo) /
            ( A[hi] - A[lo])) * ( x - A[lo])))

        
        if A[pos] == x:
            return pos

        
        if A[pos] < x:
            lo = pos + 1;

        
        else:
            hi = pos - 1;

    return -1



if __name__ == "__main__":

    for N in range(100000, 2000000, 100000):
            A = [x for x in range(0,N+1)]
            int(random.uniform(0,99999))
            
            A.sort()
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
            A.sort()
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
    print(N_bin,Binary_time)
    plt.plot(N_Value,Linear_Time)
    plt.show()
    plt.plot(N_bin,Binary_time)
    plt.show()
    print(N_inter,interpolation_time)
    plt.plot(N_inter,interpolation_time)
    plt.show()
    
