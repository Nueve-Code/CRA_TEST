member_ids = {}
total_members = 0

MAX_MEMBER_COUNT = 100

# dat[사용자ID][요일]
attendance_data = [[0] * MAX_MEMBER_COUNT for _ in range(MAX_MEMBER_COUNT)]
points = [0] * MAX_MEMBER_COUNT
grade = [0] * MAX_MEMBER_COUNT
names = [''] * MAX_MEMBER_COUNT
wednesday_attendance = [0] * MAX_MEMBER_COUNT
weekend_attendance = [0] * MAX_MEMBER_COUNT


def init_members(member_name, day: str):
    global total_members

    if member_name not in member_ids:
        total_members += 1
        member_ids[member_name] = total_members
        names[total_members] = member_name

    member_id = member_ids[member_name]

    add_point = get_points_per_day(day)
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
    elif day == "saturday":
        weekend_attendance[member_id] += 1
    elif day == "sunday":
        weekend_attendance[member_id] += 1


def get_points_per_day(day: str):
    point_per_day = {
        'monday': 1,
        'tuesday': 1,
        'wednesday': 3,
        'thursday': 1,
        'friday': 1,
        'saturday': 2,
        'sunday': 2
    }

    return point_per_day[day]


def input_file():
    try:
        with open("attendance_weekday_500.txt", encoding='utf-8') as f:
            for _ in range(500):
                line = f.readline()
                if not line:
                    break
                parts = line.strip().split()
                if len(parts) == 2:
                    init_members(parts[0], parts[1])

        for i in range(1, total_members + 1):
            points[i] += get_additional_points(i)

            if points[i] >= 50:
                grade[i] = 1
            elif points[i] >= 30:
                grade[i] = 2
            else:
                grade[i] = 0

            print(f"NAME : {names[i]}, POINT : {points[i]}, GRADE : ", end="")
            if grade[i] == 1:
                print("GOLD")
            elif grade[i] == 2:
                print("SILVER")
            else:
                print("NORMAL")

        print("\nRemoved player")
        print("==============")
        for i in range(1, total_members + 1):
            if grade[i] not in (1, 2) and wednesday_attendance[i] == 0 and weekend_attendance[i] == 0:
                print(names[i])

    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")


def get_additional_points(i):
    wednesday_attendance_count = attendance_data[i][get_day_idx('wednesday')]
    weekend_attendance_count = attendance_data[i][get_day_idx('saturday')] + attendance_data[i][get_day_idx('sunday')]

    if (wednesday_attendance_count > 9) or (weekend_attendance_count > 9) :
        return 10
    else:
        return 0


if __name__ == "__main__":
    input_file()
