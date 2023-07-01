"""
Given the names and grades for each student in a class of  students, store them in a nested list 
and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically 
and print each name on a new line.


Input Format:
------------
The first line contains an integer, , the number of students.
The 2N subsequent lines describe each student over  lines.
- The first line contains a student's name.
- The second line contains their grade.

Constraints:
------------
2 <= N <= 5
There will always be one or more students having the second lowest grade.


Output:
------------
Print the name(s) of any student(s) having the second lowest grade in
If there are multiple students, order their names alphabetically and print each one on a new line,
"""

if __name__ == '__main__':

    students_grades = []
    # receive the data as inputs and store each student students list and grade
    for _ in range(int(input())):
        name = input()
        grade = float(input())
        students_grades.append([name, grade])
    
    # create a new *set* of each students sorted grades
    sorted_grades = sorted(list({i[1] for i in students_grades}))
    second_lowest_grade = sorted_grades[1]

    # create a list for the lowest students because it can be *multiple*
    # iterate over each student and check if the grade matches, if so append the name
    lowest_students = []

    for student in students_grades:
        if second_lowest_grade == student[1]:
            lowest_students.append(student[0])

    # print the students with the lowest grades in alphabetical order
    for student in sorted(lowest_students):
        print(student)