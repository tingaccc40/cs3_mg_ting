class Plant:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, zombie):
        print(f"\n{self.name} attacks {zombie.name} for {self.damage} damage!")
        zombie.take_damage(self.damage)

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
           self.health = 0
        print(f"\n{self.name} took {amount} damage! Remaining health: {self.health}")


class Zombie:
    def __init__(self, name, health, damage, distance):
        self.name = name
        self.health = health
        self.damage = damage
        self.distance = distance

    def move(self):
        if self.distance > 0:
            self.distance -= 1
        print(f"\n{self.name} walked 1 step closer... Current distance: {self.distance}")

    def attack(self, plant):
        print(f"\n{self.name} attacks {plant.name} for {self.damage} damage!")
        plant.take_damage(self.damage)

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
        print(f"\n{self.name} took {amount} damage! (Remaining Health: {self.health})")

def run_game():
    plant1 = Plant("Potato", 65, 15)
    plant2 = Plant("Tomato", 70, 10)

    zombie = Zombie("Kaiju", 250, 30, 6)

    plants = {plant1, plant2}

    turn = 1
    
    while True:
        print(f"\nTurn {turn}")

        for plant in plants:
            if plant.health > 0:
                plant.attack(zombie)
            if zombie.health <= 0:
                print(f"\n{zombie.name} is defeated! Plants win.")
                return

        if zombie.distance > 0:
            zombie.move()
        else:
            target = target = next((p for p in plants if p.health > 0), None)
            if target:
                zombie.attack(target)
        
        if all(p.health <= 0 for p in plants):
            print(f"Both plants have been defeated! {zombie.name} WINS!")
            return

        print(f"\nEnd of Turn {turn}")
        for p in plants:
            print(f"{p.name} HP: {p.health}")
        print(f"\n{zombie.name} HP: {zombie.health}")

        turn += 1
if __name__ == "__main__":
    run_game()
        