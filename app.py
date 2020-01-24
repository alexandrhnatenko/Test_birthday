import json
import sys

HELP = """
Script has 3 arguments to calculating
 First: Number of days per year, type integer, must be greater than zero.
 Second: Number of peoples in the room, type integer, must be greater than one.
 Third: Range of days, type integer, must be greater than zero.
"""
ERROR_MESSAGE = "ERROR: {}"


def calculation(ydays, pcnt, drange):
    res = 1
    for n in range(1, pcnt):
        res *= 1 - ((drange * 2 + 1) * n / ydays)
    res = 1 - res
    return f"{res:5.2}"


def get_and_validate_args():
    year_day_count, response1 = get_year_days_count()
    peoples_count, response2 = get_peoples_count()
    range_count, response3 = get_range_count()
    message = response1 + response2 + response3
    if message:
        message += HELP
    return year_day_count, peoples_count, range_count, message


def get_year_days_count():
    try:
        year_day_count = int(sys.argv[1])
    except IndexError:
        return None, ERROR_MESSAGE.format("\nNot valid arguments count! Cannot get first argument!")
    except ValueError:
        return sys.argv[1], ERROR_MESSAGE.format("\nArguments must be integer!")
    if year_day_count < 1:
        return year_days, ERROR_MESSAGE.format("\nNumber of days per year must be greater than zero")
    return year_day_count, ''


def get_peoples_count():
    try:
        peoples_count = int(sys.argv[2])
    except IndexError:
        return None, ERROR_MESSAGE.format("\nNot valid arguments count! Cannot get second argument!")
    except ValueError:
        return sys.argv[1], ERROR_MESSAGE.format("\nArguments must be integer!")
    if peoples_count < 2:
        return peoples_count, ERROR_MESSAGE.format("\nNumber of peoples in the room must be greater than one")
    return peoples_count, ''


def get_range_count():
    try:
        range_count = int(sys.argv[3])
    except IndexError:
        return None, ERROR_MESSAGE.format("\nNot valid arguments count! Cannot get third argument!")
    except ValueError:
        return sys.argv[1], ERROR_MESSAGE.format("\nArguments must be integer!")
    if range_count < 1:
        return range_count, ERROR_MESSAGE.format("\nRange of days must be greater than zero")
    return range_count, ''


def save_result(ydays, pcnt, drange, result, file_name='result.json'):
    data = {
        'year_days': ydays,
        'peoples': pcnt,
        'day_range': drange,
        'result': result
    }
    with open(file_name, 'w') as file:
        file.write(json.dumps(data))


if __name__ == "__main__":
    year_days, peoples, day_range, result = get_and_validate_args()
    if not result:
        result = calculation(year_days, peoples, day_range)
    print('Number of days per year:', year_days)
    print('Number of peoples in the room:', peoples)
    print('Range of days:', day_range)
    print('Result:', result)
    save_result(year_days, peoples, day_range, result)
