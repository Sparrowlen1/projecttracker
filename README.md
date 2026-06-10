# project management tool
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 650 120" width="100%" height="100%">
  <defs>
    <clipPath id="typing">
      <rect x="20" y="30" width="0" height="40">
        <animate attributeName="width" from="0" to="480" dur="3s" begin="0.5s" fill="freeze" />
      </rect>
    </clipPath>
    <style>
      .cursor {
        animation: blink 1s step-end infinite;
      }
      @keyframes blink {
        0%, 100% { opacity: 1; }
        50% { opacity: 0; }
      }
    </style>
  </defs>

  <!-- terminal bg -->
  <rect width="650" height="120" rx="8" fill="#0f0f17" stroke="#2a2a3a" stroke-width="1.5" />

  <!-- top bar -->
  <rect width="650" height="28" rx="8" fill="#181824" />
  <rect y="14" width="650" height="14" fill="#181824" />
  <circle cx="18" cy="14" r="5" fill="#ff5f56" />
  <circle cx="34" cy="14" r="5" fill="#ffbd2e" />
  <circle cx="50" cy="14" r="5" fill="#27c93f" />

  <!-- prompt -->
  <text x="15" y="68" fill="#5cd9a5" font-family="'Courier New', monospace" font-size="18" font-weight="bold">$</text>

  <!-- typed message -->
  <g clip-path="url(#typing)">
    <text x="38" y="68" fill="#e2e2e8" font-family="'Courier New', monospace" font-size="18">Welcome to my project!</text>
  </g>

  <!-- blinking cursor -->
  <text x="38" y="68" fill="#e2e2e8" font-family="'Courier New', monospace" font-size="18" class="cursor">
    <animate attributeName="opacity" values="0;1;0" dur="1s" repeatCount="indefinite" begin="3.5s" />
    █
  </text>
</svg>
## Setup Instructions

1. Clone the repository:
2. pip install -r requirements.txt(install dependencies)

## how to run cli commands
python main.py <command>; that is 
### 1. Add a user
python main.py add-user --name "Sparrowlen" --email "sparrowlen@example.com"

### 2. Add another user
python main.py add-user --name "Sparrowlen2" --email "sparrowlen2@example.com"

### 3. List all users
python main.py list-users

### 4. Add a project for John
python main.py add-project --user "Sparrowlen" --title "E-commerce Website" --description "Build a fully functional e-commerce platform" --due-date "2025-12-31"

### 5. Add another project for John
python main.py add-project --user "Sparrowlen" --title "Mobile App" --description "Develop iOS and Android app" --due-date "2025-03-15"

### 6. Add project for Jane
python main.py add-project --user "Sparrowlen2" --title "Database Migration" --description "Migrate legacy database to cloud" --due-date "2025-10-30"

### 7. List all projects
python main.py list-projects

### 8. List projects for specific user
python main.py list-projects --user "Sparrowlen"

### 9. Add tasks to a project
python main.py add-task --project "E-commerce Website" --title "Design database schema"

### 10. Add more tasks
python main.py add-task --project "E-commerce Website" --title "Implement user authentication"
python main.py add-task --project "E-commerce Website" --title "Create shopping cart feature"

### 11. List tasks for a project
python main.py list-tasks --user "Sparrowlen" --project "E-commerce Website"

### 12. Complete a task
python main.py complete-task --title "Design database schema"

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
1. Add project: python main.py add-project --user "Sparrow" --title "CLI Tool" --description "Build a CLI tool" --due-date "2024-12-31"
2. List projects: python main.py list-projects or python main.py list-projects --user "Sparrow"
3. Search projects: python main.py search-projects --user "Sparrow" --term "CLI"

### task management
1. Add task: python main.py add-task --project "CLI Tool" --title "Implement parser"
2. Complete task: python main.py complete-task --title "Implement parser"
3. List tasks: python main.py list-tasks --user "Sparrow" --project "CLI Tool"

## features
:: Create and manage users with unique IDs
2. Add projects to specific users with due dates
3. Assign tasks to projects and track completion status
4. Persistent data storage using JSON
5. Search functionality for projects
6. Pretty table display for better readability

## Dependencies
1. python-dateutil: For flexible date parsing
2. prettytable: For formatted table output

## testing
:: python -m unittest discover tests