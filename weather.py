
from random import uniform
from datetime import datetime, timedelta


class Weather:
    def __init__(self, device: str = "", location: str = "",
                 time: str = "", temp: float = 0,
                 humidity: float = 0, pressure: float = 0,
                 id=None) -> None:
        if not id == None:
            self.id = id
        self.Device: str = device
        self.Location: str = location
        self.Time: str = time
        self.Temp: float = temp
        self.Humidity: float = humidity
        self.Pressure: float = pressure

    @classmethod
    def from_dictionary(cls, wdict: dict):
        if "id" in wdict.keys():
            return cls(wdict["Device"], wdict["Location"],
                       wdict["Time"], wdict["Temp"],
                       wdict["Humidity"], wdict["Pressure"],
                       wdict["id"])
        else:
            return cls(wdict["Device"], wdict["Location"],
                       wdict["Time"], wdict["Temp"],
                       wdict["Humidity"], wdict["Pressure"])

    def to_list(self) -> list:
        adict = self.__dict__
        return [adict[key] for key in Weather.static_keys()]

    num_of_random = 0

    @staticmethod
    def randomize():
        Weather.num_of_random += 1
        tdelta = timedelta(hours=Weather.num_of_random)
        dtime = datetime(2020, 2, 14)+tdelta
        return Weather("Random Device",
                       "60.65661396854781, 15.337069653989222",
                       str(dtime),
                       round(uniform(-10.0, 20.0), 1),
                       round(uniform(5.0, 99.0), 1),
                       round(uniform(1025.0, 1090.0), 2)
                       )

    @staticmethod
    def generate_randomlist(items: int = 50) -> list:
        return [Weather.randomize() for i in range(items)]

    @staticmethod
    def static_keys() -> list[str]:
        return ["Device", "Location",
                "Time", "Temp",
                "Humidity", "Pressure"]

    def keys(self) -> list[str]:
        return self.__dict__.keys()

    def __str__(self) -> str:
        return "Weather: "+str(self.__dict__)


if __name__ == "__main__":

    # testing things goes here

    # a=Weather.randomize()
    # b=Weather.randomize()

    # w=Weather()
    # wdict=w.__dict__
    # print(wdict)
    # print(a.__dict__)
    # print(b.__dict__)

    # c=Weather.randomize()
    # c_dict=c.__dict__.copy()
    # c_dict["id"]=100
    # print(c_dict)
    # print(Weather.from_dictionary(c_dict))
    # print(c)

    # print(Weather.generate_randomlist())
    pass
