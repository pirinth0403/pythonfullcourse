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
"""Position = 0
end_position = 10
Enemy_position = 8

while Position < end_position:
    Position += 1
    print(Position)
    if Position == Enemy_position:
        print("Game over")
        break

    if Position == end_position:
        print("U reached end of game") """
### FOR LOOP
"""enemy_positions = [5, 10, 15 ,20]

for enemy_position in enemy_positions:
    print(enemy_position)

for i in range(0,5):
    print("Hello")"""

###function
"""position = 100
def move_player(position,amount):
    #global position
    position += amount
    return position

position=move_player(position,-30)
print(position)"""
##inheritance

class GameObject:
    def __init__(self,name,x_position,y_position):
        self.name = name
        self.x_position = x_position
        self.y_position = y_position
    def move(self,by_x_amount,by_y_amount):
        self.x_position += by_x_amount
        self.y_position += by_y_amount
class Enemy (GameObject):
    def __init__(self,name,x_position,y_position,health):
        super().__init__(name,x_position,y_position)
        self.health = health
    def take_damage(self,amount):
        self.health -= amount



game_object = GameObject("Ragulan",10,20)
print(game_object.name)
print(game_object.x_position)
print(game_object.y_position)
enemy = Enemy("printh",20,30,190)
print(enemy.name)
print(enemy.x_position)
print(enemy.y_position)
print(enemy.health)


"""game_object.move(5,10)
game_object.name = "pirinthapan"
print(game_object.name)
print(game_object.x_position)
print(game_object.y_position)"""






