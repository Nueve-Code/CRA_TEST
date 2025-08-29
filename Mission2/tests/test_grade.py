import pytest

from Mission2.src.grade.gold import GoldGrade
from Mission2.src.grade.normal import NormalGrade
from Mission2.src.grade.silver import SilverGrade


@pytest.mark.parametrize("grade, point, grade_str", [
    (GoldGrade(), 50, "GOLD"),
    (SilverGrade(), 30, "SILVER"),
    (NormalGrade(), 0, "NORMAL"),
])
def test_grade(grade, point, grade_str):
    assert grade.standard == point
    assert grade.get_str() == grade_str