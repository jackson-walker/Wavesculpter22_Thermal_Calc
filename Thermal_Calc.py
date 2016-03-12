import os, sys, math
os.system('cls')	#for Windows
#os.system('clear')	#for Linux/OS X

print "##############################"
print "Controller Loss Calculator by Jackson Walker"
print "Designed specifically for WaveSculptor22 by Tritium"
print "Based on user manual version TRI88.004 ver 2"
print "Not an official program"
print "############################## \n"

#CONSTANTS#
fIntRes = .010800	#internal resistance of motor controller
fLinearSwitch = .0033450	#linear component of switching loss
fConstantSwitch = .018153	#constant component of switching loss
fCapFreq = .00015625	#capacitance*frequency

cRepeat = 'y'
#MAIN#
while(cRepeat != 'n'):
	fVoltage = raw_input("Please input expected voltage of main busline: ")
	fAmps = raw_input("Please input expected amperage of motor controller: ")

	fAmps = float(fAmps)	#when user enters int
	fVoltage = float(fVoltage)

	fMath = fIntRes*math.pow(fAmps,2)+((fLinearSwitch*fAmps+fConstantSwitch)*fVoltage) + (fCapFreq*math.pow(fVoltage,2)) #see user manual for formula
	sOut = ('The expected power loss is: ' + str(fMath) + ' watts.')
	print sOut
	cRepeat = raw_input("Press anything but n to repeat: ")
