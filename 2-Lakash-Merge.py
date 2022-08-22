def mergesort(mylist):
    if len(mylist)>1:
        mid = len(mylist)//2
            #print (mid)
        left_list =mylist[:mid]
        right_list = mylist[mid:]
        #function called inside the same function is called the recurssive function
        mergesort(left_list)
        mergesort(right_list)
        i=j=k=0
        while i<len(left_list) and j<len(right_list):
            if left_list[i]<right_list[j]:
                mylist[k]=left_list[i]
                i+=1
                k+=1
            else:
                mylist[k]=right_list[j]
                j+=1
                k+=1
        while i<len(left_list):
            mylist[k]=left_list[i]
            i+=1
            k+=1
        while j<len(right_list):
            mylist[k]=right_list[j]
            j+=1
            k+=1

mylist =[34,33,16,1,3,12,44,56,67]
mergesort (mylist)
print ('sorted list is: ', mylist)

