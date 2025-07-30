class Song:
    """Class to represent a song
    
    Attributes:
        title, artist, duration(optional)"""

    def __init__(self, title, artist, duration=0):
        """Song init method
        Args:
            title(str): initializes the 'title' attribute
            artist (Artist): Add Artist object representing the song's creator
            duration(optional[int]): Initial value for the duration value,
                will default to 0 if not specified."""
        self.name = title
        self.artist = artist
        self.duration = duration


class Album:
    """Class to represent an album, using its track list

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
        self.year = year
        if artist is None:
            self.artist = "Various Artists"
        else:
            self.artist = artist
        self.tracks = []

    def addSong(self, song, position=None):
        """Adds a song to the track list

        Args:
            song (Song)
            position (optional[int])
            """
        songFound = findObject(song, self.tracks)
        if songFound is None:
            songFound = Song(song, self.artist)
            if position is None:
                self.tracks.append(songFound)
            else:
                self.tracks.insert(position, songFound)


class Artist:
    """Basic artist class to store their details"""
    def __init__(self, name):
        self.name = name
        self.albums = []

    def addAlbum(self, album):
        """adds a new album to the list"""
        self.albums.append(album)

    def addSong(self, name, year, title):
        '''Add song to collection on albums'''

        albumFound = findObject(name, self.albums)
        if albumFound is None:
            print(name + " not found")
            albumFound = Album(name, year, self.name)
            self.addAlbum(albumFound)
        else:
            print("Found album " + name)

        albumFound.addSong(title)

def findObject(field, objectList):
    """Check 'objectList' to see if an object with a 'name' attribute to 'field' exists,
    return it if so."""
    for item in objectList:
        if item.name == field:
            return item
    return None


def loadData():
    artistList = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            #A row should be (artist, album, year, song)
            artistField, albumField, yearField, songField = tuple((line.strip("\n").split("\t")))
            yearField = int(yearField)
            print("{}:{}:{}:{}".format(artistField, albumField, yearField, songField))

            newArtist = findObject(artistField, artistList)
            if newArtist is None:
                newArtist = Artist(artistField)
                artistList.append(newArtist)

            newArtist.addSong(albumField, yearField, songField)

    return artistList


if __name__ == "__main__":
    artists = loadData()
    print("There are {} artists.".format(len(artists)))





















