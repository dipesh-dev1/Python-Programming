W=int(input('Enter marks of WebTech:'))
P=int(input('Enter marks of Python:'))
M=int(input('Enter marks of Management Information System:'))
R=int(input('Enter marks of Research Methodology:'))
S=int(input('Enter marks of System Analysis and Design:'))
T=(W+P+M+R+S)
print('Total marks is :', T)
if(W>=40 and P>=40 and M>=40 and R>=40 and S>=40):{
print('Pass')}
else:{
print('Fail')}
if T>=400:
    print('Distinction')
elif T>=300:
    print('First Division')
elif T>=200:
    print('Second Division')
elif T>=100:
    print('Third Division')
else:
    print('fail')