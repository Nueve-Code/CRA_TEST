member_ids = {}
total_members = 0

# dat[사용자ID][요일]
attendance_data = [[0] * 100 for _ in range(100)]
points = [0] * 100
grade = [0] * 100
names = [''] * 100
wed = [0] * 100
weeken = [0] * 100


def init_members(member_name, day):
    global total_members

    if member_name not in member_ids:
        total_members += 1
        member_ids[member_name] = total_members
        names[total_members] = member_name

    member_id = member_ids[member_name]

    day_idx = get_day_idx(day)
    add_point = get_points_per_day(day)
    add_additional_points(day, member_id)

    attendance_data[member_id][day_idx] += 1
    points[member_id] += add_point


def get_day_idx(day):
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


def add_additional_points(day, member_id):
    if day == "wednesday":
        wed[member_id] += 1
    elif day == "saturday":
        weeken[member_id] += 1
    elif day == "sunday":
        weeken[member_id] += 1


def get_points_per_day(day):
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
            if attendance_data[i][2] > 9:
                points[i] += 10
            if attendance_data[i][5] + attendance_data[i][6] > 9:
                points[i] += 10

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
            if grade[i] not in (1, 2) and wed[i] == 0 and weeken[i] == 0:
                print(names[i])

    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")


if __name__ == "__main__":
    input_file()
