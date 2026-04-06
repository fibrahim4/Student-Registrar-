"""
File name: utils_student.py
Purpose: Utility functions for the student module
Author: Fuahd Ibrahim
Date: 11/30/2025
"""

import csv;
import os;

# ---------------------------------------------------------
# LOGIN HELPERS
# ---------------------------------------------------------
def verify_student(username, password):
    """Check if username/password exist in students.csv."""
    try:
        with open("students.csv", "r", newline='') as csvfile:
            reader = csv.reader(csvfile);
            next(reader, None);  # skip header
            for row in reader:
                if len(row) >= 4:
                    if row[2] == username and row[3] == password:
                        return True;
        return False;
    except:
        print("Error: unable to read students.csv.");
        return False;


def student_login():
    """Student login with up to 5 attempts."""
    attempts = 0;
    while attempts < 5:
        username = input("Enter your student username: ");
        password = input("Enter your password: ");

        if verify_student(username, password):
            print("\nLogin successful!\n");
            return username;

        attempts += 1;
        print("Incorrect username or password. Attempts left:", 5 - attempts);

    print("Too many failed attempts. Exiting student module.");
    return None;


# ---------------------------------------------------------
# COURSE & ENROLLMENT HELPERS
# ---------------------------------------------------------
def load_courses():
    """Return list of all courses as (number, title)."""
    courses = [];
    if not os.path.exists("courses.csv"):
        return courses;

    try:
        with open("courses.csv", "r", newline='') as csvfile:
            reader = csv.reader(csvfile);
            next(reader, None);
            for row in reader:
                if len(row) >= 2:
                    courses.append((row[0], row[1]));
    except:
        print("Error reading courses.csv.");

    return courses;


def load_enrollments():
    """Return list of all enrollments as (username, course_number)."""
    enrollments = [];
    if not os.path.exists("enrollments.csv"):
        return enrollments;

    try:
        with open("enrollments.csv", "r", newline='') as csvfile:
            reader = csv.reader(csvfile);
            next(reader, None);
            for row in reader:
                if len(row) >= 2:
                    enrollments.append((row[0], row[1]));
    except:
        print("Error reading enrollments.csv.");

    return enrollments;


def save_enrollment(username, course_number):
    """Append new enrollment to enrollments.csv."""
    file_exists = os.path.exists("enrollments.csv");

    try:
        with open("enrollments.csv", "a", newline='') as csvfile:
            writer = csv.writer(csvfile);
            if not file_exists:
                writer.writerow(["student_username", "course_number"]);
            writer.writerow([username, course_number]);
    except:
        print("Error: could not write to enrollments.csv.");


def enroll_in_course(username):
    """Allow the student to enroll in a course."""
    courses = load_courses();
    if len(courses) == 0:
        print("No courses available to enroll in.");
        return;

    print("===== AVAILABLE COURSES =====");
    for idx, course in enumerate(courses):
        print(str(idx + 1) + ". " + course[0] + " | " + course[1]);

    choice = input("Select a course by number: ");
    if not choice.isdigit():
        print("Invalid selection.");
        return;

    choice = int(choice);
    if choice < 1 or choice > len(courses):
        print("Selection out of range.");
        return;

    course_number = courses[choice - 1][0];

    # Check if already enrolled
    enrollments = load_enrollments();
    for en in enrollments:
        if en[0] == username and en[1] == course_number:
            print("You are already enrolled in that course.");
            return;

    # Save new enrollment
    save_enrollment(username, course_number);
    print("Enrollment successful!");


def view_my_courses(username):
    """Display all courses the student is enrolled in."""
    enrollments = load_enrollments();
    courses = load_courses();

    # Find the student's course numbers
    my_course_numbers = set();
    for en in enrollments:
        if en[0] == username:
            my_course_numbers.add(en[1]);

    if len(my_course_numbers) == 0:
        print("You are not enrolled in any courses yet.");
        return;

    print("\nHello " + username + "! Below are courses you are enrolled in:\n")

    # Match numbers to titles
    for number in my_course_numbers:
        for cnum, ctitle in courses:
            if cnum == number:
                print("Course Number: " + cnum + ", Title: " + ctitle);
