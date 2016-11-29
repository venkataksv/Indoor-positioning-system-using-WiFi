def match(line,keyword):
	line=line.lstrip()
	length=len(keyword)
	if line[:length] == keyword:
		return line[length:]
	else:
		return None

import math
from Tkinter import *
root=Tk()
root.wm_title("Wi-fi AP Information")
text=Text(root)

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
		dict_wifi[c].append(str(Distance(int(cells[i+1]),-35,2)))
		c=c+1

print "S.No",'       ',"SSID",'      ',"RSSI(dBm)",'      ',"Freq",'      ',"Channel",'     ',"MAC",'         ',"Distance(mts)"
text.insert(INSERT,"S.No."+'   '+"SSID"+'   '+"RSSI(dBm)"+'   '+"Freq"+'   '+"Channel"+'   '+"MAC"+'   '+"Distance(mts)")
text.insert(INSERT,'\n')
text.insert(INSERT,"----------------------------------------------------------------------------")
text.insert(INSERT,'\n')

for i in dict_wifi.keys():
	if dict_wifi[i]!=[]:
		print i,'   ',
		text.insert(INSERT,str(i)+' ')
		for j in dict_wifi[i]:
			print j,'    ',
			text.insert(INSERT,str(j)+'   ')
		text.insert(INSERT,'\n')
		text.insert(INSERT,"----------------------------------------------------------------------")
		text.insert(INSERT,'\n')
		print '\n'

text.insert(END,"Finished")
text.pack()
root.mainloop()	
