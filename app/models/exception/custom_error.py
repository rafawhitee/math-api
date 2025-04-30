from datetime import datetime

class CustomError:
    def __init__(self, message: str):
        self.message = message
        self.date = datetime.now().isoformat()

    def to_dict(self):
        return vars(self)
    
    def __getitem__(self, key):
        return getattr(self, key)
    
    def __setitem__(self, key, value):
        setattr(self, key, value)
    
    def __repr__(self):
        return f"<CustomError(message='{self.message}')>"