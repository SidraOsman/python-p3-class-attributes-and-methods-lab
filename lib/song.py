class Song:
    genres = []
    artists = []
    count = 0
    artist_count={}
    genre_count = {}

    # GENRES = ["Rap", "Pop"]
    # ARTISTS = ["Jay-Z", "Drake", "Beyonce"]
    
    def __init__(self,name,artist,genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_artist_count(artist)
        self.add_to_genre_count(genre)

    @classmethod
    def add_song_to_count(cls,increment=1):
        cls.count += increment

    @classmethod
    def add_to_genres(cls,genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls,artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_artist_count(cls,artist):
        if cls.artist_count.get(artist):
            cls.artist_count[artist]+=1
        else:
            cls.artist_count[artist] = 1

    @classmethod
    def add_to_genre_count(cls,genre):
        if cls.genre_count.get(genre):
            cls.genre_count[genre]+=1
        else:
            cls.genre_count[genre] = 1


ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
ninety_nine_problems.name
ninety_nine_problems.artist
ninety_nine_problems.genre
Song.genre_count
Song.artist_count