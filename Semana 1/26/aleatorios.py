import random

dado = random.randint(1, 20)
if dado == 20:
    print("Nat 20 let's fucking go")
elif dado == 1:
    print("Nat 1 GET FUCKKKED")
else:
    print(f"Sacaste un {dado}")