import random

class Character:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        
    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
            
    def deal_damage(self, target):
        damage = max(self.attack - target.defense, 0)
        return damage
    
class Player(Character):
    def __init__(self, name, health = 100, attack = 10, defense = 5):
        super().__init__(name, health, attack, defense)
        
    def choose_action(self):
        print("\nWhat will you do?")
        print("1. Attack \n2. Heal \n3. Run")
        action = input("Choose an action (1/2/3): ")
        return action
    
class Enemy(Character):
    def __init__(self, name, health, attack, defense):
        super().__init__(name, health, attack, defense)
        
def battle(player, enemy):
    while player.is_alive() and enemy.is_alive():
        action = player.choose_action()
        
        if action == '1':
            damage = player.deal_damage(enemy)
            print(f'You attacked {enemy.name} for {damage} damage.')
            enemy.take_damage(damage)
            
        elif action == '2':
            heal = random.randint(10, 20)
            print(f'You healed yourself for {heal} health!')
            player.health += heal
            
        elif action == '3':
            print("\nYou tried to run away.")
            run_chance = random.randint(1, 2)
            if run_chance == '1':
                print("You successfully escaped.")
            if run_chance == '2':
                print("You failed to escaped and died.")
        
        else:
            print("\nInvalid choice! Try again.")
            continue
        
        if enemy.is_alive():
            damage = enemy.deal_damage(player)
            print(f'{enemy.name} attacked you for {damage} damage')
            player.take_damage(damage)
        else:
            print(f"You defeated {enemy.name}.")
            return False
        
        print(f'Your health: {player.health}')
        print(f'{enemy.name} health: {enemy.health}')
    
    return not player.is_alive()

def game():
    print("Welcome to text based RPG!\n")
    name = input("Enter your character's name: ")
    player = Player(name)
    
    enemies = [
        Enemy('Goblin', 30, 5 ,1),
        Enemy("Orc", 50, 8, 3),
        Enemy("Dragon", 100, 12, 5)
    ]
    
    print("\nYour adventure begins!")
    for enemy in enemies:
        print(f'A Wild {enemy.name} appears!')
        if battle(player, enemy):
            print("You successfully escaped the battle!")
            break
        if player.is_alive():
            print(f'You are Victorious! Moving on to the next enemy...')
        else:
            print("You have been defeated! Game Over")
            break
    if player.is_alive():
        print("Congratulations!You defeated all the enemies and won the game!")
        
if __name__ == "__main__":
    game()
            
    
        
    