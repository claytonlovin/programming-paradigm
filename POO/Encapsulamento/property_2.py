from datetime import datetime

class Data:
    def __get_data(self):
        return datetime.now().strftime('%d/%m/%Y')


obj = Data()
print(obj.__get_data())
print(obj._Data__get_data())