class ClubMembers:
    def __init__(self, name, birthday, age, favorite_food, goal):
        self.name = name
        self.birthday = birthday
        self.age = age
        self.favorite_food = favorite_food
        self.goal = goal

    def display1(self):
        print("Name: ", self.name)
        print("Birthday: ", self.birthday)
        print("Age: ", self.age)
        print("Favorite Food: ", self.favorite_food)
        print("Goal: ", self.goal)

class ClubOfficers(ClubMembers):
    def __init__(self, name, birthday, age, favorite_food, goal, position):
        self.position = position
        ClubMembers.__init__(self, name, birthday, age, favorite_food, goal)

    def display2(self):
        print("Name: ", self.name)
        print("Birthday: ", self.birthday)
        print("Age: ", self.age)
        print("Favorite Food: ", self.favorite_food)
        print("Goal: ", self.goal)
        print("Position: ",self.position)

m_1 = ClubMembers("Tom", "January 16", 16, "Ice Cream", "To Be Happy")
o_2 = ClubOfficers("Vera", "June 22", 16, "Beef Stroganoff", "To Be The World's greatest chef", "Treasure")

m_1.display1()
o_2.display2()