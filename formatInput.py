import csv

def prepareTeams():
    with open("student_to_mentors_csv.csv", mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        res = ""
        for row in csv_reader:
            res += row["Team Name"] + ": "
            for i in range(1,9):
                temp = "Preference " + str(i)
                if(i == 8):
                    res += row[temp]
                else:
                    res += row[temp] + ", "
            res += "\n"
            line_count += 1
        print("Processed " + str(line_count) + " lines.")

    file = "Teams.txt"
    with open(file, 'w') as f:
        f.write(res)
        f.close()

def prepareMentors():
    with open("mentors_to_students.csv", mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        res = ""
        for row in csv_reader:
            res += row["Full Name (e.g. Ziba Cranmer)"] + ": "
            for i in range(1,9):
                temp = "Preference " + str(i)
                if(i == 8):
                    res += row[temp]
                else:
                    res += row[temp] + ", "
            res += "\n"
            line_count += 1
        print("Processed " + str(line_count) + " lines.")

    file = "Mentors.txt"
    with open(file, 'w') as f:
        f.write(res)
        f.close()
