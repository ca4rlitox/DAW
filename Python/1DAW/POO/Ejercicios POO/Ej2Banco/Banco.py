class Banco:
    def __init__(self, direccion, provincia, codigo):
        self.direccion = direccion
        self.provincia = provincia
        self.cod = codigo

    def verDatos(self):
        print(f"Direccion: {self.direccion}, provincia: {self.provincia}, código: {self.cod}")
    @property
    def verSucursal(self):
        return self.cod