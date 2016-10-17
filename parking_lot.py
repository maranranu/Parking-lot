"""
Import required modules
"""
from collections import OrderedDict
from tabulate import tabulate
import sys

#take file name from console
file_name = sys.argv[1]

#read file and read it line by line  
f = open(file_name, 'r');
data = f.read().split("\n")

#calculate no of lines in file
length = int(data[0][-1])
print "Created a parking lot with",length, "slots"

#Array to find out whcih slot is free and which one is occupied
occupy=[]

for i in range(1,length+1):
	occupy.append(i)

#Define variables
count = 1
vehicle = []
color=[]
slot=[]
dictionary = OrderedDict()

#function for allocation of vehicle
def allocate(occupy,count):
	#check whether parking lot has capacity or not
	if (count <= length):
		veh = i.split(" ")
		#push vehicle no, color, slot no and remove particular slot no from occupy list
		vehicle.insert(count-1,veh[1])
		color.insert(count-1,veh[2])
		slot.insert(count-1,count)
		occupy.remove(count)
	else:
	   #if parking slot is full
	   print "Sorry, parking lot is full"
	return [OrderedDict(zip(vehicle, color)),occupy]

#function for free particular vehicle
def deallocate(dictionary,occupy, count):
	if (count <= length):
		#Push that slot into occupy list and remove that vehicleno, color and slot from individual list
		occupy.insert(0,count+1)
		vehicle.remove(vehicle[count])
		color.remove(color[count])
		slot.remove(slot[count])
		#del dict[dictionary.keys()[int(i.split(" ")[1]) - 1]]
	return [OrderedDict(zip(vehicle, color)), occupy]	

#traverse into file, check for allocation, deallocation and status
for i in data:
	ct = 0
	#for allocation of vehicle
	if (i.split(" ")[0] == "park"):
		#print "calling allocate function"
		if (len(occupy) != 0):
			count = occupy[ct]
			allocate(occupy,count)
			print "Allocate Slot number: ",count
		else:
			print "Sorry, parking lot is full"
	#for deallocation of vehicle
	if (i.split(" ")[0] == "leave"):
		if (int(i.split(" ")[1]) < length and int(i.split(" ")[1]) < len(vehicle)):
			deallocate(dict, occupy, int(i.split(" ")[1])-1)
			count = int(i.split(" ")[1])
			print "Slot number ",count, "is free"
		else:
			print "Not found"
	#to check status of parking lot in tabular format
	if (i.split(" ")[0] == "status"):
		dic = OrderedDict(zip(vehicle, color))
		table = []
		for index, key in enumerate(dic):
			table.append([slot[index],key,dic[key]])
		print tabulate(table,headers=["Slot No.", "Registration No", "Colour"])
	#find out slot no for particular vehicleno
	if (i.split(" ")[0] == "slot_number_for_registration_number"):
		dic = OrderedDict(zip(vehicle, color))
		if (i.split(" ")[1] in dic.keys() != -1):
			print slot[(dic.keys()).index(i.split(" ")[1])]
                else:
			print "Not found"
	#find slot nos for particular color
	if (i.split(" ")[0] == "slot_numbers_for_cars_with_colour"):
		slot_no=""
		indices = [index for index, x in enumerate(color) if x == i.split(" ")[1]]
		for s in indices:
			slot_no =  slot_no + str(slot[s])+","
		print slot_no[:-1]
	#find registration nos for particular color
	if (i.split(" ")[0] == "registration_numbers_for_cars_with_colour"):
		vehicle_no=""
		indices = [index for index, x in enumerate(color) if x == i.split(" ")[1]]
		for s in indices:
			vehicle_no = vehicle_no + str(vehicle[s])+","
		print vehicle_no[:-1]
