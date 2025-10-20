"""
high_score = ("NIMISH" , 120)
print(high_score)

high_score = ("HOLLY" , 150)
print(high_score)

name = high_score[0]
print(name)

print(len(high_score))

print("HOLLY" in high_score)

print(name[0])
print(name[0:2])
print("HOL" in name)
print(len(name)) """
from dis import Positions

"""# DICTIONARIES
actions = {"r":1, "l":-1}
print(actions) """

# IF CONDITIONS
"""KEY = "L"
if KEY == "R":
    print("move right")
elif KEY == "L":
    print("move left")
else:
    print("invalid key") """

# WHILE LOOP
Position = 0
end_position = 10
Enemy_position = 8

while Position < end_position:
    Position += 1
    print(Position)
    if Position == Enemy_position:
        print("Game over")
        break

    if Position == end_position:
        print("U reached end of game")