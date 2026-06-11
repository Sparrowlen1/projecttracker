# project management tool
<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=28&pause=1200&color=36BCF7&center=true&vCenter=true&width=1000&lines=Howdy+Estimed+Viewer+Welcome+to+the+Project+Documentation;A+Step-by-Step+Guide;Built+with+Python" alt="Typing SVG" />
</p>

## Setup Instructions

1. Clone the repository
2. pipenv install --dev (installs all dependencies including dev)
3. pipenv install (installs production packages)
4. pipenv run pytest (run test using dev dependencies)
5. pip install -r requirements.txt(install dependencies) 

## Disclaimer
1. the below CLI commands are just examples try adding your own "User" and "Email" and perform the cli commands replacing "Sparrowlen's" with your own user name that you added for a clean and workable CLI with no errors, Have fun my fellow Sparrow Viewer

## how to run cli commands
python main.py [command can be add-user, list-users etc check below for guidance fellow developer]; that is 
### 1. Add a user
python main.py add-user --name "Sparrowlen" --email "sparrowlen@example.com"

### 2. Add another user
python main.py add-user --name "Sparrowlen2" --email "sparrowlen2@example.com"

### 3. List all users
python main.py list-users

### 4. Add a project for Sparrowlen
python main.py add-project --user "Sparrowlen" --title "e-commerce Website" --description "Build a fully functional e-commerce platform" --due-date "2025-12-31"

### 5. Add another project for Sparrowlen
python main.py add-project --user "Sparrowlen" --title "Mobile App" --description "Develop iOS and Android app(flutter and dart)" --due-date "2025-03-15"

### 6. Add project for Sparrowlen2
python main.py add-project --user "Sparrowlen2" --title "Database Migration" --description "Migrate legacy database to cloud" --due-date "2025-10-30"

### 7. List all projects
python main.py list-projects

### 8. List projects for specific user
python main.py list-projects --user "Sparrowlen"

### 9. Add tasks to a project
python main.py add-task --project "e-commerce Website" --title "Design database schema(hehe next module just a btw)"

### 10. Add more tasks
python main.py add-task --project "e-commerce Website" --title "Implement user authentication"
python main.py add-task --project "e-commerce Website" --title "Create shopping cart feature"

### 11. List tasks for a project
python main.py list-tasks --user "Sparrowlen" --project "E-commerce Website"

### 12. Complete a task
python main.py complete-task --title "Design database schema(though is in the next module hehe)"

### 13. View tasks again to see status change
python main.py list-tasks --user "Sparrowlen" --project "E-commerce Website"

### 14. Search projects
python main.py search-projects --user "Sparrowlen2" --term "website"

### 15. Delete a user
python main.py delete-user --name "Sparrowlen2"

### 16. Verify user was deleted
python main.py list-users

## available commands
### user management
1. add users: python main.py add-user --name "Sparrow" --email "Sparrow@example.com"
2. List users: python main.py list-users
3. Delete user: python main.py delete-user --name "Sparrow"

### project management
1. Add project: python main.py add-project --user "Sparrow" --title "Web dev" --description "Build a website" --due-date "2024-12-31"
2. List projects: python main.py list-projects or python main.py list-projects --user "Sparrow"
3. Search projects: python main.py search-projects --user "Sparrow" --term "web"

### task management
1. Add task: python main.py add-task --project "Web dev" --title "Implement parser"
2. Complete task: python main.py complete-task --title "Implement parser"
3. List tasks: python main.py list-tasks --user "Sparrow" --project "web dev

## features
1. Create and manage users with unique IDs (asigned USR for user if user is the first entry then it will be USR 1)
2. Add projects to specific users with due dates
3. Assign tasks to projects and track completion status
4. Persistent data storage using JSON
5. Search functionality for projects
6. Pretty table display for better readability
7. inheritance applied with project.py, task,py, user.py inheriting from the base.py and applying a repr function and str function in all the models

## Dependencies
1. python-dateutil: For flexible date parsing
2. prettytable: For formatted table output
3. pytest for tests(dev dependency)

## testing
1. pipenv install pytest --dev
2. pipenv run pytest
3. pipenv run pytest tests/test_api.py (to run a single test)
4. (use unittest alternatvely)python -m unittest tests.test_user.py (since iko kwa the tests folder)