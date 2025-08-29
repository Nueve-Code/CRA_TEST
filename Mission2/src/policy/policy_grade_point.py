from Mission2.src.grade.gold import GoldGrade
from Mission2.src.grade.normal import NormalGrade
from Mission2.src.grade.silver import SilverGrade
from Mission1.attendance import get_day_idx
from Mission2.src.day import Day, day_properties

SILVER_GRADE_ID = 1
GOLD_GRADE_ID = 2
GOLD_GRADE_POINT = 50
SILVER_GRADE_POINT = 30


class GradePointPolicy:

    @staticmethod
    def remove_condition(member):
        if (member.grade.get_grade_id() not in (GOLD_GRADE_ID, SILVER_GRADE_ID)
                and member.get_wednesday_attendance() == 0
                and member.get_weekend_attendance() == 0):
            return True

        return False

    @staticmethod
    def get_grade_per_standard(point):
        if point >= GOLD_GRADE_POINT:
            return GoldGrade()
        elif point >= SILVER_GRADE_POINT:
            return SilverGrade()
        else:
            return NormalGrade()

    @staticmethod
    def get_additional_points(wednesday_attendance_count, weekend_attendance_count):
        return 10 if (wednesday_attendance_count > 9) or (weekend_attendance_count > 9) else 0

