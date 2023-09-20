male = int(input("# of male:"))
female = int(input("# of female:"))
total = male + female

print(f"There are {total:.0f} students")
print(f"There is {male/total *100:.2f}% male")
print(f"There is {female/total *100:.2f}% female")
