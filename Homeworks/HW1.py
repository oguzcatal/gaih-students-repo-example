odd_list=[]
even_list=[]
multiplied_list=[]

for i in range(5):
    x=eval(input('Please enter an odd number: '))
    odd_list.append(x)
    
for j in range(5):
    y=eval(input('Please enter an even number: '))
    even_list.append(y)

merged_list=odd_list + even_list

for k in merged_list:
    multiplied_list.append(k*2)


for a in multiplied_list:
    print(type(a))
