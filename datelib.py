# =============================================================================
# 日数計算
# =============================================================================
import datetime as dt

def day_count(fromdate, todate, delimiter='/'):
    # 年月日の分割（from）
    fy = int(fromdate.split(delimiter)[0])
    fm = int(fromdate.split(delimiter)[1])
    fd = int(fromdate.split(delimiter)[2])

    # 年月日の分割（to）
    ty = int(todate.split(delimiter)[0])
    tm = int(todate.split(delimiter)[1])
    td = int(todate.split(delimiter)[2])

    # fromdate から todate までの日数を計算
    days = dt.date(ty, tm, td) - dt.date(fy, fm, fd)

    return days.days


def add_days(fromdate, days, delimiter='/'):
    from datetime import datetime
    import datetime as dt
    from datetime import timedelta

    # 年月日の分割（from）
    fy = int(fromdate.split(delimiter)[0])
    fm = int(fromdate.split(delimiter)[1])
    fd = int(fromdate.split(delimiter)[2])

    # days で指定した日数を加算した日付を求める
    d = dt.date(fy, fm, fd) + timedelta(days)

    # 日付を文字列に変換し、指定した区切り文字で区切る。
    todate = d.strftime("%Y") + delimiter + d.strftime("%m") + delimiter + d.strftime("%d")

    return todate

print(day_count("2020/02/02","2020/05/26"))

print(add_days("2020/02/02",114))
