from random import randint
def Quickselect(lst,left,right,K):
    if(left==right):
        return(lst[left])
    split=partition(lst,left,right)
    length=split-left+1
    if(length==K):
        return(lst[split])
    elif(K<length):
        return(Quickselect(lst,left,split-1,K))  
    else:
        return(Quickselect(lst,split+1,right,K-length))          
def partition(lst,left,right):
    pivot=left
    leftMark=left+1
    rightMark=right
    while(True):
        while(leftMark<right and lst[leftMark]<pivot):
            leftMark+=1
        while(rightMark>left and lst[rightMark]>pivot):
            rightMark-=1
        if(leftMark>rightMark):
            break
        else:
            lst[leftMark],lst[rightMark] = lst[rightMark],lst[leftMark]
    lst[left],lst[rightMark] =lst[left],lst[rightMark] 
    return(rightMark)                   
def main():
    lst=[]
    for _ in range(10):
        lst.append(randint(1,100)) 
    K=int(input())    
    print(Quickselect(lst,0,len(lst)-1,K)) 
main()    