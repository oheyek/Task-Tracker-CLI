import json
import sys
import datetime


def add(task):
    tasks = []
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        pass
    finally:
        id = len(tasks) + 1
        new_task = {
            "id": id,
            "description": task,
            "status": "todo",
            "createdAt": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
            "updatedAt": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        }
        tasks.append(new_task)
    with open("tasks.json", "w") as file:
        pass
    with open("tasks.json", "a") as file:
        json.dump(tasks, file, indent=4)
        print(f"Task added successfully (ID: {id})")


def update():
    print("Update operation")


def delete():
    print("Delete operation")


def main(operation) -> None:
    match operation:
        case "add":
            task_name = str(sys.argv[2])
            add(task_name)
        case "update":
            update()
        case "delete":
            delete()
        case _:
            raise KeyError("Invalid operation")


if __name__ == "__main__":
    operation = sys.argv[1]
    main(operation)
