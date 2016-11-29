#jioFi  [5,10]
#anvesh [-5,10]
#2F [20,25]
x1,y1=-1.0,-1.0
x2,y2=20.0,3.0
x3,y3=3.0,2.0
x4,y4=5.0,5.0
import matplotlib.pyplot as plt
from sympy import *
i=0
plt.axis([-400,400,-400,400])
plt.xlabel('X_axis')
plt.ylabel('Y_axis')

def match(line,keyword):
	line=line.lstrip()
	length=len(keyword)
	if line[:length] == keyword:
		return line[length:]
	else:
		return None

import math
cells=[]
dict_wifi={}
for i in range(0,20):
	dict_wifi[i]=[]


#RSSI=-10*n*log(d)+A
#A=-35dBm Signal Strength At 1 meter
#n=2.7 Path Loss Exponent

def Distance(RSSI,A,n):
	aux=RSSI-A	
	aux=(-1)*aux
	aux=float(aux)/(10*n)
	x=math.pow(10,aux)
	return x


import subprocess
Process=subprocess.Popen(["iwlist","wlp2s0","scan"],stdout=subprocess.PIPE,universal_newlines=True)
out,err=Process.communicate()
new_l=out.split('\n')
#print new_l

for line in new_l:
	line=line.lstrip()
	line=line.rstrip()
	if line.startswith("Cell"):
		line1=line.split()
	#	print line1[4]
		cells.append(line1[4])		
	if line.startswith("ESSID"):
		line2=line.split(":")
	#	print line2[1]
		cells.append(line2[1])
	if line.startswith("Channel"):
		line3=line.split(":")
	#	print line3[1]
		cells.append(line3[1])	
	if line.startswith("Frequency"):
		line4=line.split(":")
		k=line4[1].split('(')
#		print k[0]
		cells.append(k[0])
	if line.startswith("Quality"):
		line5=line.split()
		#line6=line.split(' ')
		#line5=line.split("=")
		line6=line5[2].split("=")
	#	print line6[1]
		cells.append(line6[1])
#print cells
cells.reverse()
#print cells

c=0
for i in range(0,len(cells)):
	if i%5==0:
		dict_wifi[c].append(cells[i])
		dict_wifi[c].append(cells[i+1])
		dict_wifi[c].append(cells[i+2])
		dict_wifi[c].append(cells[i+3])
		dict_wifi[c].append(cells[i+4])
		dict_wifi[c].append(str(Distance(int(cells[i+1]),-40,2.3)))
		c=c+1

print "S.No",'       ',"SSID",'      ',"RSSI(dBm)",'      ',"Freq",'      ',"Channel",'     ',"MAC",'         ',"Distance(mts)"


for i in dict_wifi.keys():
	if dict_wifi[i]!=[]:
		print i,'   ',
		for j in dict_wifi[i]:
			print j,'    ',
		print '\n'

ln=[]
for h in dict_wifi.values():
	if h!=[]:
		print h,type(h)
		ln.append(float(h[5]))
print ln 

ind=[]
i=0
while(i<3):
	ind.append(ln.index(min(ln)))
	ln[ln.index(min(ln))]=max(ln)+1
	i+=1
print ind
dist=[]
for j in ind:
#	dist.append(float(dict_wifi[j][5])
	print dict_wifi[j][0],float(dict_wifi[j][5])

d1=(x1**2)+(y1**2)-(float(dict_wifi[ind[0]][5])**2)
d2=(x2**2)+(y2**2)-(float(dict_wifi[ind[1]][5])**2)
d3=(x3**2)+(y3**2)-(float(dict_wifi[ind[2]][5])**2)
plt.plot(x1,y1,'ro')
plt.annotate(dict_wifi[ind[0]][0]+'\n'+str(round(float(dict_wifi[ind[0]][5]),2))+'mts',xy=(x1,y1),xycoords='data',xytext=(-30,+40),textcoords='offset points',fontsize=10,arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=.2"))
plt.plot(x2,y2,'ro')
plt.annotate(dict_wifi[ind[1]][0]+'\n'+str(round(float(dict_wifi[ind[1]][5]),2))+'mts',xy=(x2,y2),xycoords='data',xytext=(+30,+40),textcoords='offset points',fontsize=10,arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=.2"))
plt.plot(x3,y3,'ro') 
plt.annotate(dict_wifi[ind[2]][0]+'\n'+str(round(float(dict_wifi[ind[2]][5]),2))+'mts',xy=(x3,y3),xycoords='data',xytext=(+30,-40),textcoords='offset points',fontsize=10,arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=.2"))
#A=2*x*(x2-x1)+2*y*(y2-y1)+d1-d2
#B=2*x*(x3-x1)+2*y*(y3-y1)+d1-d3
x,y=symbols('x,y',real=True)
system=[(2*x*(x2-x1))+(2*y*(y2-y1))+d1-d2,(2*x*(x3-x1))+(2*y*(y3-y1))+d1-d3]
#system=[2*x+3*y-5,3*x+2*y-5]
q={}
q=solve(system,x,y)
x=q[x]
y=q[y]
print x,y
plt.plot(x,y,'bo')
plt.annotate(r'You'+'\n'+'['+str(round(x,2))+','+str(round(y,2))+']',xy=(x,y),xycoords='data',xytext=(+0,-30),textcoords='offset points',fontsize=10,arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=.2"))
plt.show()
