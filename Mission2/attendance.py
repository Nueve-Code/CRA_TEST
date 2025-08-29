member_ids = {}
total_members = 0

MAX_MEMBER_COUNT = 100
GOLD_GRADE_POINT = 50
SILVER_GRADE_POINT = 30
GRADE_NORMAL = 0
GRADE_GOLD = 1
GRADE_SILVER = 2

# dat[사용자ID][요일]
attendance_data = [[0] * MAX_MEMBER_COUNT for _ in range(MAX_MEMBER_COUNT)]
points = [0] * MAX_MEMBER_COUNT
grade = [0] * MAX_MEMBER_COUNT
names = [''] * MAX_MEMBER_COUNT
wednesday_attendance = [0] * MAX_MEMBER_COUNT
weekend_attendance = [0] * MAX_MEMBER_COUNT


def init_member_data(member_name, day: str):
    global total_members

    if member_name not in member_ids:
        total_members += 1
        member_ids[member_name] = total_members
        names[total_members] = member_name

    member_id = member_ids[member_name]

    add_point = get_point_of_the_day(day)
    check_special_day_attendance(day, member_id)

    attendance_data[member_id][get_day_idx(day)] += 1
    points[member_id] += add_point


def get_day_idx(day: str):
    day_dict = {
        'monday': 0,
        'tuesday': 1,
        'wednesday': 2,
        'thursday': 3,
        'friday': 4,
        'saturday': 5,
        'sunday': 6
    }

    return day_dict[day]


def check_special_day_attendance(day: str, member_id):
    if day == "wednesday":
        wednesday_attendance[member_id] += 1
    elif day == "saturday" or day == "sunday":
        weekend_attendance[member_id] += 1


def get_point_of_the_day(day: str):
    day_point = {
        'monday': 1,
        'tuesday': 1,
        'wednesday': 3,
        'thursday': 1,
        'friday': 1,
        'saturday': 2,
        'sunday': 2
    }

    return day_point[day]


def get_additional_points(i):
    wednesday_attendance_count = attendance_data[i][get_day_idx('wednesday')]
    weekend_attendance_count = attendance_data[i][get_day_idx('saturday')] + attendance_data[i][get_day_idx('sunday')]

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
    for member_id in range(1, total_members + 1):
        points[member_id] += get_additional_points(member_id)
        set_grade(member_id)

        print(f"NAME : {names[member_id]}, POINT : {points[member_id]}, GRADE : ", end="")
        print(f"{get_grade_str(member_id)}")


def removing_members():
    print("\nRemoved player")
    print("==============")
    for member_id in range(1, total_members + 1):
        if (grade[member_id] not in (GRADE_GOLD, GRADE_SILVER)
                and wednesday_attendance[member_id] == 0
                and weekend_attendance[member_id] == 0):
            print(names[member_id])


def get_grade_str(member_id):
    if grade[member_id] == GRADE_GOLD:
        return "GOLD"
    elif grade[member_id] == GRADE_SILVER:
        return "SILVER"
    else:
        return "NORMAL"


def set_grade(i):
    if points[i] >= GOLD_GRADE_POINT:
        grade[i] = GRADE_GOLD
    elif points[i] >= SILVER_GRADE_POINT:
        grade[i] = GRADE_SILVER
    else:
        grade[i] = GRADE_NORMAL


if __name__ == "__main__":
    input_file()
