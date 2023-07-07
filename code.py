# cisco_telnet
#This program is for a beginner who need to telnet cisco device using python telnet library.

############### Welcome to Netminion Solutions#####################
import getpass import telnetlib

#Telnet Lib is understanding BYTE Strings (ascii)

device = "150.1.1.3" #change the IP with your LAB IP user = input ("Enter your username: ") password = getpass.getpass() #user is putting the password

tn = telnetlib.Telnet(device)

tn.read_until(b"Username: ") tn.write(user.encode('ascii') + b"\n") #Cisco> tn.read_until(b"Password: ") tn.write(password.encode('ascii') + b"\n") #Cisco>

print ("Telnet successful to the device!")

tn.write(b"conf ter\n") 
tn.write(b"int loop 0 \n") 
tn.write(b"ip address 1.1.1.11 255.255.255.255 \n") 
tn.write(b"no shut\n") 
tn.write(b"description Using Python\n") 
tn.write(b"end\n") 
tn.write(b"exit\n")

print ("Commands are pushed – below is the detail :") 
print(tn.read_all().decode('ascii')) #byte string to the string 
print ("Thanks for using Netminion Python Script\n")
