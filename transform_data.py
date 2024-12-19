class TransformData:
    def __init__(self, data):
        self.data = data
        self.extracted_data = self.bonus_increment()

    def bonus_increment(self):
        self.data['salary'] = self.data['salary'] * 1.1
        return self.data
