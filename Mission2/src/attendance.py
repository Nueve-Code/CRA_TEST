from Mission2.src.day import day_properties, Day, parsingDays
from Mission2.src.grade.gold import GoldGrade
from Mission2.src.grade.normal import NormalGrade
from Mission2.src.grade.silver import SilverGrade
from Mission2.src.member import Member

member_list: dict = {}
total_members = 0

GOLD_GRADE_POINT = 50
SILVER_GRADE_POINT = 30
GRADE_NORMAL = 0
GRADE_GOLD = 1
GRADE_SILVER = 2


def init_member_data(member_name, day):
    global total_members

    day = parsingDays(day)

    if member_name not in member_list:
        total_members += 1
        m = Member(member_name, total_members)
        member_list[member_name] = m

    member = member_list[member_name]
    member.check_attendance(get_day_idx(day))
    member.add_points(get_point_of_the_day(day))


def get_day_idx(day):
    return day_properties[day]["day_id"]


def get_point_of_the_day(day):
    return day_properties[day]["point"]


def get_additional_points(member):
    wednesday_attendance_count = member.attendance[get_day_idx(Day.WEDNESDAY)]
    weekend_attendance_count = member.get_weekend_attendance() == 0

    if (wednesday_attendance_count > 9) or (weekend_attendance_count > 9):
        return 10
    else:
        return 0


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
        member.add_points(get_additional_points(member))
        set_grade(point=member.points, member=member)

        print(f"NAME : {member.name}, POINT : {member.points}, GRADE : ", end="")
        print(f"{member.grade.get_str()}")


def removing_members():
    print("\nRemoved player")
    print("==============")
    for member in member_list:
        member = member_list[member]
        if (member.grade.get_grade_id() not in (GRADE_GOLD, GRADE_SILVER)
                and member.attendance[get_day_idx(Day.WEDNESDAY)] == 0
                and member.get_weekend_attendance() == 0):
            print(member.name)

def set_grade(point, member):
    if point >= GOLD_GRADE_POINT:
        grade = GoldGrade()
    elif point >= SILVER_GRADE_POINT:
        grade = SilverGrade()
    else:
        grade = NormalGrade()

    member.grade = grade

if __name__ == "__main__":
    input_file()
