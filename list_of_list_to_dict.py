grades = [
    # First line is descriptive header. Subsequent lines hold data
    ['Student', 'Exam 1', 'Exam 2', 'Exam 3'],
    ['Thorny', '100', '90', '80'],
    ['Mac', '88', '99', '111'],
    ['Farva', '45', '56', '67'],
    ['Rabbit', '59', '61', '67'],
    ['Ursula', '73', '79', '83'],
    ['Foster', '89', '97', '101']
]

grade_lists = {}

for y in range (1, len(grades)):
    student_grades = []
    for x in range(1, len(grades[y])):
        student_grades.append(int(grades[y][x]))
    grade_lists[grades[y][0]] = student_grades
