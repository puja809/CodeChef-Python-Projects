import time

print("You have 10 seconds to think...")
for i in range(10,0,-1):
    print(f"\rTime left: {i} seconds ", end="")
    time.sleep(1)
print('\nTime\'s up!')