class Review:
    def __init__(self, title, date, text, rating, name, origin,contributions):
        self.title = title
        self.date = date
        self.text = text
        self.rating = rating
        self.name = name
        self.origin = origin
        self.contributions = contributions
    def to_dict(self):
        return {
            'rating': self.rating,
            'date': self.date,
            'title': self.title,
            'origin': self.origin,
            'name': self.name,
            'contributions': self.contributions,
            'text': self.text,
        }