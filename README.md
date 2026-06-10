# Python Project Management CLI Tool
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 280" width="100%" height="100%">
  <defs>
    <!-- Background Glow Filter -->
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="5" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
    
    <!-- Blinking Cursor Animation -->
    <style>
      .cursor {
        animation: blink 1s step-end infinite;
      }
      @keyframes blink {
        from, to { opacity: 1; }
        50% { opacity: 0; }
      }
    </style>
  </defs>

  <!-- Terminal Window Background -->
  <rect width="800" height="280" rx="12" fill="#1e1e2e" />
  <rect width="800" height="280" rx="12" fill="none" stroke="#313244" stroke-width="2" />
  
  <!-- Top Bar -->
  <rect width="800" height="40" rx="12" fill="#181825" />
  <rect y="20" width="800" height="20" fill="#181825" /> <!-- Flatten bottom of top bar -->

  <!-- Window Controls (Red, Yellow, Green) -->
  <circle cx="30" cy="20" r="6" fill="#f38ba8" />
  <circle cx="50" cy="20" r="6" fill="#fab387" />
  <circle cx="70" cy="20" r="6" fill="#a6e3a1" />

  <!-- Line 1: whoami -->
  <text x="25" y="70" fill="#a6e3a1" font-family="'Courier New', 'Fira Code', monospace" font-size="14" font-weight="bold">user@arch:~$</text>
  <text x="155" y="70" fill="#f9e2af" font-family="'Courier New', 'Fira Code', monospace" font-size="14">whoami</text>

  <!-- Line 2: Response -->
  <text x="25" y="95" fill="#a6e3a1" font-family="'Courier New', 'Fira Code', monospace" font-size="14" font-weight="bold">></text>
  <text x="45" y="95" fill="#94e2d5" font-family="'Courier New', 'Fira Code', monospace" font-size="14">danny (Senior Python Developer / AI Engineer)</text>

  <!-- Line 3: pwd -->
  <text x="25" y="125" fill="#a6e3a1" font-family="'Courier New', 'Fira Code', monospace" font-size="14" font-weight="bold">user@arch:~$</text>
  <text x="155" y="125" fill="#f9e2af" font-family="'Courier New', 'Fira Code', monospace" font-size="14">pwd</text>

  <!-- Line 4: Response -->
  <text x="25" y="150" fill="#a6e3a1" font-family="'Courier New', 'Fira Code', monospace" font-size="14" font-weight="bold">></text>
  <text x="45" y="150" fill="#89b4fa" font-family="'Courier New', 'Fira Code', monospace" font-size="14">/home/danny/projects/ai-readme</text>

  <!-- Line 5: python --version -->
  <text x="25" y="180" fill="#a6e3a1" font-family="'Courier New', 'Fira Code', monospace" font-size="14" font-weight="bold">user@arch:~$</text>
  <text x="155" y="180" fill="#f9e2af" font-family="'Courier New', 'Fira Code', monospace" font-size="14">python --version</text>

  <!-- Line 6: Response -->
  <text x="25" y="205" fill="#a6e3a1" font-family="'Courier New', 'Fira Code', monospace" font-size="14" font-weight="bold">></text>
  <text x="45" y="205" fill="#f5c2e7" font-family="'Courier New', 'Fira Code', monospace" font-size="14">Python 3.12.1</text>

  <!-- Line 7: Ready Prompt with Blinking Cursor -->
  <text x="25" y="235" fill="#a6e3a1" font-family="'Courier New', 'Fira Code', monospace" font-size="14" font-weight="bold">user@arch:~$</text>
  <text x="155" y="235" fill="#cdd6f4" font-family="'Courier New', 'Fira Code', monospace" font-size="14" class="cursor">█</text>
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