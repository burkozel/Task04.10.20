class Track:
    def __init__(self, name, duration):
        self.name = name
        self.duration = float(duration)

    def show(self):

        for tracks in tracks_library:
            input_ = input()
            if input_ in tracks_library:
                print(f"<{tracks.name} - {tracks.duration}>")

tracks_library = []
def get_library():
    tracks_library.append(Track("Серпантин", 3.07))
    tracks_library.append(Track("Компас", 3.04))
    tracks_library.append(Track("B.I.D", 3.13))
    tracks_library.append(Track("Кино", 3.05))
    tracks_library.append(Track("77", 2.03))
    tracks_library.append(Track("Бенз", 2.13))

class Album:
    def __init__(self, gname, album):
        self.gname = gname
        self.album = album

    def get_tracks(self):
        for tracks in tracks_library:
            print(f"<{tracks.name} - {tracks.duration}>")

    def add_track(self):
        new_name = input("Введите название трека ")
        new_duration =  float(input("Введите продолжительнсть трека "))
        tracks_library.append(Track(new_name, new_duration))

    def get_duration(self):
        album_input = input()
        if album_input == "Great_depression":
            sum_ = 0
            for tracks in Great_depression:
                sum_ = sum_ + tracks[1]
        if album_input == "Favorites":
            sum_ = 0
            for tracks in Favorites:
                sum_ = sum_ + tracks[1]


Great_depression = []
Favorites = []
def add_tracks():
    Great_depression.append(Track("Серпантин", 3.07))
    Great_depression.append(Track("Компас", 3.04))
    Great_depression.append(Track("B.I.D", 3.13))
    Favorites.append(Track("Кино", 3.05))
    Favorites.append(Track("77", 2.03))
    Favorites.append(Track("Бенз", 2.13))




