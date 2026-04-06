"""
File name: admin_module.py
Purpose: Admin login + menu (add students/courses, view lists) for Final Project
Author: Fuahd Ibrahim
Date: 11/23/2025
"""

import sys;

from utils_admin import admin_login, add_student, add_course, view_students, view_courses, view_enrollments;

#---------------------------------------------------------------
# Main admin menu loop
#---------------------------------------------------------------
def admin_menu():
    while True:
        print("\n=========== ADMIN MENU ===========");
        print("1. Add a new student");
        print("2. Add a new course");
        print("3. View all students");
        print("4. View all courses");
        print("5. View all enrollments");
        print("6. Exit");

        choice = input("Please select an option (1-6): ");

        if choice == "1":
            add_student();
        elif choice == "2":
            add_course();
        elif choice == "3":
            view_students();
        elif choice == "4":
            view_courses();
        elif choice == "5":
            view_enrollments();
        elif choice == "6":
            print("Exiting admin module. Goodbye!");
            break;
        else:
            print("Invalid option. Please enter a number between 1 and 6.");

def main():
    print("=========== ADMIN MODULE ===========\n");

    logged_in = admin_login();
    if not logged_in:
        sys.exit("Exiting program...");

    # After successful login, show admin menu
    admin_menu();

if __name__ == "__main__":
    main();
