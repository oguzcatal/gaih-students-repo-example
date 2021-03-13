import pandas as pd
import random

questions=pd.read_csv('source.csv', usecols = [' Question',' Answer'], low_memory = True)

count=0

a=random.randint(0,100000)
print('                                    Welcome to Paying You!                                    \n''')
print('You will be asked 10 questions which you can answer by typing. Your successfulness will be deemed according to your result. Note that your answers must be case sensitive.\n''')
print('Shall we begin?\n''')
print('Here is your first question: {}?'.format(questions[' Question'][a]))
answer1=input('Your anser is: ')

if answer1==questions[' Answer'][a]:
    print('\nYour anser is correct.')
    count+=1
else:
    print('You chose poorly.')

b=random.randint(0,100000)
print('\nQuestion 2: {}?'.format(questions[' Question'][b]))
answer2=input('Your anser is: ')

if answer2==questions[' Answer'][b]:
    print('\nYour anser is correct.')
    count+=1
else:
    print('You chose poorly.')

c=random.randint(0,100000)
print('\nQuestion 3: {}?'.format(questions[' Question'][c]))
answer2=input('Your anser is: ')

if answer2==questions[' Answer'][c]:
    print('\nYour anser is correct.')
    count+=1
else:
    print('You chose poorly.')
    
d=random.randint(0,100000)
print('\nQuestion 4: {}?'.format(questions[' Question'][d]))
answer2=input('Your anser is: ')

if answer2==questions[' Answer'][d]:
    print('\nYour anser is correct.')
    count+=1
else:
    print('You chose poorly.')
    
e=random.randint(0,100000)
print('\nQuestion 5: {}?'.format(questions[' Question'][e]))
answer2=input('Your anser is: ')

if answer2==questions[' Answer'][e]:
    print('\nYour anser is correct.')
    count+=1
else:
    print('You chose poorly.')
    
f=random.randint(0,100000)
print('\nQuestion 6: {}?'.format(questions[' Question'][f]))
answer2=input('Your anser is: ')

if answer2==questions[' Answer'][f]:
    print('\nYour anser is correct.')
    count+=1
else:
    print('You chose poorly.')
    
g=random.randint(0,100000)
print('\nQuestion 7: {}?'.format(questions[' Question'][g]))
answer2=input('Your anser is: ')

if answer2==questions[' Answer'][g]:
    print('\nYour anser is correct.')
    count+=1
else:
    print('You chose poorly.')

h=random.randint(0,100000)
print('\nQuestion 8: {}?'.format(questions[' Question'][h]))
answer2=input('Your anser is: ')

if answer2==questions[' Answer'][h]:
    print('\nYour anser is correct.')
    count+=1
else:
    print('You chose poorly.')
    
i=random.randint(0,100000)
print('\nQuestion 9: {}?'.format(questions[' Question'][i]))
answer2=input('Your anser is: ')

if answer2==questions[' Answer'][i]:
    print('\nYour anser is correct.')
    count+=1
else:
    print('You chose poorly.')

j=random.randint(0,100000)
print('\nQuestion 10: {}?'.format(questions[' Question'][j]))
answer2=input('Your anser is: ')

if answer2==questions[' Answer'][j]:
    print('\nYour anser is correct.')
    count+=1
else:
    print('You chose poorly.')
    
print('\nTHE END!')
print('\nAre you excited about your score?')
print('\nYou correctly answered {} questions.'.format(count))

if count>5:
    print('\nCongratulations! You were successful.')
else:
    print('\nYou are an abysmal failure ...')