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
        tasks[task_id]["updatedAt"] = datetime.datetime.now().strftime(
            "%Y-%m-%dT%H:%M:%S"
        )
    except ValueError:
        print(f"Invalid ID format: '{id}'. Please provide a numeric ID.")
    except IndexError:
        print(f"No task found with ID: {id}. Please provide a valid task ID.")
    else:
        with open("tasks.json", "w") as file:
            json.dump(tasks, file, indent=4)
            print(f"Task updated successfully (ID: {id})")


def mark(id, status) -> None:
    """
    Function to mark tasks.
    :param id: Id of a task to be marked.
    :param status: The status of the task.
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
                allowed_status = ["todo", "in-progress", "done"]
                if status in allowed_status:
                    tasks[element]["status"] = status
                    tasks[element]["updatedAt"] = datetime.datetime.now().strftime(
                        "%Y-%m-%dT%H:%M:%S"
                    )
                else:
                    raise ValueError("Invalid status.")
                print(f"Task marked successfully (ID: {id})")
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


def list_tasks(status) -> None:
    """
    Function to list tasks basing on status.
    :param status: The status of the task to be searched.
    """
    tasks = []
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        pass

    allowed_search = ["all", "todo", "in-progress", "done"]
    if status in allowed_search:
        if status == "all":
            for task in range(len(tasks)):
                print("==========")
                print(f"ID: {tasks[task]['id']}")
                print(f"Description: {tasks[task]['description']}")
                print(f"Status: {tasks[task]['status']}")
                print(f"Created at: {tasks[task]['createdAt']}")
                print(f"Updated at: {tasks[task]['updatedAt']}")
        else:
            for task in range(len(tasks)):
                if tasks[task]["status"] == status:
                    print("==========")
                    print(f"ID: {tasks[task]['id']}")
                    print(f"Description: {tasks[task]['description']}")
                    print(f"Status: {tasks[task]['status']}")
                    print(f"Created at: {tasks[task]['createdAt']}")
                    print(f"Updated at: {tasks[task]['updatedAt']}")
    else:
        raise ValueError("Invalid task status.")


def main() -> None:
    """
    Main function of a program.
    """
    operation = sys.argv[1]
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
        case "mark-todo":
            if len(sys.argv) <= 2:
                raise ValueError("Task id is required for the 'mark-todo' operation.")
            task_id = sys.argv[2]
            mark(task_id, "todo")
        case "mark-in-progress":
            if len(sys.argv) <= 2:
                raise ValueError(
                    "Task id is required for the 'mark-in-progress' operation."
                )
            task_id = sys.argv[2]
            mark(task_id, "in-progress")
        case "mark-done":
            if len(sys.argv) <= 2:
                raise ValueError("Task id is required for the 'mark-done' operation.")
            task_id = sys.argv[2]
            mark(task_id, "done")
        case "list":
            if len(sys.argv) <= 2:
                status = "all"
            else:
                status = sys.argv[2]
            list_tasks(status)

        case _:
            raise ValueError("Invalid operation.")


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Error: Missing operation. Usage: python main.py <operation> [args]")
        sys.exit(1)
    main()
