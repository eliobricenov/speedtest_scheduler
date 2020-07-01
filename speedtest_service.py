from tinydb import TinyDB, Query
import datetime


class SpeedtestService:
    db = None
    STORAGE_NAME = 'db.json'

    def __init__(self):
        if self.db is None:
            self.db = TinyDB(self.STORAGE_NAME)

    def all(self):
        return self.db.all()

    def today_test(self):
        date = datetime.datetime.now().date().__str__()
        test = Query()
        return self.db.search(test.date == date)

    def create(self, result):
        date_time_object = datetime.datetime.now()
        date = date_time_object.date().__str__()
        time = date_time_object.time().__str__()
        return self.db.insert({'result': result, 'date': date, 'time': time})
