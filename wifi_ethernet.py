#1. Change the ethernet device name in code 
#2. run the code as root
#3. shud change the NET.txt first according to the corrent connection 'E'for ethernet and 'W'for wlan

import os
#cheking for ping
hostname = "google.com"
response = os.system("ping -c 1 " + hostname)
if response == 0:

    print ("NETWORK ACTIVE")
	
else:
	print ("PING NOT AVAILABLE")
	#Reading the current connection
	f = open("NET.txt","r+")
	if f.mode == "r+":
		c = f.readline(1)
		if c =="E":
			#Disabling Ethernet
			os.system('sudo ifconfig enxfcde56ff0106 down')
			#Enabling WIFI
			os.system('rfkill unblock wlan')
			f.seek(0)
			f.truncate(0)
			f.write("W")
			print ("CONNECTING TO WIFI")

		elif c =="W":
			#Disabling WIFI
			os.system('rfkill block wlan')
			#Enabling Ethernet
	    		os.system('sudo ifconfig enxfcde56ff0106 up')
			f.seek(0)
			f.truncate(0)
			f.write("E")
			print ("CONNECTING TO ETHERNET")
		 
