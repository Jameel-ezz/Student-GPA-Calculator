def calculate_grade(grade):
    # Assign a letter grade based on the grade input
    if grade >= 90:
        letter_grade = "A"
    elif grade >= 80:
        letter_grade = "B"
    elif grade >= 70:
        letter_grade = "C"
    elif grade >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"

    # Calculate the weighted grade
    weighted_grade = (grade / 20) - 1

    # Return the letter grade and the weighted grade
    return letter_grade, weighted_grade


def calculate_gpa(grades, credit_hours):
    # Initialize total_quality_points and total_credit_hours
    total_quality_points = 0
    total_credit_hours = 0

    # Iterate through the grades and credit_hours lists
    for grade, hours in zip(grades, credit_hours):
        # Call the calculate_grade function to get the letter grade and weighted grade
        letter_grade, weighted_grade = calculate_grade(grade)

        # Assign a quality point value based on the letter grade
        if grade >= 90:
            quality_points = 4.0
        elif grade >= 80:
            quality_points = 3.0
        elif grade >= 70:
            quality_points = 2.0
        elif grade >= 60:
            quality_points = 1.0
        else:
            quality_points = 0.0

        # Add the quality points * credit hours to the total_quality_points
        # Add the credit hours to the total_credit_hours
        total_quality_points += quality_points * hours
        total_credit_hours += hours

    # Calculate the semester GPA
    semester_gpa = total_quality_points / total_credit_hours

    # Return the semester GPA
    return semester_gpa


# Test the calculate_gpa function with a list of grades and a list of credit hours
grades = [85, 90, 75, 92, 88]
credit_hours = [3, 3, 3, 3, 3]
semester_gpa = calculate_gpa(grades, credit_hours)

# Print the semester GPA
print("Semester GPA: ", semester_gpa)