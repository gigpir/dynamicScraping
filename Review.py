class Review:
    def __init__(self, title, date, text):
        self.title = title
        self.date = date
        self.text = text


    def to_dict(self):
        return {
            'title': self.title,
            'date': self.date,
            'text': self.text
        }