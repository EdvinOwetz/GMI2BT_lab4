
import sqlite3

#Reference
#https://www.sqlitetutorial.net/sqlite-python/create-tables/

class WeatherDatabase:
    def __init__(self,dbfilepath:str) -> None:
        self.database_filepath=dbfilepath
    
    
    def create_db_connection(self):
        try:
            self.connection=sqlite3.connect(self.database_filepath)
            print("Databas ansluten\nSQLite3 version:"+sqlite3.version)
        except sqlite3.Error as e:
            print("Error: Kunde inte anslutning till databasen.")
            print(e)
        finally:
            if self.connection:
                self.connection.close()
    
    def __del__(self):
        if self.connection:
                self.connection.close()
    
    
    
    def get_weather_data(self)->list:
        return []