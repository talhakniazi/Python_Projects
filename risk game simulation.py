import random

class RiskGame:
    def __init__(self, attacker_armies, defender_armies):
        self.attacker_armies = attacker_armies
        self.defender_armies = defender_armies

    def roll_dice(self, num_dice):
        """Simulates rolling dice and returns sorted list of dice in descending order."""
        dice = sorted([random.randint(1, 6) for _ in range(num_dice)], reverse=True)
        return dice

    def battle_round(self):
        # Determine the number of dice for each side
        attacker_dice = min(3, self.attacker_armies - 1)
        defender_dice = min(2, self.defender_armies)

        # Roll dice for both attacker and defender
        attacker_rolls = self.roll_dice(attacker_dice)
        defender_rolls = self.roll_dice(defender_dice)

        # Battle resolution
        print(f"Attacker rolls: {attacker_rolls}")
        print(f"Defender rolls: {defender_rolls}")
        
        # Compare highest dice rolls
        for a, d in zip(attacker_rolls, defender_rolls):
            if a > d:
                self.defender_armies -= 1
                print("Defender loses 1 army")
            else:
                self.attacker_armies -= 1
                print("Attacker loses 1 army")

    def simulate_battle(self):
        """Simulate the battle until one side runs out of armies."""
        print(f"Starting battle: Attacker {self.attacker_armies} armies, Defender {self.defender_armies} armies")
        
        while self.attacker_armies > 1 and self.defender_armies > 0:
            self.battle_round()
            print(f"Current armies - Attacker: {self.attacker_armies}, Defender: {self.defender_armies}")
            print("-" * 30)
        
        # Display outcome
        if self.defender_armies <= 0:
            print("Attacker wins the battle!")
        else:
            print("Defender successfully defends!")

# Run a sample battle simulation
if __name__ == "__main__":
    # Example: Attacker has 10 armies, Defender has 5 armies
    battle = RiskGame(attacker_armies=10, defender_armies=5)
    battle.simulate_battle()
