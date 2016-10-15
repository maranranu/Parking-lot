from collections import OrderedDict
from tabulate import tabulate

f = open('/home/kamnee.maran/Videos/parking-lot/parking_input.txt', 'r');
data = f.read().split("\n")

length = int(data[0][-1])
print "Created a parking lot with",length, "slots"

occupy=[]

for i in range(1,length+1):
	occupy.append(i)

count = 1
vehicle = []
color=[]
slot=[]
dictionary = OrderedDict()

def allocate(occupy,count):
	if (count <= length):
		veh = i.split(" ")
		vehicle.insert(count-1,veh[1])
		color.insert(count-1,veh[2])
		slot.insert(count-1,count)
		#dict[veh[1]] = veh[2]
		occupy.remove(count)
	else:
	   print "Sorry, parking lot is full"
	return [OrderedDict(zip(vehicle, color)),occupy]

def deallocate(dictionary,occupy, count):
	if (count <= length):
		occupy.insert(0,count+1)
		vehicle.remove(vehicle[count])
		color.remove(color[count])
		slot.remove(slot[count])
		#del dict[dictionary.keys()[int(i.split(" ")[1]) - 1]]
	return [OrderedDict(zip(vehicle, color)), occupy]	

for i in data:
	ct = 0
	if (i.split(" ")[0] == "park"):
		#print "calling allocate function"
		if (len(occupy) != 0):
			count = occupy[ct]
			allocate(occupy,count)
			print "Allocate Slot number: ",count
		else:
			print "Sorry, parking lot is full"
		
	if (i.split(" ")[0] == "leave"):
		deallocate(dict, occupy, int(i.split(" ")[1])-1)
		count = int(i.split(" ")[1])
		print "Slot number ",count, "is free"
		
	if (i.split(" ")[0] == "status"):
		dic = OrderedDict(zip(vehicle, color))
		table = []
		for index, key in enumerate(dic):
			table.append([slot[index],key,dic[key]])
		print tabulate(table,headers=["Slot No.", "Registration No", "Colour"])

	if (i.split(" ")[0] == "slot_number_for_registration_number"):
		dic = OrderedDict(zip(vehicle, color))
		if (i.split(" ")[1] in dic.keys() != -1):
			print slot[(dic.keys()).index(i.split(" ")[1])]
                else:
			print "Not found"
	if (i.split(" ")[0] == "slot_numbers_for_cars_with_colour"):
		slot_no=""
		indices = [index for index, x in enumerate(color) if x == i.split(" ")[1]]
		for s in indices:
			slot_no =  slot_no + str(slot[s])+","
		print slot_no[:-1]
	if (i.split(" ")[0] == "registration_numbers_for_cars_with_colour"):
		vehicle_no=""
		indices = [index for index, x in enumerate(color) if x == i.split(" ")[1]]
		for s in indices:
			vehicle_no = vehicle_no + str(vehicle[s])+","
		print vehicle_no[:-1]
