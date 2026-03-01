# Student Record Management System

A Python-based command-line interface (CLI) application for managing student records with comprehensive CRUD operations, score tracking, and course management.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Data Structure](#data-structure)
- [API Reference](#api-reference)
- [Examples](#examples)
- [Notes](#notes)

---

## Overview

The Student Record Management System is a lightweight CLI application that stores student information in memory using Python dictionaries. It provides a complete set of tools for managing student records including personal details, academic scores, course enrollments, seating arrangements, and graduation status.

---

## Features

### Core Functionality
- ✅ Create new student records with unique IDs
- 📖 View detailed student information with calculated averages
- ✏️ Update existing student records
- 🗑️ Delete student records from the system

### Score Management
- ➕ Add individual scores (0-100 range validation)
- ➖ Remove scores by index
- 📊 Automatic average calculation

### Course Management
- 📚 Enroll students in courses
- 🚫 Remove courses by index
- 📋 Track course enrollment

---

## Installation

1. Clone the repository or download the source code:
```bash
git clone https://github.com/yourusername/student-record-system.git
cd student-record-system
```

2. Ensure you have Python 3.8 or higher installed:
```bash
python --version
```

3. No additional dependencies required - uses only Python standard library.

---

## Usage

Run the application from the command line:

```bash
python student_management.py
```

### Main Menu Options

| Option | Description |
|--------|-------------|
| `1` | Create a new student record |
| `2` | View an existing student's details |
| `3` | Update student information |
| `4` | Delete a student record |
| `5` | Add or remove courses |
| `6` | Add or remove scores |
| `0` | Exit the application |

---

## Data Structure

Each student record is stored as a dictionary with the following structure:

```python
{
    "STU001": {
        "name": "John Doe",           # str: Student's full name
        "age": 20,                    # int: Student's age
        "scores": [85, 90, 78],       # List[float]: Academic scores
        "courses": ["Python", "Math"], # List[str]: Enrolled courses
        "seat": (4, 7),               # Tuple[int, int]: (row, seat_number)
        "graduated": False            # bool: Graduation status
    }
}
```

---

## API Reference

### Helper Functions

| Function | Description |
|----------|-------------|
| `avg(scores)` | Calculates the average of a list of scores, rounded to 2 decimal places |
| `student_exists(student_id)` | Returns `True` if the student ID exists in the system |
| `format_student(student_id)` | Returns a formatted string with all student details |

### CRUD Operations

| Function | Parameters | Description |
|----------|------------|-------------|
| `create_student(student_id, name, age, seat)` | `id: str`, `name: str`, `age: int`, `seat: Tuple[int, int]` | Creates a new student record |
| `read_student(student_id)` | `student_id: str` | Displays formatted student information |
| `update_student(student_id, name, age, seat, graduated)` | `id: str`, optional fields | Updates specified student fields |
| `delete_student(student_id)` | `student_id: str` | Removes the student from the system |

### Score & Course Management

| Function | Parameters | Description |
|----------|------------|-------------|
| `add_score(student_id, score)` | `student_id: str`, `score: int (0-100)` | Adds a score and displays updated average |
| `remove_score(student_id, index)` | `student_id: str`, `index: int` | Removes score at specified index |
| `add_course(student_id, course)` | `student_id: str`, `course: str` | Enrolls student in a course |
| `remove_course(student_id, index)` | `student_id: str`, `index: int` | Removes course at specified index |

---

## Examples

### Creating a New Student

```
=====Students System=====
1) Create student
2) Read student
3) Update student
4) Delete student
5) Add course or Remove course
6) Add score or Remove score
0) Exit

Select an option: 1
ID: STU003
name: Alice Johnson
Age: 21
Row: 5
seat_no: 12

Student with id STU003 has been successfully created
```

### Viewing Student Details

```
Select an option: 2
ID: STU001

Id: STU001
Name: Job
Age: 20
Scores: [55, 66, 77] | Avg: 66.0
Seat: Row: 4, Seat: 7
Courses: ['python', 'DataSci', 'DataEng']
Graduated: False
```

### Adding a Score

```
Select an option: 6
ID: STU001
a. Add score b. Remove score: a
Score (0-100): 88

Score has been added successfully and the new average is 71.5
```

### Adding a Course

```
Select an option: 5
ID: STU002
a. Add Course b. Remove course: a
Name of new course: Machine Learning

Machine Learning has been added successfully
```

---

## Notes

- **Unique IDs**: Student IDs must be unique. Attempting to create a duplicate ID will result in an error message.
- **Score Validation**: All scores must be between 0 and 100. The system validates inputs and rejects out-of-range values.
- **Zero-Based Indexing**: When removing scores or courses, remember that indexing starts at 0 (first item = index 0).
- **In-Memory Storage**: All data is stored in memory using Python dictionaries. Data will be lost when the program exits. For persistent storage, consider implementing file I/O or database integration.
- **Input Validation**: The system handles invalid integer inputs gracefully (e.g., non-numeric values for age or seat numbers).

---

## Future Enhancements

- [ ] File-based persistent storage (JSON/CSV)
- [ ] Database integration (SQLite)
- [ ] Search and filter functionality
- [ ] Export reports to PDF/Excel
- [ ] GUI interface using Tkinter

---

## License

This project is licensed under the MIT License - feel free to use, modify, and distribute as needed.

---

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve the functionality.

---

<p align="center">Built with Python 🐍</p>
