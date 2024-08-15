## TaskBuddy
TaskBuddy is a command-line interface (CLI) application for managing and scheduling tasks. It allows users to create, view, update, and delete tasks with ease.

### Features
* **Add Tasks**: Create new tasks with a description and due date.
* **List Tasks**: View all scheduled tasks with their details.
* **Update Tasks**: Modify existing tasks' descriptions or due dates.
* **Delete Tasks**: Remove tasks from your schedule.
* **Mark Tasks Complete**: Mark tasks as completed.

### Installation
To get started with TaskBuddy, clone the repository and install the required dependencies.

```bash
git clone https://github.com/prcryx/taskbuddy.git
cd taskbuddy
pip install -r requirements.txt
python -m pip install .
```
or in dev mode you can install this as an editable package
```bash
python -m pip install -e .
```
### Usage

#### Adding a Task
```bash
taskbuddy --add "Task Description" --due "YYYY-MM-DD"
```

#### Listing Tasks
```bash
taskbuddy --list
```

#### Updating a Task
```bash
taskbuddy --update TASK_ID --description "New Description" --due "YYYY-MM-DD"
```

#### Deleting a Task
```bash
taskbuddy --delete TASK_ID
```

#### Marking a Task as Complete
```bash
taskbuddy complete TASK_ID
```

### Contributing
Feel free to contribute to TaskBuddy by submitting pull requests or opening issues.

### License
This project is licensed under the MIT License. See the LICENSE file for details.
