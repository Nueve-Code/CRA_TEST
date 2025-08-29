from Mission2.src.grade.grade_interface import GradeInterface


class NormalGrade(GradeInterface):

    def __init__(self):
        super().__init__(0)

    def get_str(self):
        return "NORMAL"