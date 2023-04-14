amt=0
n=0
def large():
  print("Enter number of the L-PIZZA")
  k=int(input())
  n=500*k
  print('Do you need coke,cheese,or icecream')
  ch=int(input('Enter\n 0 for none\n 1 for extra cheese\n 2 for coke\n 3 for icecream\n 4 for coke and icecream and cheese'))
  
  if ch==1:
    print('1 extra cheese is added')
    print('Your Order Number Is \t'+str(ra))
    print('your bill is\n '+str(k)+' l-pizza\n extra cheese\n total==='+str(amt+n+50))
    
  elif ch==2:
    i=int(input('Enter number of cokes'))
    print('Total cackes added are'+str(i))
    print('Your Order Number Is \t'+str(ra))
    print('your bill is\n '+str(k)+' l-pizza\n '+str(i)+' Coke\n total==='+str(amt+n+(i*100)))
    
  elif ch==3:
    j=int(input('Enter number of ICECREAMS'))
    print('Total ICECREAMS added are'+str(j))
    print('Your Order Number Is \t'+str(ra))
    print('your bill is\n '+str(k)+' l-pizza\n '+str(j)+' Icecream\n total==='+str(amt+n+(j*100)))
    
  elif ch==4:
    i=int(input('Enter number of cokes'))
    j=int(input('Enter number of ICECREAMS'))
    print('Total cackes added are'+str(j)+'Total ICECREAMS added are'+str(j))
    print('Your Order Number Is \t'+str(ra))
    print('your bill is\n'+str(k)+' l-pizza\n '+str(i)+'\tCoke\n  '+str(j)+'\tIcecream\n Extra cheese\n total==='+str(amt+n+(j*100)+(i*100)+50))
    
  elif ch==0:
    print('your bill is\n '+str(k)+' l-pizza\n '+str(n))
    
  elif ch>5:
    print('Enter valid choice')
 

#amt=0
def small():
  print("Enter number of the S-PIZZA")
  k=int(input())
  n=250*k
  print('Do you need coke,cheese,or icecream')
  ch=int(input('Enter\n 0 for none\n 1 for extra cheese\n 2 for coke\n 3 for icecream\n 4 for coke and icecream and cheese'))
  if ch==1:
    print('1 extra cheese is added')
    print('Your Order Number Is \t'+str(ra))
    print('your bill is\n '+str(k)+' s-pizza\n extra cheese\n total==='+str(amt+n+50))
  elif ch==2:
    i=int(input('Enter number of cokes'))
    print('Total cackes added are'+str(i))
    print('Your Order Number Is \t'+str(ra))
    print('your bill is\n '+str(k)+' s-pizza\n '+str(i)+' Coke\n total==='+str(amt+n+(i*100)))
  elif ch==3:
    j=int(input('Enter number of ICECREAMS'))
    print('Total ICECREAMS added are'+str(j))
    print('Your Order Number Is \t'+str(ra))
    print('your bill is\n '+str(k)+' s-pizza\n '+str(j)+' Icecream\n total==='+str(amt+n+(j*100)))
  elif ch==4:
    i=int(input('Enter number of cokes'))
    j=int(input('Enter number of ICECREAMS'))
    print('Total cackes added are'+str(j)+'Total ICECREAMS added are'+str(j))
    print('Your Order Number Is \t'+str(ra))
    print('your bill is\n '+str(k)+' s-pizza\n '+str(i)+'\tCoke\n  '+str(j)+'\tIcecream\n Extra cheese\n total==='+str(amt+n+(j*100)+(i*100)+50))
  elif ch==0:
    print('your bill is\n '+str(k)+' s-pizza\n '+str(n))
  elif ch>=5:
    print('Enter valid choice')





#amt=0
def med():
  print("Enter number of the M-PIZZA")
  k=int(input())
  n=350*k
  print('Do you need coke,cheese,or icecream')
  ch=int(input('Enter\n 0 for none\n 1 for extra cheese\n 2 for coke\n 3 for icecream\n 4 for coke and icecream and cheese'))
  if ch==1:
    print('1 extra cheese is added')
    print('Your Order Number Is \t'+str(ra))
    print('your bill is\n '+str(k)+' m-pizza\n extra chees\n total==='+str(amt+n+50))
  elif ch==2:
    i=int(input('Enter number of cokes'))
    print('Total cokes added are'+str(i))
    print('Your Order Number Is \t'+str(ra))
    print('your bill is\n '+str(k)+' m-pizza\n '+str(i)+' Coke\n total==='+str(amt+n+(i*100)))
  elif ch==3:
    j=int(input('Enter number of ICECREAMS'))
    print('Total ICECREAMS added are'+str(j))
    print('Your Order Number Is \t'+str(ra))
    print('your bill is\n '+str(k)+' m-pizza\n '+str(j)+' Icecream\n total==='+str(amt+n+(j*100)))
  elif ch==4:
    i=int(input('Enter number of cokes'))
    j=int(input('Enter number of ICECREAMS'))
    print('Your Order Number Is \t'+str(ra))
    print('Total cokes added are'+str(j)+'Total ICECREAMS added are'+str(j))
    print('your bill is\n '+str(k)+' m-pizza\n '+str(i)+'\tCoke\n  '+str(j)+'\tIcecream\n Extra cheese\n total==='+str(amt+n+(j*100)+(i*100)+50))
  elif ch==0:
    print('your bill is\n '+str(k)+' m-pizza\n '+str(n))
  elif ch>=5:
    print('Enter valid choice')




import random
import datetime
ra=random.randint(1,1000000)

print('Welcome To Dominos')
name=input('\nEnter Your Name')
print(name+'\tplease enter you choice')
ch=int(input('1 .Large Pizza\n 2.Medium Pizza\n 3.Small Pizza\n'))
if ch==1:
  large()
  e=int(input('can you try with small or medium pizza\n if yes press\n 1 for small pizza\n 2 for medium pizza\n if no press 0'))
  if e==0:
   exit()
  elif e==1:
   small()
  elif e==2:
   med()
  else:
   print("Not valid")
  
elif ch==2:
  med()
  e=int(input('can you try with small or medium pizza\n if yes press\n 1 for small piza\n 2 for Large pizza\n if no press 0'))
  if e==0:
   exit()
  elif e==1:
   small()
  elif e==2:
   med()
  else:
   print("Not valid")
elif ch==3:
  small()
  e=int(input('can you try with small or medium pizza\n if yes press\n 1 for Large piza\n 2 for medium pizza\n if no press 0'))
  if e==0:
   exit()
  elif e==1:
   small()
  elif e==2:
   med()
  else:
   print("Not valid")
elif ch>=4:
  print('INVALID')
tra=random.randint(1000000,1000000000)
print('Thank You!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
print('Your Transaction completed\n Through online mode')
#dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
#print("date and time =", dt_string)	

print('YOUR TRANSACTION ID IS======'+str(tra))
print('Thank You!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!..............................................................................................')


