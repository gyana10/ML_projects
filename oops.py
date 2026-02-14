# Write a Python program to:

# Define a Student class with attributes: name, grade, percentage, and team.

# Include an __init__ method to initialize these attributes.

# Add a method student_details that prints the student’s details in the format:
# "<name> is in <grade> grade with <percentage>%, from team <team>".

# Create two teams (team1 and team2) as string variables.

# Create at least two student objects, each belonging to one of the teams.

# Call the student_details method for each student to display their details.

class Student:
    def __init__(self, name, grade, percentage, team):
        self.name = name
        self.grade = grade
        self.percentage = percentage
        self.team = team

    def student_details(self):
        print(f"{self.name} is in {self.grade} grade with {self.percentage}%, from team {self.team}.")


team1 = "Red Team"
team2 = "Blue Team"

student1 = Student("Alice", "10th", 85, team1)
student2 = Student("Bob", "11th", 90, team2)

student1.student_details()
student2.student_details()
 