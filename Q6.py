import functions
from functions import *
for i in range(0,1000):
	Istate_space=calculate_ndet_Gstate(Current_state_x,Current_state_y)
	Stages.append(len(Istate_space))
	del Istate_space[:]
#for item in Istate_space:
	#print item
print "The average no of stages to reach the goal:"+str(sum(Stages)/len(Stages))
print "The maximum no of stages to reach the goal:"+str(max(Stages))
print "Thd minimum no of stages to reach the goal:"+str(min(Stages))