class Song:
    """Class to represent a song
    
    Attributes:
        title, artist, duration(optional)"""

    def __init__(self, title, artist, duration):
        """Song init method
        Args:
            title(str): initializes the 'title' attribute
            artist (Artist): Add Artist object representing the song's creator
            duration(optional[int]): Initial value for the duration value,
                will default to 0 if not specified."""
        self.title = title
        self.artist = artist
        self.duration = duration


class Album:
    """Class to represent an album, using its track lsit

    Attributes:
        name (str)
        year (int)
        artist (Artist)
        tracks (List[Song})

    Methods:
        addSong:
        """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.yesr = year
        if artist is None:
            self.artist = Artist.__name__ = ("Various Artists")
        else:
            self.artist = artist
        self.tracks = []

    def addSong(self, song, position=None):
        """Adds a song to the track list

        Args:
            song (Song)
            position (optional[int])
            """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


class Artist:
    """Basic artist class to store their details"""

    def __int__(self, name):
        self.name = name
        self.albums = []

    def addAlbum(self, album):
        """adds a new album to the list"""
        self.albums.append(album)


def loadData():
    newArtist = None
    newAlbum = None
    artistList = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            #A row should be (artist, album, year, song)
            artistField, albumField, yearField, songField = tuple((line.strip("\n").split("\t")))
            yearField = int(yearField)
            print("{}:{}:{}:{}".format(artistField, albumField, yearField, songField))

            if newArtist is None:
                newArtist = Artist.__name__ = artistField
            elif newArtist.name != artistField:     # Idk what the hell is going on here
                newArtist.addAlbum(newAlbum)
                artistList.append(artistField)
                newArtist = Artist.__name__ = artistField
                newAlbum = None

            if newAlbum is None:
                newAlbum = Album(albumField, yearField, newArtist)
            elif newAlbum.name != albumField:
                newArtist.addAlbum(newAlbum)
                newAlbum = Album(albumField, yearField, newArtist)

            newSong = Song(songField, newArtist, 0)
            newAlbum.addSong(newSong)

        if newArtist is not None:
            if newAlbum is not None:
                newArtist.addAlbum(newAlbum)
            artistList.append(newArtist)

    return artistList


if __name__ == "__main__":
    artists = loadData()
    print("There are {} artists.".format(len(artists)))





















