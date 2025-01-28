from data.modelo.artistas import Artista

class DaoArtistas:
    def get_all(self,db) -> list[Artista]:
        cursor = db.cursor()

        cursor.execute("SELECT * FROM artistas")

        equipos_en_db = cursor.fetchall()
        equipos : list[Artista]=list()
        for equipo in equipos_en_db:
            artista = Artista(equipo[0], equipo[1])
            equipos.append(artista)
        cursor.close()

        return equipos
    
    def insert(self, db, nombre : str):
        cursor = db.cursor()
        sql = ("INSERT INTO artistas (nombre) values (%s)")
        data = (nombre,)
        cursor.execute(sql, data)
        db.commit()
        cursor.close()

    def delete(self, db, id : int):
        cursor = db.cursor()
        sql = ("DELETE FROM artistas where id = (%s)")
        data = (id,)
        cursor.execute(sql,data)
        db.commit()
        cursor.close()
