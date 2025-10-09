class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.current_page = {}  # isbn -> page number
