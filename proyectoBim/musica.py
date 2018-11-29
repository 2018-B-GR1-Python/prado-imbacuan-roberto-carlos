import archivos
import pandas as pd


class Artist:

    artist_id = None
    artist_hotttnesss = 0
    artist_name = None

    def __init__(self, id):
        self.artist_id = id

    def buscar(self):
        artistas = archivos.leer_json("./data/artists.json")
        for persona in artistas:
            if (persona['artist_id'] == self.artist_id):
                self.artist_name = persona["artist_name"]
                self.artist_hotttnesss = persona["artist_hotttnesss"]


class Cancion:

    artist_id = None
    artist_hotttnesss = 0
    artist_name = None
    duration = 0
    familiarity = 0
    location = None
    latitude = 0
    longitude = 0
    loudness = 0
    similar = None
    song_hotttnesss = 0
    song_id = None
    tempo = 0
    terms = None
    title = None
    year = 0

    def filtrar(self):
        f = pd.read_csv("./data/music.csv")
        keep_col = ['artist.hotttnesss', 'artist.id', 'artist.name', 'duration', 'familiarity', 'latitude', 'location', 'longitude', 'loudness', 'similar', 'song.hotttnesss', 'song.id', 'tempo', 'terms', 'title', 'year']
        new_f = f[keep_col]
        new_f.to_csv("./data/musicre.csv", index=False)

    def crear(self):
        df = pd.read_csv('./data/musicre.csv')
        df = df.append(vars(self), ignore_index=True)
        df.to_csv('./data/musicre.csv', index=False)

    def buscar(self, id):
        df = pd.read_csv('./data/musicre.csv')
        indexes = df['song_id'] == id
        print(df[indexes])

    def listar(self, llave, ascendente):
        df = pd.read_csv('./data/musicre.csv')
        if (llave != None):
            df = df.sort_values(llave, ascending=ascendente)
        print(df)

    def checkIfExists(self, id):
        df = pd.read_csv('./data/musicre.csv')
        indexes = df['song_id'] == id
        return True if len(df[indexes].index) == 1 else False

    def leer(self, id):
        df = pd.read_csv('./data/musicre.csv')
        if self.checkIfExists(id):
            indexes = df['song_id'] == id
            items = df[indexes]
            return items.iloc[0]
        else:
            return pd.Series([])

    def actualizar(self, serie):
        df = pd.read_csv('./data/musicre.csv')
        df.iloc[serie.name] = serie
        df.to_csv('./data/musicre.csv', index=False)

    def eliminar(self, id):
        print('delete')
        if self.checkIfExists(id):
            df = pd.read_csv('./data/musicre.csv')
            df = df.drop(df[df.song_id == id].index)
            df.to_csv('./data/musicre.csv', index=False)
        else:
            print('Registro no existe')
