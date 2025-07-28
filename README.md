# 🚀 Task Tracker CLI

A sleek, lightweight command-line task management tool built with Python. Keep your productivity on track with simple commands and JSON-based storage.

## ✨ Features

- **Simple & Fast**: Add, update, delete, and manage tasks with single commands
- **Status Tracking**: Organize tasks with `todo`, `in-progress`, and `done` statuses
- **Timestamp Management**: Automatic creation and update timestamps
- **Flexible Filtering**: List tasks by status or view all at once
- **JSON Storage**: Human-readable task storage in `tasks.json`
- **Error Handling**: Robust input validation and helpful error messages

## 🛠️ Installation

### Quick Setup
```bash
# Clone the repository
git clone https://github.com/oheyek/Task-Tracker-CLI.git
cd Task-Tracker-CLI

# Install dependencies
pip install -r requirements.txt

# Install as a CLI tool (optional)
pip install -e .
```

### Using as Installed CLI
After installation, you can use `task-cli` directly:
```bash
task-cli add "Learn Python"
```

### Using Python Script
Alternatively, run directly with Python:
```bash
python main.py add "Learn Python"
```

## 🎯 Usage

### Adding Tasks
```bash
# Add a new task
task-cli add "Complete project documentation"
task-cli add "Review pull requests"
```

### Listing Tasks
```bash
# List all tasks
task-cli list

# List tasks by status
task-cli list todo
task-cli list in-progress
task-cli list done
```

### Updating Tasks
```bash
# Update task description
task-cli update 1 "Complete comprehensive project documentation"
```

### Managing Task Status
```bash
# Mark task as in-progress
task-cli mark-in-progress 1

# Mark task as done
task-cli mark-done 1

# Mark task back to todo
task-cli mark-todo 1
```

### Deleting Tasks
```bash
# Delete a task by ID
task-cli delete 1
```

## 📋 Command Reference

| Command | Arguments | Description | Example |
|---------|-----------|-------------|---------|
| `add` | `<description>` | Add a new task | `task-cli add "Buy groceries"` |
| `list` | `[status]` | List tasks (all, todo, in-progress, done) | `task-cli list done` |
| `update` | `<id> <description>` | Update task description | `task-cli update 2 "New description"` |
| `delete` | `<id>` | Delete a task | `task-cli delete 3` |
| `mark-todo` | `<id>` | Mark task as todo | `task-cli mark-todo 1` |
| `mark-in-progress` | `<id>` | Mark task as in-progress | `task-cli mark-in-progress 1` |
| `mark-done` | `<id>` | Mark task as completed | `task-cli mark-done 1` |

## 📊 Task Structure

Each task is stored with the following structure:
```json
{
    "id": 1,
    "description": "Complete project documentation",
    "status": "todo",
    "createdAt": "2025-01-15T10:30:00",
    "updatedAt": "2025-01-15T10:30:00"
}
```

### Status Options
- `todo` - Task is pending
- `in-progress` - Task is currently being worked on
- `done` - Task is completed

## 🗂️ File Structure

```
Task-Tracker-CLI/
├── main.py           # Main application logic
├── tasks.json        # Task storage (auto-generated)
├── requirements.txt  # Python dependencies
├── setup.py         # Package setup configuration
└── README.md        # This file
```

## 🔧 Technical Details

- **Language**: Python 3.8+
- **Storage**: JSON file-based persistence
- **Dependencies**: Standard library + datetime package
- **Error Handling**: Comprehensive input validation
- **ID Management**: Auto-incrementing task IDs

## 🚦 Error Handling

The CLI provides helpful error messages for common issues:
- Invalid task IDs
- Missing required arguments
- Invalid status values
- File operation errors

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 Examples

### Typical Workflow
```bash
# Add some tasks
task-cli add "Set up development environment"
task-cli add "Write unit tests"
task-cli add "Deploy to production"

# Start working on first task
task-cli mark-in-progress 1

# Check progress
task-cli list in-progress

# Complete and move to next
task-cli mark-done 1
task-cli mark-in-progress 2

# View all completed tasks
task-cli list done
```

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

**Happy Task Tracking! 🎉**

## Author

Made with ❤️ by ohey<br>
[![Buy Me A Coffee](https://www.buymeacoffee.com/assets/img/custom_images/black_img.png)](https://www.buymeacoffee.com/ohey)

---

If you find this project useful, consider buying me a coffee!

https://roadmap.sh/projects/task-tracker
