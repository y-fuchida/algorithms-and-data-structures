
def leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

def day_of_week(year, month):
    # 1~12月の月の日数
    days_of_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if leap_year(year):
        days_of_month[2] = 29

    day = 1
    days = 0
    # 年の日数を集計
    for y in range(1, year):
        if leap_year(y):
            days += 366
        else:
            days += 365
    # 月の日数を集計
    for m in range(1, month):
        days += days_of_month[m]
    # 日を集計
    days += day
    # 日〜土曜日を0~6で返す
    return days % 7


if __name__ == '__main__':
    # 曜日
    day_of_week_name = ['日', '月', '火', '水', '木', '金', '土']

    # 年月を入力する
    year = int(input('year = '))
    month = int(input('month = '))

    # 1日の曜日表示
    print(day_of_week_name[day_of_week(year, month)] + '曜日')


