from Mission2.src.day import Day, day_properties
from Mission2.src.grade.normal import NormalGrade


class Member:
    def __init__(self, member_name: str, member_id: int):
        self._member_name = member_name
        self._member_id = member_id
        self._points = 0
        self._attendance_of_the_week = [0, 0, 0, 0, 0, 0, 0]
        self._grade = NormalGrade()

    @property
    def id(self):
        return self._member_id

    @property
    def name(self):
        return self._member_name

    @property
    def points(self):
        return self._points

    @property
    def attendance(self):
        return self._attendance_of_the_week

    def get_wednesday_attendance(self):
        return self._attendance_of_the_week[day_properties[Day.WEDNESDAY]["day_id"]]

    def get_weekend_attendance(self):
        return (self._attendance_of_the_week[day_properties[Day.SATURDAY]["day_id"]] +
                self._attendance_of_the_week[day_properties[Day.SUNDAY]["day_id"]])

    def check_attendance(self, day: int):
        self._attendance_of_the_week[day] += 1

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def add_points(self, point: int):
        self._points += point
