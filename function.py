def greet(name):
  return f"Hello, {name}!"

message = greet("Rangga")
print(message)


def get_student_info(student: dict) -> str:
    return (
      f"Name: {student['name']}\n"
      f"Age: {student['age']}\n"
      f"Major: {student['major']}\n"
    )


student_data = {
  "name": "Rangga",
  "age": 21,
  "major": "Computer Science"
}

result = get_student_info(student_data)
print(result)
