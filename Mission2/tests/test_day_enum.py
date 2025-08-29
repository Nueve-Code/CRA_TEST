import pytest

from Mission2.src.day import Day, day_properties, parsing_days


@pytest.mark.parametrize(
    "day, day_id, point",
    (
        (Day.MONDAY, 0, 1),
        (Day.TUESDAY, 1, 1),
        (Day.WEDNESDAY, 2, 3),
        (Day.THURSDAY, 3, 1),
        (Day.FRIDAY, 4, 1),
        (Day.SATURDAY, 5, 2),
        (Day.SUNDAY, 6, 2),
    )
)
def test_day_properties(day, day_id, point):
    assert day_properties[day]["point"] == point
    assert day_properties[day]["day_id"] == day_id

@pytest.mark.parametrize(
    "day, day_string",
    (
        (Day.MONDAY, 'monday'),
        (Day.TUESDAY, 'tuesday'),
        (Day.WEDNESDAY, 'wednesday'),
        (Day.THURSDAY, 'thursday'),
        (Day.FRIDAY, 'friday'),
        (Day.SATURDAY, 'saturday'),
        (Day.SUNDAY, 'sunday'),
        (None, 'invalid'),
    )
)
def test_parsing_days(day, day_string):
    assert parsing_days(day_string) == day