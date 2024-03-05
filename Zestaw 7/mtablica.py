import numpy as np

class MonitorowanaTablica:

    def __init__(self, od=0, do=1000, elem=50, tryb="R"):
        np.random.seed(0)
        if tryb=="R":
            self.tablica = np.linspace(od, do, elem, dtype=np.int64)
            np.random.shuffle(self.tablica)
        elif tryb=="S":
            self.tablica = np.linspace(od, do, elem, dtype=np.int64)
        elif tryb=="A":
            self.tablica = np.linspace(do, od, elem, dtype=np.int64)
        elif tryb=="T":
            __tablica = np.linspace(od, (do-od)//3, elem//3, dtype=np.int64)
            self.tablica = np.concatenate((__tablica,__tablica,__tablica))
        elif tryb=="basic":
            self.tablica = np.empty(dtype=np.int64, shape=elem)
        self.reset()

    def reset(self):
        self.indeksy = []
        self.wartosci = []
        self.typ_dostepu = []
        self.pelne_kopie = []

    def sledzenie(self, key, typ_dostepu):
        self.indeksy.append(key)
        self.wartosci.append(self.tablica[key])
        self.typ_dostepu.append(typ_dostepu)
        self.pelne_kopie.append(np.copy(self.tablica))

    def aktywnosc(self, idx=None):
        if isinstance(idx, type(None)):
            return [(i, op) for (i, op) in zip(self.indeksy, self.typ_dostepu)]
        else:
            return (self.indeksy[idx], self.typ_dostepu[idx])

    def __getitem__(self, key):
        self.sledzenie(key, "get")
        return self.tablica.__getitem__(key)

    def __setitem__(self, key, value):
        self.tablica.__setitem__(key, value)
        self.sledzenie(key, "set")

    def __len__(self):
        return self.tablica.__len__()

    def podmien_tablice(self, nowa_tablica):
        if isinstance(nowa_tablica, np.ndarray):
            if nowa_tablica.shape == self.tablica.shape:
                self.tablica = nowa_tablica.copy()
                self.reset()  # Resetowanie śledzenia dla nowej tablicy
            else:
                raise ValueError("Nowa tablica ma inne wymiary niż oryginalna tablica")
        else:
            raise ValueError("Podana wartość nie jest tablicą NumPy")

    def set_tablica(self, new_tablica):
        if isinstance(new_tablica, np.ndarray) and new_tablica.shape == self.tablica.shape:
            self.tablica = new_tablica.copy()
        else:
            raise ValueError("Nowa tablica ma nieprawidłowy rozmiar lub nie jest tablicą NumPy")


