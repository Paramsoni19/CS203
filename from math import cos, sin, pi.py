from math import cos, sin, pi
import matplotlib.pyplot as plt
from math import sqrt
from itertools import combinations
from random import randbytes, uniform, seed, random,randint


win_time=0
r=1
N = 1000

first_theta=[]
second_theta=[]
distance=[]

tri_1st_point   = [r*cos(pi/2), r*sin(pi/2)]
tri_2nd_point = [r*cos(pi/2-(2*pi)/3), r*sin(pi/2-(2*pi)/3)]
len_side_of_tri =sqrt( (float(tri_1st_point[0]) - float(tri_2nd_point[0]))**2  + (float(tri_1st_point[1]) -float(tri_2nd_point[1]))**2  )


for n in range(0 , 1000):#random points & distance
   first_theta.append(uniform(0, 2*pi))
   second_theta.append(uniform(0, 2*pi))
   D=sqrt( (r*sin(first_theta[n])-r*sin(second_theta[n]))**2  + (r*cos(first_theta[n])-r*cos(second_theta[n]))**2 )
   distance.append(D)

#draw circle
circle = plt.Circle((0, 0), 1, color='blue', fill=False, linewidth=2, zorder=10)
plt.gca().add_artist(circle)
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)


for i in range(N):#drawing lines and caculating prabability
    if distance[i] > len_side_of_tri:
        color = 'red'
        win_time=win_time+1
    else:
        color = 'green'
    first_point= (r*cos(first_theta[i]), r*sin(first_theta[i]))
    second_point=(r*cos(second_theta[i]), r*sin(second_theta[i]))
    plt.plot(*zip(first_point, second_point), color = color, zorder=randint(1, 2), linewidth=1)

plt.show()
print("probability is  " + str(win_time/N))
