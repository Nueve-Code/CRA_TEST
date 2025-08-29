from enum import Enum


class Day(Enum):
    MONDAY = "monday",
    TUESDAY = "tuesday",
    WEDNESDAY = "wednesday",
    THURSDAY = "thursday",
    FRIDAY = "friday",
    SATURDAY = "saturday",
    SUNDAY = "sunday",


day_properties = {
    Day.MONDAY: {"point": 1, "day_id": 0},
    Day.TUESDAY: {"point": 1, "day_id": 1},
    Day.WEDNESDAY: {"point": 3, "day_id": 2},
    Day.THURSDAY: {"point": 1, "day_id": 3},
    Day.FRIDAY: {"point": 1, "day_id": 4},
    Day.SATURDAY: {"point": 2, "day_id": 5},
    Day.SUNDAY: {"point": 2, "day_id": 6},
}
