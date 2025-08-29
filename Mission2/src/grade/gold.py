from Mission2.src.grade.grade_interface import GradeInterface


class GoldGrade(GradeInterface):
    GOLD_GRADE_POINT = 50

    def __init__(self):
        super().__init__(self.GOLD_GRADE_POINT)

    def get_str(self):
        return "GOLD"