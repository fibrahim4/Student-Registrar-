"""
File name: utils_admin.py
Purpose: Utility functions for admin module
Author: Fuahd Ibrahim
Date: 11/23/2025
"""

import csv;
import os;

#---------------------------------------------------------------
# Admin authentication utilities
#---------------------------------------------------------------
def verify_admin(username, password):
    """Verify admin username and password using admin.csv."""
    try:
        with open("admin.csv", "r", newline='') as csvfile:
            reader = csv.reader(csvfile);
            next(reader);  # skip header
            for row in reader:
                if len(row) >= 2 and row[0] == username and row[1] == password:
                    return True;
        return False;
    except:
        print("Error: unable to read admin.csv. Make sure the file exists.");
        return False;


def admin_login():
    """Allow up to 5 login attempts for an admin."""
    attempts = 0;
    while attempts < 5:
        username = input("Enter admin username: ");
        password = input("Enter admin password: ");

        if verify_admin(username, password):
            print("\nLogin successful!\n");
            return True;
        else:
            attempts += 1;
            print("Incorrect username/password. Attempts remaining:", 5 - attempts);

    print("Too many failed attempts. Exiting program.");
    return False;


#---------------------------------------------------------------
# Helper functions for students
#---------------------------------------------------------------
def load_existing_student_usernames():
    """Return a set of existing student usernames from students.csv."""
    usernames = set();
    if not os.path.exists("students.csv"):
        return usernames;

    try:
        with open("students.csv", "r", newline='') as csvfile:
            reader = csv.reader(csvfile);
            next(reader, None);
            for row in reader:
                if len(row) >= 3:
                    usernames.add(row[2]);
    except:
        print("Warning: unable to read students.csv.");
    return usernames;


def add_student():
    """
    Add new students.
    Fields: first name, last name, unique username, password, email.
    Ensures usernames are unique.
    """
    print("\n===== ADD NEW STUDENT =====");

    # Create file with header if missing
    file_exists = os.path.exists("students.csv");
    if not file_exists:
        with open("students.csv", "w", newline='') as csvfile:
            writer = csv.writer(csvfile);
            writer.writerow(["first_name", "last_name", "username", "password", "email"]);

    existing_usernames = load_existing_student_usernames();

    while True:
        first = input("Enter student's first name: ");
        last = input("Enter student's last name: ");

        while True:
            username = input("Enter a username for the student (must be unique): ");
            if username in existing_usernames:
                print("That username already exists. Please choose another.");
            else:
                break;

        password = input("Enter a password for the student: ");
        email = input("Enter student's email: ");

        try:
            with open("students.csv", "a", newline='') as csvfile:
                writer = csv.writer(csvfile);
                writer.writerow([first, last, username, password, email]);
            print("Student added successfully!\n");
            existing_usernames.add(username);
        except:
            print("Error: could not write to students.csv.");

        choice = input("Add another student? (y/n): ").strip().lower();
        if choice != "y":
            break;


#---------------------------------------------------------------
# Helper functions for courses
#---------------------------------------------------------------
def load_existing_course_numbers():
    """Return a set of existing course numbers from courses.csv."""
    numbers = set();
    if not os.path.exists("courses.csv"):
        return numbers;

    try:
        with open("courses.csv", "r", newline='') as csvfile:
            reader = csv.reader(csvfile);
            next(reader, None);
            for row in reader:
                if len(row) >= 1:
                    numbers.add(row[0]);
    except:
        print("Warning: unable to read courses.csv.");
    return numbers;


def add_course():
    """
    Add new courses.
    Fields: unique course number, course title.
    Ensures course numbers are unique.
    """
    print("\n===== ADD NEW COURSE =====");

    file_exists = os.path.exists("courses.csv");
    if not file_exists:
        with open("courses.csv", "w", newline='') as csvfile:
            writer = csv.writer(csvfile);
            writer.writerow(["course_number", "course_title"]);

    existing_numbers = load_existing_course_numbers();

    while True:
        while True:
            course_number = input("Enter a course number (must be unique): ");
            if course_number in existing_numbers:
                print("That course number already exists. Please choose another.");
            else:
                break;

        course_title = input("Enter the course title: ");

        try:
            with open("courses.csv", "a", newline='') as csvfile:
                writer = csv.writer(csvfile);
                writer.writerow([course_number, course_title]);
            print("Course added successfully!\n");
            existing_numbers.add(course_number);
        except:
            print("Error: could not write to courses.csv.");

        choice = input("Add another course? (y/n): ").strip().lower();
        if choice != "y":
            break;


#---------------------------------------------------------------
# View functions
#---------------------------------------------------------------
def view_students():
    """Display all students in a nicely formatted way."""
    print("\n===== ALL STUDENTS =====");
    if not os.path.exists("students.csv"):
        print("No student data available yet.");
        return;

    try:
        with open("students.csv", "r", newline='') as csvfile:
            reader = csv.reader(csvfile);
            next(reader, None);
            for row in reader:
                if len(row) >= 5:
                    print("Name: " + row[0] + " " + row[1] +
                          " | Username: " + row[2] +
                          " | Email: " + row[4]);
    except:
        print("Error: unable to read students.csv.");


def view_courses():
    """Display all courses in a nicely formatted way."""
    print("\n===== ALL COURSES =====");
    if not os.path.exists("courses.csv"):
        print("No course data available yet.");
        return;

    try:
        with open("courses.csv", "r", newline='') as csvfile:
            reader = csv.reader(csvfile);
            next(reader, None);
            for row in reader:
                if len(row) >= 2:
                    print("Course Number: " + row[0] + " | Title: " + row[1]);
    except:
        print("Error: unable to read courses.csv.");


#---------------------------------------------------------------
# NEW FOR PART 4 — View all enrollments
#---------------------------------------------------------------
def view_enrollments():
    """Display all enrollments with course titles."""
    print("\n===== ALL ENROLLMENTS =====");

    if not os.path.exists("enrollments.csv"):
        print("No enrollments available yet.");
        return;

    # Load enrollments
    enrollments = [];
    try:
        with open("enrollments.csv", "r", newline='') as csvfile:
            reader = csv.reader(csvfile);
            next(reader, None);
            for row in reader:
                if len(row) >= 2:
                    enrollments.append((row[0], row[1]));  # username, course_number
    except:
        print("Error: unable to read enrollments.csv.");
        return;

    # Load courses into dictionary
    courses = {};
    try:
        with open("courses.csv", "r", newline='') as csvfile:
            reader = csv.reader(csvfile);
            next(reader, None);
            for row in reader:
                if len(row) >= 2:
                    courses[row[0]] = row[1];  # number → title
    except:
        print("Error: unable to read courses.csv.");
        return;

    # Print results
    if len(enrollments) == 0:
        print("There are no enrollments yet.");
        return;

    for username, course_num in enrollments:
        course_title = courses.get(course_num, "Unknown Title");
        print(username + " → " + course_num + " (" + course_title + ")");
