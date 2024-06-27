# Реализуйте класс Date, который должен:
#
# проверять числа даты на корректность;
# конвертировать строку даты в объект класса Date, состоящий из соответствующих числовых значений дня, месяца и года.
# Оба метода должны получать на вход строку вида ‘dd-mm-yyyy’.
#
# При тестировании программы объект класса Date должен инициализироваться исключительно через метод конвертации,
# например:
#
# date = Date.from_string('10-12-2077')
# Неверный вариант: date = Date(10, 12, 2077)
#
# Пример основного кода:
#
# date = Date.from_string('10-12-2077')
# print(date)
# print(Date.is_date_valid('10-12-2077'))
# print(Date.is_date_valid('40-12-2077'))
# Результат:
# День: 10    Месяц: 12    Год: 2077
# True
# False
import datetime


class Date:

    @classmethod
    def from_string(cls, string):
        day = string[:2]
        month = string[3:5]
        year = string[6:]
        return f"День: {day}\t Месяц: {month}\t Год: {year}"

    @classmethod
    def is_date_valid(cls, string):
        try:
            datetime.datetime.strptime(string, "%d-%m-%Y")
        except Exception:
            return False
        return True
        # day = int(string[:2])
        # month = int(string[3:5])
        # # year = string[6:]
        # # if (month in [int('01'), int('03'), int('05'), int('07'), int('08'), 10, 12] and day == 31)\
        # #         or (month in [int('04'), int('06'), int('09'), 11] and day == 30)\
        # #         or (month == int('02') and day in [28, 29]):
        # #     return True
        # if (month in [1, 3, 5, 7, 8, 10, 12] and 0 < day <= 31)\
        #         or (month in [4, 6, 9, 11] and 0 < day <= 30)\
        #         or (month == 2 and day in [28, 29]):
        #     return True
        # else:
        #     return False


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
