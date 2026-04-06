"""
File name: student_module.py
Purpose: Student module for login, enrollment, and viewing courses
Author: Fuahd Ibrahim
Date: 11/30/2025
"""

import sys;
from utils_student import student_login, enroll_in_course, view_my_courses;

def student_menu(username):
    while True:
        print("=========== STUDENT MENU ===========");
        print("1. Enroll in a course");
        print("2. View my courses");
        print("3. Exit");

        choice = input("Select an option (1-3): ");

        if choice == "1":
            enroll_in_course(username);
        elif choice == "2":
            view_my_courses(username);
        elif choice == "3":
            print("Logging out. Goodbye!");
            break;
        else:
            print("Invalid selection. Try again.");

def main():
    print("=========== STUDENT MODULE ===========\n");

    username = student_login();
    if username is None:
        sys.exit();

    student_menu(username);

if __name__ == "__main__":
    main();
