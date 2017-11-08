# http://codecombat.com/play/level/slumbering-sample
# <%= last_stop %>
# <%= up_to_you %>
def average(array):
    sum = 0
    len = 0
    for yet in array:
        if yet.type == 'yeti':
            sum = sum + yet.size
            len = len + 1
    return sum / len
    # Initialize a sum variable
    # Iterate over each element
    # Add the element's size to the sum variable
    # Return the sum variable divided by the length of the array


enemies = hero.findEnemies()
hero.say(average(enemies))
# <%= find_yetis %>

# <%= impelemnt_average %>

# <%= say_average %>
