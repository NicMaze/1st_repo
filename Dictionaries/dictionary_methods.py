# game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notications", "achievements"]
#
# # Use the game_properties list and dict.fromkeys() to generate a dictionary with all values set to 0.  Save the result to a variabled called initial_game_state
# initial_game_state = dict.fromkeys(game_properties, 0)
# print(initial_game_state)
#
# initial_game_state.pop("number_of_lives")
# print(initial_game_state)


inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1}
# Make a copy of inventory and save it to a variable called stock_list USE A DICTIONARY METHOD
stock_list = inventory.copy()

# add the value 18 to stock_list under the key "cookie"
stock_list['cookie'] = 18

# remove 'cake' from stock_list USE A DICTIONARY METHOD
stock_list.pop('cake')

print(stock_list)