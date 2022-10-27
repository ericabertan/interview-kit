from functools import cmp_to_key

class Checker:
    
    def __init__(self, person1, person2):
        self.person1 = person1
        self.person2 = person2
    
    def check_name(self):
        if self.person1.name < self.person2.name:
            return -1
        elif self.person1.name > self.person2.name:
            return 1
        else:
            return 0

    def check_score(self):
        if self.person1.score < self.person2.score:
            return 1
        elif self.person1.score > self.person2.score:
            return -1
        else:
            return self.check_name()

    def comparator(self):
        return self.check_score()

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def __repr__(self):
        """ Learn how this could be useful and implement it."""
        pass 

    def comparator(a, b):
        checker = Checker(a, b)
        return checker.comparator() 
        
n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)
    
data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)