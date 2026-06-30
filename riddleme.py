from logic import *

# Propositions
# J = Joker
# R = Riddler
# P = Penguin
# A = Acid Burns
# C = Cards
# B = Deadly Joy Buzzers
# U = Umbrella
# T = Tell-tale clue
# S = Low-level street criminal
# Q = Riddler clues (word games, etc.)
# H = Hole

J, P, R, A, C, B, U, T, S, Q, H = vars('J', 'P', 'R', 'A', 'C', 'B', 'U', 'T', 'S', 'Q', 'H')

# Formulas
f01 = T
f02 = T >> ~S
f03 = T >> (J | R | P)
f04 = J >> (A | C | B)
f05 = R >> Q
f06 = P >> U
f07 = H
f08 = H >> T
f09 = H >> (A | U)
f10 = H >> ~Q

# ArgumentForms
llcriminal = ArgumentForm(f01, f02, f03, f04, f05, f06, f07, f08, f09, f10, conclusion=S)
joker = ArgumentForm(f01, f02, f03, f04, f05, f06, f07, f08, f09, f10, conclusion=J)
penguin = ArgumentForm(f01, f02, f03, f04, f05, f06, f07, f08, f09, f10, conclusion=P)
riddler = ArgumentForm(f01, f02, f03, f04, f05, f06, f07, f08, f09, f10, conclusion=R)

print("Who definitely committed this crime: ")
print("A low-level criminal:", llcriminal.is_valid())
print("The Joker:", joker.is_valid())
print("The Penguin:", penguin.is_valid())
print("The Riddler:", riddler.is_valid())

