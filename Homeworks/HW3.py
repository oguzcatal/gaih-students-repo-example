q = eval(input('Please enter first student\'s midterm grade: '))
w = eval(input('Please enter first student\'s project grade: '))
e = eval(input('Please enter first student\'s final grade: '))
r = eval(input('Please enter second student\'s midterm grade: '))
t = eval(input('Please enter second student\'s project grade: '))
y = eval(input('Please enter second student\'s final grade: '))
u = eval(input('Please enter third student\'s midterm grade: '))
o = eval(input('Please enter third student\'s project grade: '))
p = eval(input('Please enter third student\'s final grade: '))
a = eval(input('Please enter fourth student\'s midterm grade: '))
s = eval(input('Please enter fourth student\'s project grade: '))
d = eval(input('Please enter fourth student\'s final grade: '))
f = eval(input('Please enter fifth student\'s midterm grade: '))
g = eval(input('Please enter fifth student\'s project grade: '))
h = eval(input('Please enter fifth student\'s final grade: '))


student1 = {'Midterm grade':q, 'Project grade':w, 'Final grade':e}
student2 = {'Midterm grade':r, 'Project grade':t, 'Final grade':y}
student3 = {'Midterm grade':u, 'Project grade':o, 'Final grade':p}
student4 = {'Midterm grade':a, 'Project grade':s, 'Final grade':d}
student5 = {'Midterm grade':f, 'Project grade':g, 'Final grade':h}


def passingGrade(midterm, project, final):
    return midterm*0.3 + project*0.3 + final*0.4

grade_1 = passingGrade(student1['Midterm grade'], student1['Project grade'], student1['Final grade'])
grade_2 = passingGrade(student2['Midterm grade'], student2['Project grade'], student2['Final grade'])
grade_3 = passingGrade(student3['Midterm grade'], student3['Project grade'], student3['Final grade'])
grade_4 = passingGrade(student4['Midterm grade'], student4['Project grade'], student4['Final grade'])
grade_5 = passingGrade(student5['Midterm grade'], student5['Project grade'], student5['Final grade'])

final_list=[grade_1, grade_2, grade_3, grade_4, grade_5]

print(sorted(final_list)[::-1])