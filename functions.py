import itertools
import interval
import random
from interval import interval , inf , imath
from collections import namedtuple
import matplotlib.pyplot as plt
I_state = namedtuple("I_state","Current_State Action Nature_Action Nature_Observation_Action Actual_State");
Istate_space=list()
Area =list()
Stages =list()

Initial_state_x = interval[-10,10]   #Initialize starting position
Initial_state_y = interval[-10,10]



Current_state_x = Initial_state_x    #set initial state to current state 
Current_state_y = Initial_state_y

Robot_action_space_x = interval[-5,5]
Robot_action_space_y = interval[-5,5]

Nature_observation_action_space_y = interval[-1.5,1.5]
 
Nature_action_space_x = interval[-0.25,0.75];
Nature_action_space_y = interval[-0.75,0.25];

Goal_state_x= interval[-2,2];
Goal_state_y=interval[-2,2];

Flag = 0

def get_pre_image(Current_observation_X,Current_observation_Y):
	if Current_observation_X==0:
		Range_X = Current_observation_Y + Nature_observation_action_space_y
		Range_Y = interval[inf,-inf]
		#print "range_x = "+ str(Range_X)
		#print "range_y = "+ str(Range_Y)
		return (Range_X,Range_Y)
	else:
		Range_Y = Current_observation_Y + Nature_observation_action_space_y
		Range_X = interval[inf,-inf]
		#print "range_x = "+ str(Range_X)
		#print "range_y = "+ str(Range_Y)
		return (Range_X,Range_Y)


def get_corrected_state(Current_state_x,Current_state_y,PreImage_X,PreImage_Y):
		Current_state_x=Current_state_x & PreImage_X
		Current_state_y=Current_state_y & PreImage_Y
		return(Current_state_x,Current_state_y)


def get_new_state(Current_state_x,Current_state_y,Action_space_x,Action_space_y):
		Current_state_x=Current_state_x + Action_space_x + Nature_action_space_x
		Current_state_y=Current_state_y + Action_space_y + Nature_action_space_y
		return(Current_state_x,Current_state_y)


def get_new_state_ndet(Current_state_x,Current_state_y,Action_space_x,Action_space_y,Nature_action_x,Nature_action_y):
		#print "current = "+ str(Current_state_x)
		Current_state_x=Current_state_x + Action_space_x + Nature_action_x
		#print Current_state_x
		Current_state_y=Current_state_y + Action_space_y + Nature_action_y
		#print Current_state_y
		return(Current_state_x,Current_state_y)



def user_interact():
		response=raw_input('Enter "A" to enter a new action,"O" to enter a new observation and any other key to quit: ')
		return(response)


def get_random(Range):
		randomNo = round((random.uniform(Range[0][0],Range[0][1])),2)
		#print randomNo
		return(randomNo)

def calculate_area(Current_state_x,Current_state_y):
		area = (Current_state_x[0][1]-Current_state_x[0][0])*(Current_state_y[0][1]-Current_state_y[0][0])
		Area.append(round(area,3))
		return(Area)

def plot(list_data):
		plt.plot(list_data)
		plt.show()	


def calculate_action_x(Current_state_x):
		if Robot_action_space_x in Current_state_x :
			Action_x=0.1;
		else:	
			if (Current_state_x[0][0] >= Goal_state_x[0][0]):
				if (Current_state_x[0][1] <= Goal_state_x[0][1]):
					Action_x = 0
				else:
					Action_x = Goal_state_x[0][1] - (Current_state_x[0][1] + Nature_action_space_x[0][1])
					if Action_x not in Robot_action_space_x:
						Action_x = Robot_action_space_x[0][0]
			else:
				if (Current_state_x[0][1] <= Goal_state_x[0][1]):
					Action_x = Goal_state_x[0][0] - (Current_state_x[0][0] + Nature_action_space_x[0][0])
					if Action_x not in Robot_action_space_x:
						Action_x = Robot_action_space_x[0][1]

				else:
					if (Current_state_x[0][1] > Goal_state_x[0][1]):
						Action_x = Goal_state_x[0][1] - (Current_state_x[0][1] + Nature_action_space_x[0][1])
						if Action_x not in Robot_action_space_x:
							Action_x = Robot_action_space_x[0][0]
					else :
						Action_x = Goal_state_x[0][0] - (Current_state_x[0][0] + Nature_action_space_x[0][0])
						if Action_x not in Robot_action_space_x:
							Action_x = Robot_action_space_x[0][1]
	
		return(Action_x)


