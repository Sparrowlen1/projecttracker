class User:
    def __init__(self, name, email, user_id=None):
        self.name = name
        self.email = email
        self.user_id = user_id
        self.projects = []
    
    def to_dict(self):
        return {
            'name': self.name,
            'email': self.email,
            'user_id': self.user_id,
            'projects': [p.to_dict() if hasattr(p, 'to_dict') else p for p in self.projects]
        }
    
    @classmethod
    def from_dict(cls, data):
        user = cls(data['name'], data['email'], data.get('user_id'))
        return user
    
    def add_project(self, project):
        self.projects.append(project)
    
    def display_info(self):
        return f"User: {self.name} | Email: {self.email} | ID: {self.user_id}"