def main():
    project_name = "AI Internship Week 1"
    tasks_completed = 5
    is_active = True

    print("--- Variables & Data Types ---")
    print(f"Project: {project_name} | Tasks Done: {tasks_completed} | Active: {is_active}\n")
    print("--- Loops & Conditionals ---")
    for i in range(1, 6):
        if i % 2 == 0:
            print(f"Task {i} is an EVEN number task.")
        else:
            print(f"Task {i} is an ODD number task.")
    print("\n--- File Handling ---")
    file_name = "task_log.txt"
    with open(file_name, "w") as file:
        file.write("Week 1 Tasks logged successfully.\n")
        file.write("Python basics and Git setup complete.")
    with open(file_name, "r") as file:
        content = file.read()
        print("Content read from task_log.txt:")
        print(content)

if __name__ == "__main__":
    main()