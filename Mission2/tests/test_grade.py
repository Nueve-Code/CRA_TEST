import pytest

from Mission2.src.grade.gold import GoldGrade
from Mission2.src.grade.normal import NormalGrade
from Mission2.src.grade.silver import SilverGrade


@pytest.mark.parametrize("grade, point, grade_str, id", [
    (GoldGrade(), 50, "GOLD", 2),
    (SilverGrade(), 30, "SILVER", 1),
    (NormalGrade(), 0, "NORMAL", 0),
])
def test_grade(grade, point, grade_str, id):
    assert grade.standard == point
    assert grade.get_str() == grade_str
    assert grade.get_grade_id() == id
