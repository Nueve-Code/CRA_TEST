from Mission2.src.day import get_day_idx, get_point_of_the_day, parsing_days
from Mission2.src.member import Member
from Mission2.src.policy.policy_grade_point import GradePointPolicy

member_list: dict = {}
total_members = 0


def init_member_data(member_name, day):
    global total_members

    day = parsing_days(day)

    if member_name not in member_list:
        total_members += 1
        m = Member(member_name, total_members)
        member_list[member_name] = m

    member = member_list[member_name]
    member.check_attendance(get_day_idx(day))
    member.add_points(get_point_of_the_day(day))


def input_file():
    try:
        init_data_with_read_file()
        set_grade_per_members()
        removing_members()

    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")


def init_data_with_read_file():
    with open("attendance_weekday_500.txt", encoding='utf-8') as f:
        for _ in range(500):
            line = f.readline()
            if not line:
                break
            attend_data = line.strip().split()
            if len(attend_data) == 2:
                name, day = attend_data[0], attend_data[1]
                init_member_data(name, day)


def set_grade_per_members():
    for member in member_list:
        member = member_list[member]
        member.add_points(GradePointPolicy.get_additional_points(
            weekend_attendance_count=member.get_weekend_attendance(),
            wednesday_attendance_count=member.get_wednesday_attendance()))
        member.grade = GradePointPolicy.get_grade_per_standard(member.points)

        print(f"NAME : {member.name}, POINT : {member.points}, GRADE : ", end="")
        print(f"{member.grade.get_str()}")


def removing_members():
    print("\nRemoved player")
    print("==============")
    for member in member_list:
        member = member_list[member]
        if GradePointPolicy.remove_condition(member):
            print(member.name)


if __name__ == "__main__":
    input_file()
