
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
    days_of_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # 年月を入力する
    year = int(input('year = '))
    month = int(input('month = '))

    if leap_year(year):
        days_of_month[2] = 29

    first_day = day_of_week(year, month)
    print("日 月 火 水 木 金 土")

    # 1日の前に空白（１日あたり3文字）を表示する
    print(' ' * first_day * 3, end = '')

    # 日を表示する
    for day in (range(1, 1 + days_of_month[month])):
        # 2文字右詰＋空白1文字＝3文字で表示する
        print(format(day, '>2') + ' ', end = '')

        # 土曜日を表示したら改行する
        if (day + first_day - 1) % 7 == 6:
            print()

    # 最後にもう1度改行する
    print()



