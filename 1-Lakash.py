#insetion sort
a = [58,45,67,14,56,78,34,1,50,20,55] #mylist
#applying for loop gives range from 1 to len of array (array starts from 0 so we take range from 1)
for i in range(1,len(a)):
        key= a[i] #key = a[i],45 current value
        #print (key)(cur_elemnt) unsorted
        position = i
        while key<a[position-1] and position>0:
            a[position] = a[position-1]
            position = position -1
        a[position] = key #condition dose not match


print(a)



             

        

        