def calculate_action_y(Current_state_x):
		if Robot_action_space_x in Current_state_x :
			Action_x = 0.1
		else:	
			if (Current_state_x[0][0] >= Goal_state_x[0][0]):
				if (Current_state_x[0][1] <= Goal_state_x[0][1]):
					Action_x = 0
				else:
					Action_x = Goal_state_x[0][1] - (Current_state_x[0][1] + Nature_action_space_y[0][1])
					if Action_x not in Robot_action_space_x:
						Action_x = Robot_action_space_x[0][0]
			else:
				if (Current_state_x[0][1] <= Goal_state_x[0][1]):
					Action_x = Goal_state_x[0][0] - (Current_state_x[0][0] + Nature_action_space_y[0][0])
					if Action_x not in Robot_action_space_x:
						Action_x = Robot_action_space_x[0][1]

				else:
					if (Current_state_x[0][1] > Goal_state_x[0][1]):
						Action_x = Goal_state_x[0][1] - (Current_state_x[0][1] + Nature_action_space_y[0][1])
						if Action_x not in Robot_action_space_x:
							Action_x = Robot_action_space_x[0][0]

					else :
						Action_x = Goal_state_x[0][0] - (Current_state_x[0][0] + Nature_action_space_y[0][0])	
						if Action_x not in Robot_action_space_x:
							Action_x = Robot_action_space_x[0][1]

		return(Action_x)

					


def update_Actual_State(Actual_state_x,Actual_state_y,random_action_x,random_action_y,Nature_action_space_x,Nature_action_space_y):
		
		Actual_state_x = Actual_state_x + random_action_x + Nature_action_space_x
		Actual_state_y = Actual_state_y + random_action_y + Nature_action_space_y
		return(Actual_state_x,Actual_state_y)



def calculate_ndet_Istate(Current_state_x,Current_state_y):
		for i in range(0,500):
			if i==0:
				random_action_x=0
				random_action_y=0
				random_nature_action_x=0
				random_nature_action_y=0
				Actual_state_x=0
				Actual_state_y=0
			random_observation_x = random.choice([0,1])
			if random_observation_x == 0:
					random_observation_y = get_random(Nature_observation_action_space_y)
					observation_y = Actual_state_x + random_observation_y
					PreImage_X,PreImage_Y = get_pre_image(random_observation_x,observation_y)
			else:
					random_observation_y = get_random(Nature_observation_action_space_y)
					observation_y = Actual_state_y + random_observation_y
					PreImage_X,PreImage_Y = get_pre_image(random_observation_x,observation_y)
			
			Current_state_x,Current_state_y = get_corrected_state(Current_state_x,Current_state_y,PreImage_X,PreImage_Y)
			Area = calculate_area(interval[Current_state_x],interval[Current_state_y])
			I =I_state((Current_state_x,Current_state_y),(random_action_x,random_action_y),(random_nature_action_x,random_nature_action_y),(random_observation_x,random_observation_y),(Actual_state_x,Actual_state_y))
			Istate_space.append(I)
			random_action_x = get_random(Robot_action_space_x)
			random_action_y = get_random(Robot_action_space_y)
			random_nature_action_x = get_random(Nature_action_space_x)
			random_nature_action_y = get_random(Nature_action_space_y)
			Actual_state_x,Actual_state_y=update_Actual_State(Actual_state_x,Actual_state_y,random_action_x,random_action_y,random_nature_action_x,random_nature_action_y)
			Current_state_x,Current_state_y = get_new_state_ndet(Current_state_x,Current_state_y,random_action_x,random_action_y,Nature_action_space_x,Nature_action_space_y)
		return(Istate_space,Area)



def calculate_ndet_Gstate(Current_state_x,Current_state_y):
		
		for i in range(0,100):
				if i==0:
					random_action_x=0
					random_action_y=0
					random_nature_action_x=0
					random_nature_action_y=0
					Actual_state_x=9.5
					Actual_state_y=9.5
				random_observation_x = random.choice([0,1])
				if random_observation_x == 0:
					random_observation_y = get_random(Nature_observation_action_space_y)
					observation_y = Actual_state_x + random_observation_y
					PreImage_X,PreImage_Y = get_pre_image(random_observation_x,observation_y)
				else:
					random_observation_y = get_random(Nature_observation_action_space_y)
					observation_y = Actual_state_y + random_observation_y
					PreImage_X,PreImage_Y = get_pre_image(random_observation_x,observation_y)
				
				Current_state_x,Current_state_y = get_corrected_state(Current_state_x,Current_state_y,PreImage_X,PreImage_Y)
				I =I_state((Current_state_x,Current_state_y),(random_action_x,random_action_y),(random_nature_action_x,random_nature_action_y),(random_observation_x,random_observation_y),(Actual_state_x,Actual_state_y))
				Istate_space.append(I)
				random_action_x = calculate_action_x(Current_state_x)
				random_action_y = calculate_action_y(Current_state_y)
				random_nature_action_x = get_random(Nature_action_space_x)
				random_nature_action_y = get_random(Nature_action_space_y)
				Actual_state_x,Actual_state_y=update_Actual_State(Actual_state_x,Actual_state_y,random_action_x,random_action_y,random_nature_action_x,random_nature_action_y)
				Current_state_x,Current_state_y = get_new_state_ndet(Current_state_x,Current_state_y,random_action_x,random_action_y,Nature_action_space_x,Nature_action_space_y)
				if random_action_x == 0 and random_action_y == 0:
						break

		
		return(Istate_space)


