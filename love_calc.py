print('Welcome to love calculator.')
your_name = input('enter your name\n').lower()
crush_name = input('enter your crush name\n').lower()
t = your_name and crush_name.count('t')
r = your_name and crush_name.count('r')
u = your_name and crush_name.count('u')
e = your_name and crush_name.count('e')

l = your_name and crush_name.count('l')
o = your_name   and crush_name.count('o')
v= your_name and crush_name.count('v')
e = your_name and crush_name.count('e')
 
true = int(t) + int(r) +int(u) + int(e)
love = int(l) +int(o) + int(v) +int(e)
true_love1 = str(true) + str(love)
true_love = int(true_love1)

if true_love <= 10:
    print(f'Your score is {true_love}.you both go like coke and mentos')
elif true_love <=40 and true_love >=50:
    print(f'Your score is {true-love}. you could be a good couple')
else:
    print(f"your score is {true_love}")