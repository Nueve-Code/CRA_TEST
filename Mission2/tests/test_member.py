import pytest

from Mission2.src.attendance import *
from Mission2.src.member import Member
from Mission2.src.day import Day


@pytest.mark.parametrize(
    ("member_name", "member_id"),
    [
        ("test", 0),
        ("a", 1),
        ("b", 2),
        ("c", 3),
    ]
)
def test_member_properties(member_name, member_id):
    member = Member(member_name, member_id)

    assert member._member_name == member_name
    assert member._member_id == member_id


@pytest.mark.parametrize(
    "day", [0, 1, 2, 3, 4, 5, 6]
)
def test_member_attendance_single_day(day):
    member = Member("test", 0)

    member.check_attendance(day)

    assert member._attendance_of_the_week[day] == 1


@pytest.mark.parametrize(
    "point", [0, 1, 2, 3, 4, 5, 6]
)
def test_member_point(point):
    member = Member("test", 0)

    member.add_points(point)

    assert member.points == point

def test_init_members():
    from Mission2.src.attendance import init_member_data
    test_member = "test"
    test_day = 'monday'

    init_member_data(member_name=test_member, day=test_day)

    m = member_list[test_member]
    assert m.id == 1
    assert m.name == test_member
    assert m.points == 1
    assert m.attendance[get_day_idx(Day.MONDAY)] == 1
    assert m.grade.get_str() == "NORMAL"
