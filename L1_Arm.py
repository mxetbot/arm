import time, math
import getopt, sys
import rcpy  # This automatically initizalizes the robotics cape
import rcpy.servo as servo
import rcpy.clock as clock	# For PWM period for servos

# INITIALIZE DEFAULT VARS
duty = 1.5		# Duty cycle (-1.5,1.5 is the typical range)
period = 0.02 	# recommended servo period: 20ms (this is the interval of commands)
ch1 = 1			# select channel (1 thru 8 are available)
ch2 = 2			# selection of 0 performs output on all channels
ch3 = 3
ch4 = 4
ch5 = 5
ch6 = 6

rcpy.set_state(rcpy.RUNNING) # set state to rcpy.RUNNING
srvo1 = servo.Servo(ch1)	# Create servo object
srvo2 = servo.Servo(ch2)
srvo3 = servo.Servo(ch3)
srvo4 = servo.Servo(ch4)
srvo5 = servo.Servo(ch5)
srvo6 = servo.Servo(ch6)
clck1 = clock.Clock(srvo1, period)	# Set PWM period for servos
clck2 = clock.Clock(srvo2, period)
clck3 = clock.Clock(srvo3, period)
clck4 = clock.Clock(srvo4, period)
clck5 = clock.Clock(srvo5, period)
clck6 = clock.Clock(srvo6, period)

servo.enable()		# Enables 6v rail on beaglebone blue
clck1.start()		# Starts PWM
clck2.start()
clck3.start()
clck4.start()
clck5.start()
clck6.start()

def move1(angle):
	srvo1.set(angle)
	
def move2(angle):
	srvo2.set(angle)
	
def move3(angle):
	srvo3.set(angle)

def move4(angle):
	srvo4.set(angle)

def move5(angle):
	srvo5.set(angle)

def move6(angle):
	srvo6.set(angle)
	
	
def arm():	

	move6(-1.5)#open 
	time.sleep(2)
	move1(1.5) #turns left
	time.sleep(3)
	move2(1.1) #down
	time.sleep(1)
	move6(-1.5)#open 
	time.sleep(2)
	move6(1.5)#close 
	time.sleep(2)
	move2(-.2) #up
	time.sleep(2)
	move1(-.5) #turns right
	time.sleep(2)
	move1(-.7) #turns right
	time.sleep(2)
	move1(-1.5) #turns right
	time.sleep(2)
arm()
