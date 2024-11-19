
n = int(input())
elderly = []
non_elderly = []

for i in range(n):
    patient_info = input().strip().split()
    patient_id = patient_info[0]
    age = int(patient_info[1])

    if age >= 60:
        elderly.append((patient_id, age, i))
    else:
        non_elderly.append((patient_id, age, i))


elderly.sort(key=lambda x: (-x[1], x[2]))


non_elderly.sort(key=lambda x: x[2])


for patient in elderly + non_elderly:
    print(patient[0])
