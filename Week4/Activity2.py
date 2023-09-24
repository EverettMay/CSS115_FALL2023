from collections import namedtuple

student = namedtuple("student", ['name', 'age', 'major', 'GPA'])
first = student('A', 17, 'CS', 4.0)
second = student('B', 18, 'CS', 4.0)
third = student('C', 19, 'CS', 4.0)
print("First student info:", end = ' ')
print(*first, sep=',')
print("Second student info:", end = ' ')
print(*second, sep=',')
print("Thirs student info:", end = ' ')
print(*third, sep=',')

first = student('me', 20, 'CS', 4.0)
print(f"updated student info: {first}")
