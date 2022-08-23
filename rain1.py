import test12
print(test12.__name__)
if __name__ == "__main__":
    rain = input("Is it rainy now?")
    night = input("Is it night now?")
    warm = input("Is it warm now?")
    if (rain == "yes") or (night == "yes") or (warm != "yes"):
        print("Stay home")
    else:
        print("Go for a walk")

# and 10 => 0
# or 0000010 => 1
# not 1 => 0