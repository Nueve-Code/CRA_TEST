import pytest

from Mission2.src.grade.gold import GoldGrade
from Mission2.src.member import Member
from Mission2.src.day import Day, get_day_idx
from Mission2.src.attendance import init_member_data
import Mission2.src.attendance

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

    assert member.name == member_name
    assert member.id == member_id


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
    Mission2.src.attendance.member_list = {}
    test_member = "test"
    test_day = 'monday'

    init_member_data(member_name=test_member, day=test_day)

    m = Mission2.src.attendance.member_list[test_member]
    assert m.name == test_member
    assert m.points == 1
    assert m.attendance[get_day_idx(Day.MONDAY)] == 1
    assert m.grade.get_str() == "NORMAL"


def test_init_members_with_weekend():
    Mission2.src.attendance.member_list = {}
    test_member = "test"
    test_day = 'saturday'

    init_member_data(member_name=test_member, day=test_day)

    m = Mission2.src.attendance.member_list[test_member]
    assert m.get_weekend_attendance() == 1


def test_init_members_with_weekends():
    Mission2.src.attendance.member_list = {}
    test_member = "test2"
    test_data = [(test_member, 'saturday'), (test_member, 'sunday')]

    for data in test_data:
        init_member_data(member_name=data[0], day=data[1])

    m = Mission2.src.attendance.member_list[test_data[0][0]]
    assert m.get_weekend_attendance() == 2

def test_init_members_with_wen():
    Mission2.src.attendance.member_list = {}
    test_member = "test"
    test_day = 'wednesday'

    init_member_data(member_name=test_member, day=test_day)

    m = Mission2.src.attendance.member_list[test_member]
    assert m.get_wednesday_attendance() == 1


def test_get_grade():
    Mission2.src.attendance.member_list = {}
    test_member = "test"
    test_day = 'wednesday'
    test_grade = GoldGrade()
    init_member_data(member_name=test_member, day=test_day)

    m = Mission2.src.attendance.member_list[test_member]
    m.grade = test_grade

    assert m.grade == test_grade
