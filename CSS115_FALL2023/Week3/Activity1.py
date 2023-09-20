midterm = int(input("Enter your midterm exam score:"))
final = int(input("Enter your final exam score:"))
total = midterm*0.3 + final*0.7
print(f"Midterm weight 30% = {midterm*0.3:.1f} points")
print(f"Final is 70% = {final*0.7:.1f} points")
print(f"Total final:{total:.1f} points")
