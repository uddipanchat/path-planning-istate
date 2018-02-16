import itertools
import interval
from interval import interval
from interval import inf
from functions import get_pre_image
from functions import get_corrected_state
from functions import get_new_state
from functions import user_interact
from functions import *

response= user_interact()
while(response is 'A' or response is 'O' or response is 'a' or response is 'o'): 
	if(response is 'O' or response is 'o'):
		X =input('Enter the x coordinate for the observation function: ')
		Y =input('Enter the y coordinate for the observation function: ') 

		PreImage_X,PreImage_Y=get_pre_image(X,Y)   #Calculate preimage for any observation 
		Current_state_x,Current_state_y=get_corrected_state(Current_state_x,Current_state_y,PreImage_X,PreImage_Y)  #calculte correcrted pose from preimage
		print(Current_state_x,Current_state_y)
		response=user_interact()
	
	if(response is'A' or response is 'a'):
		Action_space_x =input('Enter the x coordinate for the action space function: ')
		Action_space_y = input('Enter the y coordinate for the action space function: ')

		Current_state_x,Current_state_y=get_new_state(Current_state_x,Current_state_y,Action_space_x,Action_space_y)
		print(Current_state_x,Current_state_y)
		response=user_interact()