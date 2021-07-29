import shelve

class Save:
    def __init__(self):
        self.file = shelve.open('data')
        self.info = {
            'name': 'Kanye',
            'age': 24,
            'state': 0
        }
    def save(self):
        self.file['Info'] = self.info
        self.file['Number'] = 42

    def get(self):
        num = self.file('Number')
        print(num)
        print(self.file['Info'])

    def __del__(self):
        self.file.close()