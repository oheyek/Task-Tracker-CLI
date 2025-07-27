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
        "createdAt": date,
        "updatedAt": date,
    }
    tasks.append(new_task)
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)
        print(f"Task added successfully (ID: {id})")


def update(id, task) -> None:
    """
    Function to update an existing task.
    :param id: The id of a task to be updated.
    :param task: The new description for a selected task.
    """
    tasks = []
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        pass
    try:
        task_id = int(id) - 1
        tasks[task_id]["description"] = str(task)
        tasks[task_id]["updatedAt"] = date
    except ValueError:
        print(f"Invalid ID format: '{id}'. Please provide a numeric ID.")
    except IndexError:
        print(f"No task found with ID: {id}. Please provide a valid task ID.")
    else:
        with open("tasks.json", "w") as file:
            json.dump(tasks, file, indent=4)
            print(f"Task updated successfully (ID: {id})")


def delete(id) -> None:
    """
    Function to delete tasks.
    :param id: Id of a task to be deleted.
    """
    tasks = []
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        pass
    found = False
    try:
        id = int(id)
        for element in range(len(tasks)):
            if tasks[element]["id"] == id:
                del tasks[element]
                print(f"Task deleted successfully (ID: {id})")
                found = True
                break
    except ValueError:
        print(f"Invalid ID format: '{id}'. Please provide a numeric ID.")
    else:
        if found:
            with open("tasks.json", "w") as file:
                json.dump(tasks, file, indent=4)
        else:
            print(f"No task found with ID: {id}. Please provide a valid task ID.")


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
            task_name = sys.argv[2]
            add(task_name)
        case "update":
            if len(sys.argv) <= 3:
                raise ValueError(
                    "Task id and new description is required for the 'update' operation."
                )
            task_id = sys.argv[2]
            task_name = sys.argv[3]
            update(task_id, task_name)
        case "delete":
            if len(sys.argv) <= 2:
                raise ValueError("Task id is required for the 'delete' operation.")
            task_id = sys.argv[2]
            delete(task_id)
        case _:
            raise ValueError("Invalid operation.")


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Error: Missing operation. Usage: python main.py <operation> [args]")
        sys.exit(1)
    operation = sys.argv[1]
    date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    main(operation)
