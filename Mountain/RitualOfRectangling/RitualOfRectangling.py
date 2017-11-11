# http://codecombat.com/play/level/ritual-of-rectangling
# <%= we_need_summon %>
# <%= paladin_rect %>
# <%= rect_certain %>
# <%= say_phrase %>
# <%= almost_equal %>
# <%= almost_equal_func %>
def almostEqual(valueA, valueB):
    # <%= check_le_and_ge %>
    pass
    # <%= remove_it %>
    return valueA < valueB * 1.03 and valueA > valueB * 0.97


# <%= rect_perimeter_func %>
def perimeter(side1, side2):
    return (side1 + side2) * 2
    # <%= perimeter_explain %>


# <%= area_perimeter_func %>
def area(side1, side2):
    return side1 * side2
    # <%= area_explain %>


# <%= etalon_values %>
requiredPerimeter = 104
requiredArea = 660

# <%= anchor %>
base = hero.findNearest(hero.findFriends())

while True:
    sideSN = base.distanceTo("Femae")
    sideWE = base.distanceTo("Illumina")
    currentPerimeter = perimeter(sideSN, sideWE)
    currentArea = area(sideSN, sideWE)
    if almostEqual(currentArea, requiredArea) and almostEqual(currentPerimeter, requiredPerimeter):
        hero.say("VENITE!")
        break
