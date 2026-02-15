#  Dice Roll Simulator -
#  Generate 100 random dice rolls (1–6) 
#  Count frequency of each number 
#  Calculate probability of rolling 6 
#  Check distribution fairness

import numpy as np

# Generate 100 random dice rolls (1–6) 
rolls = np.random.randint(1,7,100)
print("100 random dice rolls:",rolls)

# Count frequency of each number
one = rolls[rolls == 1].size
two = rolls[rolls == 2].size
three = rolls[rolls == 3].size
four = rolls[rolls == 4].size
five = rolls[rolls == 5].size
six = rolls[rolls == 6].size

print(one, "ones")
print(two, "twos")
print(three, "threes")
print(four, "fours")
print(five, "fives")
print(six, "sixes")

# Calculate probability of rolling 6 
prob_six = rolls[rolls == 6].size / rolls.size*100
print("Probability of rolling a 6:", prob_six, "%")

# Check distribution fairness
expected = rolls.size/6
print("Expected frequency for each number:", expected)
print("1:", one - expected)
print("2:", two - expected)
print("3:", three - expected)
print("4:", four - expected)
print("5:", five - expected)
print("6:", six - expected)

# Fareness decision
tolerance = 5
if (
    abs(one - expected) <= tolerance and
    abs(two - expected) <= tolerance and
    abs(three - expected) <= tolerance and
    abs(four - expected) <= tolerance and
    abs(five - expected) <= tolerance and
    abs(six - expected) <= tolerance
):
    print("The dice distribution is fair.")
else:
    print("The dice distribution is not fair.")