from unittest import mock

import Mission2.src.attendance
from Mission2.src.attendance import removing_members, init_member_data, set_grade_per_members, input_file


def test_removing_members(capsys):
    Mission2.src.attendance.member_list = {}
    test_member = "test"
    test_day = 'monday'

    init_member_data(member_name=test_member, day=test_day)
    removing_members()

    captured = capsys.readouterr()
    assert "\nRemoved player\n==============\ntest" in captured.out


def test_set_grade_per_members(capsys):
    Mission2.src.attendance.member_list = {}
    test_member = "test"
    test_day = 'monday'

    init_member_data(member_name=test_member, day=test_day)
    set_grade_per_members()

    captured = capsys.readouterr()
    assert f"NAME : {test_member}, POINT : 1, GRADE : NORMAL\n" in captured.out


def test_init_data_with_read_file_with_error(capsys):
    Mission2.src.attendance.init_data_with_read_file("invalid_file.txt")

    captured = capsys.readouterr()
    assert "파일을 찾을 수 없습니다." in captured.out


@mock.patch("Mission2.src.attendance.init_data_with_read_file")
@mock.patch("Mission2.src.attendance.set_grade_per_members")
@mock.patch("Mission2.src.attendance.removing_members")
def test_input_file(removing_members, set_grade_per_members, init_data_with_read_file):
    input_file()

    removing_members.assert_called_once()
    set_grade_per_members.assert_called_once()
    init_data_with_read_file.assert_called_once()
