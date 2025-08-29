import pytest

from Mission2.src.attendance import get_day_idx, get_point_of_the_day
from Mission2.src.day import Day, day_properties


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
