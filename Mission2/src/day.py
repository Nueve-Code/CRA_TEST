from enum import Enum


class Day(Enum):
    MONDAY = 'monday',
    TUESDAY = "tuesday",
    WEDNESDAY = "wednesday",
    THURSDAY = "thursday",
    FRIDAY = "friday",
    SATURDAY = "saturday",
    SUNDAY = "sunday",


def get_day_idx(day):
    return day_properties[day]["day_id"]


def get_point_of_the_day(day):
    return day_properties[day]["point"]


def parsing_days(day):
    if day == 'monday':
        return Day.MONDAY
    elif day == 'tuesday':
        return Day.TUESDAY
    elif day == 'wednesday':
        return Day.WEDNESDAY
    elif day == 'thursday':
        return Day.THURSDAY
    elif day == 'friday':
        return Day.FRIDAY
    elif day == 'saturday':
        return Day.SATURDAY
    elif day == 'sunday':
        return Day.SUNDAY
    else:
        return None


day_properties = {
    Day.MONDAY: {"point": 1, "day_id": 0},
    Day.TUESDAY: {"point": 1, "day_id": 1},
    Day.WEDNESDAY: {"point": 3, "day_id": 2},
    Day.THURSDAY: {"point": 1, "day_id": 3},
    Day.FRIDAY: {"point": 1, "day_id": 4},
    Day.SATURDAY: {"point": 2, "day_id": 5},
    Day.SUNDAY: {"point": 2, "day_id": 6},
}
