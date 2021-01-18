from random import randint
def Quickselect(lst,left,right,K):
    if(left==right):
        return(lst[left])
    pos=partition(lst,left,right)
    if(pos==K-1):
        return(lst[pos])
    elif(pos>=K):
        return(Quickselect(lst,left,pos-1,K))
    return(Quickselect(lst,pos+1,right,K))
def partition(lst,left,right):
    pivot=lst[right]
    i=left
    for j in range(left,right):
        if(lst[j]>pivot):
            lst[j],lst[i]=lst[i],lst[j]
            i+=1
    lst[right],lst[i]=lst[i],lst[right]
    return(i)                        
def main():
    lst=[]
    for _ in range(10):
        lst.append(randint(1,100))
    K=int(input())    
    print(Quickselect(lst,0,len(lst)-1,K))    
main()        
