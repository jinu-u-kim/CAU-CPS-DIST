import random

total_students = 30
total_teams = 6

students = range(30)

list_students = list(students)

random.shuffle(list_students)

print(list_students)

project_team = []
for i in range(6):
    num_of_members = int(total_students/total_teams)
    index = i * num_of_members
    project_team.append(list_students[index:index+num_of_members])

for i in project_team:
    print(i)


