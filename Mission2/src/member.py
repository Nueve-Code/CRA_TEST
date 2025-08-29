from Mission2.src.day import Day


class Member:
    def __init__(self, member_name: str, member_id: int):
        self._member_name = member_name
        self._member_id = member_id
        self._weekend_attendance = 0
        self._wednesday_attendance = 0
        self._points = 0
        self._attendance_of_the_week = [0] * 7

    @property
    def member_id(self):
        return self._member_id

    @property
    def member_name(self):
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
    def attendance(self):
        return self._attendance_of_the_week

    def check_attendance(self, day: int):
        self._attendance_of_the_week[day] += 1

    def add_points(self, point: int):
        self._points += point