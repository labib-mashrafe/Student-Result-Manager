# Student Result Manager

A command-line tool in Python for managing student records: add students, record subject grades, and view each student's average and letter grade. Data is saved to a JSON file, so records persist between sessions.

## Features

- Add students with unique IDs
- Record grades per subject (0–100), with input validation
- Rejects empty or duplicate student IDs and empty names
- Shows each student's grades, average, and letter grade
- Saves all data to `students.json` automatically

## How to Run

Requires Python 3.

```
python student_result_manager.py
```

Data is stored in `students.json` in the same folder. The file is created automatically on first use.

## Letter Grade Scale

| Average | Grade |
|---|---|
| 80 and above | A+ |
| 70 to below 80 | A |
| 60 to below 70 | B |
| 50 to below 60 | C |
| 40 to below 50 | D |
| Below 40 | F |

## Example

```
--- Student Result Manager ---
1. Add student
2. Add grade
3. View student
4. View all students
5. Exit
Enter choice: 2
Enter student ID: 1
Enter subject: Physics
Enter grade (0-100): abc
Please enter a number.
Enter grade (0-100): 150
Grade must be between 0 and 100.
Enter grade (0-100): 70
Grade added for Labib

Enter choice: 3
Enter student ID: 1

Name: Labib
Grades:
  Math: 85
  Physics: 70
  Average: 77.5
  Grade: A
```

## What I Learned

- Validating user input with `try/except`
- Reading and writing data with JSON files
- Structuring a program with functions

## License

MIT
