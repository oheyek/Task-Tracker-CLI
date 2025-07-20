import json
import sys
import datetime


def add(task) -> None:
    """
    Function to add a new task to the tasks.json file.
    :param task: Task description to be added.
    """
    tasks = []
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        pass
    id = max((task["id"] for task in tasks), default=0) + 1
    new_task = {
        "id": id,
        "description": task,
        "status": "todo",
        "createdAt": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        "updatedAt": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
    }
    tasks.append(new_task)
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)
        print(f"Task added successfully (ID: {id})")


def update():
    print("Update operation")


def delete():
    print("Delete operation")


def main(operation) -> None:
    """
    Main function of a program.
    :param operation: Operation to be performed.
    """
    match operation:
        case "add":
            if len(sys.argv) <= 2:
                raise ValueError(
                    "Task description is required for the 'add' operation."
                )
            task_name = str(sys.argv[2])
            add(task_name)
        case "update":
            update()
        case "delete":
            delete()
        case _:
            raise ValueError("Invalid operation")


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Error: Missing operation. Usage: python main.py <operation> [args]")
        sys.exit(1)
    operation = sys.argv[1]
    main(operation)
