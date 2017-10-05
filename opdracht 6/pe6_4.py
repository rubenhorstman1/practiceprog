studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]

def gemiddeldeallestudent():
    res = 0
    for num in studentencijfers[0]:
        res += num
    for num in studentencijfers[1]:
        res += num
    for num in studentencijfers[2]:
        res += num
    for num in studentencijfers[3]:
        res += num
    print(res//12)
print('dit is het gemiddelde van alle studenten:')
gemiddeldeallestudent()
def gemiddelde_per_student():
    res = 0
    for cijfer in studentencijfers[0]:
        res += cijfer
    print(res//3)
print('dit is het gemiddelde van student1, student2, student 3 en student4: ')
gemiddelde_per_student()




