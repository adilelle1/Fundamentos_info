class Productions:

    def __init__(self, type, category, name, description, date_published, director, rating):
        self.type = type
        self.category = category
        self.name = name
        self.description = description
        self.date_published = date_published
        self.director = director
        self.rating = rating
        self.seasons = None
        self.run_time = None

    def serie_or_movie(self, seasons, run_time):
        if self.type == 'Serie':
            self.seasons = seasons
        elif self.type == 'Movie':
            self.run_time = run_time

    def __str__(self):
        print(f'Name: {self.name}')
        print(f'Director: {self.director}')
        print(f'Type: {self.type}')
        print(f'Category: {self.category}')
        print(f'Description: {self.description}')
        print(f'Date published: {self.date_published}')
        print(f'Rating: {self.description}')

        if self.type == 'Serie':
            print('Seasons: {self.seasons}')
        elif self.type == 'Movie':
            print(f'Run time: {self.run_time}')
