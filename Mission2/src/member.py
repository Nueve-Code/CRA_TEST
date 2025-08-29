from Mission2.src.day import Day, day_properties
from Mission2.src.grade.normal import NormalGrade


class Member:
    def __init__(self, member_name: str, member_id: int):
        self._member_name = member_name
        self._member_id = member_id
        self._weekend_attendance = 0
        self._wednesday_attendance = 0
        self._points = 0
        self._attendance_of_the_week = [0] * 7
        self._grade = NormalGrade()

    @property
    def id(self):
        return self._member_id

    @property
    def name(self):
        return self._member_name

    @property
    def weekend_attendance(self):
        return self._weekend_attendance

    @property
    def wednesday_attendance(self):
        return self._wednesday_attendance

    @property
    def points(self):
        return self._points

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    @property
    def attendance(self):
        return self._attendance_of_the_week

    def get_weekend_attendance(self):
        return (self._attendance_of_the_week[day_properties[Day.SATURDAY]["day_id"]] +
        self._attendance_of_the_week[day_properties[Day.SUNDAY]["day_id"]])

    def check_attendance(self, day: int):
        self._attendance_of_the_week[day] += 1

    def add_points(self, point: int):
        self._points += point