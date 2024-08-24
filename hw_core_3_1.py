from datetime import date, datetime

def validate_date_format(date):
    try:
        date_str = bool(datetime.strptime(date, "%Y-%m-%d"))
    except ValueError:
        date_str = False

    return date_str

def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y-%m-%d").date()

def get_days_from_today(date_input):
    today_date = date.today()

    if(validate_date_format(date_input)):
        return (today_date - string_to_date(date_input)).days
    else:
        return 'incorrect date value, format must be: YYYY-MM-DD'

print(get_days_from_today('2022-03-30'))