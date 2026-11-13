# List of students and their corresponding marks
students = [("Alice", 85), ("Bob", 40), ("Charlie", 72), ("David", 33), ("Eve", 90)]

passing_score = 50

# List comprehensions to split students into pass and fail
passed_students = [name for name, mark in students if mark >= passing_score]
failed_students = [name for name, mark in students if mark < passing_score]

print(f"Passed students: {passed_students}")
print(f"Failed students: {failed_students}")
