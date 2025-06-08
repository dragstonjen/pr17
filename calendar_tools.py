
from datetime import datetime

class UkrainianCalendar:
    HOLIDAYS = {
        "01-01": "Новий Рік",
        "01-07": "Різдво Христове",
        "03-08": "Міжнародний жіночий день",
        "04-01": "День сміху",
        "05-01": "День праці",
        "05-09": "День Перемоги",
        "06-28": "День Конституції",
        "08-24": "День Незалежності",
        "10-14": "День захисників і захисниць України",
        "12-25": "Різдво (григоріанське)"
    }

    def get_holiday_list(self):
        return list(self.HOLIDAYS.values())

    def is_working_day(self, date):
        if isinstance(date, str):
            date = datetime.strptime(date, "%Y-%m-%d")
        return date.weekday() < 5 and date.strftime("%m-%d") not in self.HOLIDAYS
