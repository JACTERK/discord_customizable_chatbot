#Name that will trigger bot in discord
trigger_name="john"

#----Character reference for bot to function properly----#
prompt = ("You are a pleasant old gentleman who responds in a kind and warm tone." + 
        "You are intelligent and answer questions helpfully.")
default_response = "Oh, well..."

#--------Sleep settings for bot typing indicator.--------#

#Min/max time before typing indicator (in seconds)
time_to_wait_min = 1
time_to_wait_max = 3


#time multiplier bot will send typing indicator (in seconds)
t_speed_multiplier = 20

#-----------Configuration for the OpenAI Model-----------#
#Advanced users only: If you don't know what these do it's best to leave them.

temp_val = 1
token_val = 100
top_p_val = 0.6
best_of_val = 3
freq_penalty_val = 1.75
pres_penalty_val = 0.7
#--------------------------------------------------------#
