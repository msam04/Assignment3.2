
# coding: utf-8

# In[47]:


my_string = 'acadgild'
my_list1 = [s.upper() for s in my_string]
print(my_list1)

list2 = ['x', 'y', 'z']
my_list2 = []
for i in range(1,5):
    my_list2.extend([l*i for l in list2])
print(my_list2)

my_list3 = []
powers = [1, 2, 4]
for p in powers:
    my_list3.extend([l*p for l in list2])
print(my_list3)

list4 = [2, 3, 4, 5, 6]
my_list4 = []
for i in range(len(list4)-2):
    temp_list1 = [list4[i]]
    temp_list2 = [list4[i+1]]
    temp_list3 = [list4[i+2]]
    my_list4.append([l for l in temp_list1])
    my_list4.append([l for l in temp_list2])
    my_list4.append([l for l in temp_list3])
    
print(my_list4) 

list5 = [2, 3, 4, 5, 6, 7, 8]
my_list5 = []
for i in range(len(list5)- 3):
    temp_list = [list5[i], list5[i+1], list5[i+2], list5[i+3]]
    my_list5.append([l for l in temp_list])
print(my_list5)

list6 = [1, 2, 3]
my_list6 = []
for i in list6:
    for j in list6:
        temp_set = (i,j)
        my_list6.append(temp_set)
        
print(my_list6)

