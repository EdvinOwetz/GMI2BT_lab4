
import sqlite3

from random_weather import generate_weather_data

# Reference
# https://www.sqlitetutorial.net/sqlite-python/create-tables/


class WeatherDatabase:
    def __init__(self, dbfilepath:str = "w.db") -> None:
        self.database_filepath = dbfilepath
        self.create_db_connection()
        

    def create_db_connection(self):
        try:
            self.connection = sqlite3.connect(self.database_filepath)
            return True
            print("Databas ansluten\nSQLite3 version:"+sqlite3.version)
        except sqlite3.Error as e:
            print("Error: Kunde inte anslutning till databasen.")
            print(e)
            return False
    
    def create_table(self):
        # if(not self.create_db_connection()):
        #     return
        cursor=self.connection.cursor()
        tablesqltext=""" CREATE TABLE IF NOT EXISTS SensorData (
                            id INTEGER PRIMARY KEY,
                            device VARCHAR(30) NOT NULL,
                            location VARCHAR(60) NOT NULL,
                            time VARCHAR(30) NOT NULL,
                            temp FLOAT NOT NULL,
                            humidity FLOAT NOT NULL,
                            pressure FLOAT NOT NULL
                        ); """
        try:
            cursor.execute(tablesqltext)
        except sqlite3.Error as e:
            print(e)
    
    def fill_table(self):
        sql_insert=""" INSERT INTO SensorData(device,location,time,temp,humidity,pressure) 
        VALUES(?,?,?,?,?,?)"""
        
        rand_w=[(item["Device"],
                 item["Location"],
                 item["Time"],
                 item["Temp"],
                 item["Humidity"],
                 item["Pressure"]) for item in generate_weather_data()]
        cursor=self.connection.cursor()
        for data in rand_w:
            cursor.execute(sql_insert,data)
            self.connection.commit()
    
    def get_table(self):
        sql_text_headers="""as"""
        sql_text="""SELECT * FROM SensorData;"""
        cursor=self.connection.cursor()
        cursor.execute(sql_text)
        headers=cursor.fetchall()
        cursor.execute(sql_text)
        rows=cursor.fetchall()
        lista=[]
        keys=["id",
                 "Device",
                 "Location",
                 "Time",
                 "Temp",
                 "Humidity",
                 "Pressure"]
        for item in rows:
            newdict={}
            for i in range(len(keys)):
                newdict[keys[i]]=item[i]
            lista.append(newdict)
        return lista

    def get_weather_data(self) -> list:
        return []

# wdb=WeatherDatabase()
# wdb.create_table()
# wdb.fill_table()
# wdb.connection.close()