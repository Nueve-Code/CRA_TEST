

import pytest

from Mission2.src.grade.gold import GoldGrade
from Mission2.src.grade.normal import NormalGrade
from Mission2.src.grade.silver import SilverGrade
from Mission2.src.policy.policy_grade_point import GradePointPolicy


@pytest.fixture
def member(mocker):
    member = mocker.Mock()
    return member

def test_get_additional_points(member):
    member.get_weekend_attendance.return_value = 0
    member.get_wednesday_attendance.return_value = 0

    assert GradePointPolicy.get_additional_points(
        member.get_wednesday_attendance(),
        member.get_weekend_attendance()) == 0

def test_get_additional_points_with10(member):
    member.get_weekend_attendance.return_value = 10
    member.get_wednesday_attendance.return_value = 10

    assert GradePointPolicy.get_additional_points(
        member.get_wednesday_attendance(),
        member.get_weekend_attendance()) == 10

def test_remove(member):
    member.grade.get_grade_id.return_value = 0
    member.get_weekend_attendance.return_value = 0
    member.get_wednesday_attendance.return_value = 0

    assert GradePointPolicy.remove_condition(member) == True

def test_dont_remove(member):
    member.grade.get_grade_id.return_value = 1
    member.get_weekend_attendance.return_value = 0
    member.get_wednesday_attendance.return_value = 0

    assert GradePointPolicy.remove_condition(member) == False

def test_get_grade_gold(member):
    assert GradePointPolicy.get_grade_per_standard(50).get_grade_id() == GoldGrade().get_grade_id()

def test_get_grade_silver(member):
    assert GradePointPolicy.get_grade_per_standard(30).get_grade_id() == SilverGrade().get_grade_id()

def test_get_grade_normal(member):
    assert GradePointPolicy.get_grade_per_standard(10).get_grade_id() == NormalGrade().get_grade_id()
