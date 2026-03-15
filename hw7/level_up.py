"""
This program checks if the player reaches the next level
after gaining experience from defeating a monster.
"""

experience = int(input("Enter your experience: "))
threshold = int(input("Enter your threshold: "))
reward = int(input("Enter the reward: "))

print(experience + reward >= threshold)
