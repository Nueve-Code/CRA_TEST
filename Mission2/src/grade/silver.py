from Mission2.src.grade.grade_interface import GradeInterface


class SilverGrade(GradeInterface):
    SILVER_GRADE_POINT = 30

    def __init__(self):
        super().__init__(self.SILVER_GRADE_POINT)

    def get_str(self):
        return "SILVER"

    def get_grade_id(self):
        return 1