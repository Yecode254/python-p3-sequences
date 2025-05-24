my_list = ['mango','banana','apple' ,'orange', 'watermelon' , 'guava' ]
my_list[0]='pear'
my_list.append('pineapple')
my_list.insert(3,'cherry')
my_list.remove('apple')
my_sorted_list=sorted(my_list,key= len)

print(my_list)
print(my_sorted_list)
print(my_list[0])