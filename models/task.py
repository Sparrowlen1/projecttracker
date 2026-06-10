class Task:
    def __init__(self, title, assigned_to=None, status='pending', task_id=None):
        self.title = title
        self.assigned_to = assigned_to
        self.status = status
        self.task_id = task_id
    
    def to_dict(self):
        return {
            'title': self.title,
            'assigned_to': self.assigned_to,
            'status': self.status,
            'task_id': self.task_id
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            data['title'],
            data.get('assigned_to'),
            data.get('status', 'pending'),
            data.get('task_id')
        )
    
    def mark_complete(self):
        self.status = 'completed'
    
    def display_info(self):
        return f"Task: {self.title} | Status: {self.status} | Assigned to: {self.assigned_to}"