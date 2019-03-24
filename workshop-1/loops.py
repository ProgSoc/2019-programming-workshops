# loops - for, while

# infinite loop... be careful!
while hungry is True:
    print("Om nom nom...")

# this loop will stop after the first print
while hungry is True:
    print("Eating some pizza...")
    hungry = False

for laps in range(10):
    print("Running 10 laps... Lap number", (laps+1))
