class Track:
    def __init__(self, name, duration):
        self.name = name
        self.duration = float(duration)

    def show(self):
        return f"<{self.name} - {self.duration}>"


tracks_library = []


def track_library():
    tracks_library.append(Track("Серпантин", 3.07))
    tracks_library.append(Track("Компас", 3.04))
    tracks_library.append(Track("Dark Light", 3.27))


def album():
    Great_depression = [Track("Серпантин", 3.07), Track("Компас", 3.04)]
    Concept_Vague = [Track("Dark Light", 3.27)]


class Album(Track):
    def __init__(self, gname, album):
        self.gname = gname
        self.album = album

    def get_tracks(self):
        return f"<{self.name} - {self.duration}>"

    def add_tracks(self):
        new_name = input("Введите название нового трека ")
        new_dur = input("Введите длительность нового трека ")
        tracks_library.append(Track(new_name, new_dur))
        return "Track added"

    def get_duration(self):
        for tracks in tracks_library: