import functions
from functions import *
Istate_space,Area=calculate_ndet_Istate(Current_state_x,Current_state_y)
for item in Istate_space:
	print "At Stage-"+ str(Istate_space.index(item))+" the I-state:"  
	print item 
	print "\n"
print "The maximum area of the I-state is:"+str(max(Area))
print "The minimum area if the I-state is:"+str(min(Area))
Max=Istate_space[Area.index(max(Area))]
Min=Istate_space[Area.index(min(Area))]
Max_Area_x= Max[0][0]
Max_Area_y=Max[0][1]
Min_Area_x= Min[0][0]
Min_Area_y=Min[0][1]
print "The co-ordinates of the maximum area I-state is :(" +str(Max_Area_x[0][0]) +"," +str(Max_Area_y[0][0])+ "),("+str(Max_Area_x[0][0])+","+str(Max_Area_y[0][1])+"),("+str(Max_Area_x[0][1])+","+str(Max_Area_y[0][0])+"),("+str(Max_Area_x[0][1])+","+str(Max_Area_y[0][1])+")"
print "The co-ordinates of the minimum area I-state is :(" +str(Min_Area_x[0][0]) +"," +str(Min_Area_y[0][0])+ "),("+str(Min_Area_x[0][0])+","+str(Min_Area_y[0][1])+"),("+str(Min_Area_x[0][1])+","+str(Min_Area_y[0][0])+"),("+str(Min_Area_x[0][1])+","+str(Min_Area_y[0][1])+")"
plot(Area)

