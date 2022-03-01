
import sqlite3
from pathlib import Path
from weather import Weather

from random_weather import generate_weather_data

# Reference
# https://www.sqlitetutorial.net/sqlite-python/create-tables/


class Database:
    def __init__(self, dbfile: str = "database.db", table_name: str = "default_table") -> None:
        self.dbfile = dbfile
        self.table_name = table_name

    def connect(self) -> sqlite3.Connection:
        try:
            con = sqlite3.connect(self.dbfile)
            # print("Databas \""+self.dbfilepath+"\"" ansluten\nSQLite3 version:"+sqlite3.version)
            return con
        except sqlite3.Error as e:
            print("Error: Kunde inte anslutning till databasen.")
            print(e)

    # private methods

    def _create_table(self, sql: str = None) -> None:
        if sql == None:
            sql = f""" CREATE TABLE IF NOT EXISTS {self.table_name}( test TEXT ); """
        self._db_commit(sql)

    def _get_tabledata(self) -> list:
        sql = f"""SELECT * FROM {self.table_name};"""
        res: list = self._db_fetchall(sql)
        return res

    def _dbfile_exists(self) -> bool:
        return Path(self.dbfile).is_file()

    def _tabel_exists(self) -> bool:
        sql = f""" SELECT name FROM sqlite_master WHERE type='table' AND name='{self.table_name}'; """
        res: list = self._db_fetchall(sql)
        if len(res) == 0:
            return False
        else:
            return True

    def _db_fetchall(self, sql: str) -> list:
        res: list = []
        with self.connect() as con:
            cur = con.cursor()
            cur.execute(sql)
            res = cur.fetchall()
        return res

    def _db_commit(self, sql: str) -> None:
        with self.connect() as con:
            cur = con.cursor()
            cur.execute(sql)
            con.commit()

    def _db_insert(self, sql: str, data: list) -> None:
        with self.connect() as con:
            cur = con.cursor()
            cur.execute(sql, data)
            con.commit()

    def _db_insert_list(self, sql: str, data: list[list]) -> None:
        with self.connect() as con:
            cur = con.cursor()
            for item in data:
                cur.execute(sql, item)
            con.commit()


class WeatherDatabase(Database):
    def __init__(self, dbfile: str = "weather.db", table_name: str = "SensorData") -> None:
        super().__init__(dbfile, table_name)
        self.setup()

    def setup(self) -> None:
        sql = """ CREATE TABLE IF NOT EXISTS SensorData (
                            id INTEGER PRIMARY KEY,
                            device VARCHAR(30) NOT NULL,
                            location VARCHAR(60) NOT NULL,
                            time TEXT NOT NULL,
                            temp FLOAT NOT NULL,
                            humidity FLOAT NOT NULL,
                            pressure FLOAT NOT NULL
                        ); """
        if self._dbfile_exists():
            if not self._tabel_exists():
                self._create_table(sql)
                self.fill_table()
        else:
            self._create_table(sql)
            self.fill_table()

    def fill_table(self) -> None:
        data: list[Weather] = Weather.generate_randomlist()
        lista: list[list] = [item.to_list() for item in data]
        sql: str = """ INSERT INTO SensorData(device,location,time,temp,humidity,pressure) 
        VALUES(?,?,?,?,?,?)"""
        self._db_insert_list(sql, lista)

    def get_tabledata(self) -> list[Weather]:
        keys: list[str] = Weather.static_keys()
        keys.insert(0, "id")
        data = self._get_tabledata()
        wlist: list[Weather] = []
        for item in data:
            adict = {}
            for i in range(len(keys)):
                adict[keys[i]] = item[i]
            wlist.append(Weather.from_dictionary(adict))
        return wlist


if __name__ == "__main__":

    # testing things goes here
    d = WeatherDatabase()
    print([item.__dict__ for item in d.get_tabledata()])
