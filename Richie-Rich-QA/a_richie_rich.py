#!/bin/python

import sys

n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
number = raw_input().strip()
def comp(n,k,number):
    if n == 0 or n!=len(number):
        print '-1'
        return
    dif = []
    x = [1]
    y = x
    x.append(2)
    for i in xrange(len(number)/2):
        if number[i] != number[len(number)-1-i]:
            dif.append((i,len(number)-1-i))
    if len(dif)>k:
        print -1
        return
    ar = []
    for char in number:
        ar.append(char)
    if len(dif)==k:
        for b,e in dif:
            ar[b] = ar[e] = str(max(int(ar[b]),int(ar[e])))
    if len(dif)< k:
        ex = k - len(dif)
        i = 0
        while i<n/2 and ex>0:
            b = i
            e = n-1-i
            if ar[b]!=ar[e] :
                if  ar[b]!='9' and ar[e]!='9':
                    ar[b] = ar[e] = '9'
                    ex-=1

            else:
                if  ar[b] !='9' and ex>1:
                    ar[b] = ar[e] = '9'
                    ex-=2
            i+=1
        if ex>0 and n%2!=0:
            ar[n/2] = '9'
        for b,e in dif:
            ar[b] = ar[e] = str(max(int(ar[b]),int(ar[e])))

    a = ""
    for char in ar:
        a +=char
    print a
    
comp(n,k,number)