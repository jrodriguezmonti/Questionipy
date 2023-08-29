class Student:
    def __init__(self, id, name=None, number=None, email=None):
        self.id = id
        self.name = name or f"Student {id + 1}"
        self.number = number or f"ST{id + 1:03}"
        self.email = email or f"student{id + 1}@example.com"

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'number': self.number,
            'email': self.email
        }
