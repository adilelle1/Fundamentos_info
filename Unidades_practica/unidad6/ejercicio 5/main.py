from netflix import Productions

movie = 'Movie'
serie = 'Serie'
action = 'Action'
anime = 'Anime'
comedy = 'Comedy'
documentary = 'Documentary'
scifi = 'Science fiction '
romance = 'Romance'

star_wars1 = Productions(movie,
                         scifi,
                         'Star Wars Episode 1: The Phantom Menace',
                         'Two Jedi escape a hostile blockade to find allies and come across a young boy who may bring '
                         'balance to the Force, but the long dormant Sith resurface to claim their original glory.',
                         '12/06/2019',
                         'George Lucas',
                         '13+')
star_wars1.serie_or_movie(None, '2h 16m')

stranger_things = Productions(serie,
                              scifi,
                              'Stranger Things: episode 1',
                              'Kids playing with monsters',
                              '12/06/2019',
                              'Matt Duffer and Ross Duffer', '13+')
stranger_things.serie_or_movie('3', None)

print(stranger_things)
