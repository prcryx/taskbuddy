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
pip install -r requirements/base.txt
python -m pip install .
```
or in dev mode you can install this as an editable package
```bash
python -m pip install -e .
```
### Usage

#### Setup
```bash
taskbuddy setup --db_name='taskbuddy.db'
```

#### Adding a Task
```bash
taskbuddy add --task="Task Description" --due="DD-MM-YYYY"
```

#### List All Tasks
```bash
taskbuddy ls --all
```
#### List Specific Task
```bash
taskbuddy ls --id=<task_id>
```

#### Updating Task
```bash
taskbuddy update --id=<task_id> --task="New Description" --due="DD--MM-YYYY" --status=0
```

#### Deleting Task
```bash
taskbuddy del --id=<task_id>
```
#### Deleting All Task
```bash
taskbuddy del --all
```
#### Searching By Due Date
```bash
taskbuddy search --due="DD--MM-YYYY"
```

### Contributing
Feel free to contribute to TaskBuddy by submitting pull requests or opening issues.

### License
This project is licensed under the MIT License. See the LICENSE file for details.

### Early Stage Development - Pre-Alpha Version Warning
This software is currently in the Pre-Alpha stage, meaning it is in a very early phase of development & is under heavy development. At this stage:

* **Active Development**: Core features and functionalities are still being built. Expect frequent updates and significant changes as the project evolves.

* **Unstable**: The software may have many bugs, incomplete features and may not work as expected. Breaking changes can occur at any time without warning.

* **For Testing Purposes Only**: This version is intended for testing, experimentation, and feedback. It is not suitable for production environments.

* **Feedback Welcome**: We encourage developers and early adopters to experiment with this version and provide feedback. Your input is valuable in shaping the future of the project.
