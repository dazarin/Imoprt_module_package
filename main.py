from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime, date, time
from bs4 import BeautifulSoup

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print(f'Текущая дата:\n{datetime.date(datetime.now())}')

