# 读取文件中的课表信息并生成一个时间-课程文件
import json
import time

courses = json.load(open('course.json', 'r', encoding='utf-8'))
time_table = []
# 设置第一周的周一的日期'2023-09-04'
start_time = time.mktime(time.strptime('2023-09-04', '%Y-%m-%d'))
# 每节课的时间
times = [["08:00", "08:50"],["09:00", "09:50"],["10:10", "11:00"],["11:10", "12:00"],["13:30", "14:20"],["14:20", "15:10"],["15:20", "16:10"],["16:10", "17:00"],["18:00", "18:50"],["19:00", "19:50"],["20:00", "20:50"],["21:00", "21:50"]]
# for course in courses['datas']['cxxszhxqkb']['rows']:
    # print(course['KCM'])    # 课程名
    # print(course['SKZC'])   # 上课周次
    # print(course['JASMC'])  # 教室名
    # print(course['KSJC'])   # 开始节次
    # print(course['JSJC'])   # 结束节次
    # print(course['SKXQ'])   # 上课星期

# 遍历20周，共20*7=140天，i代表周次
for i in range(20):
    # 遍历每一节课
    for course in courses['datas']['cxxszhxqkb']['rows']:
        # 生成时间
        today_date = time.strftime(
            "%Y-%m-%d", time.localtime(start_time + (course['SKXQ']-1) * 86400 + i * 7 * 86400))
        start = today_date + ' ' + times[course['KSJC']-1][0]
        end = today_date + ' ' + times[course['JSJC']-1][1]
        # 判断是否在上课周次内，"1111100000" ，代表前五周有课
        try:
            if course['SKZC'][i] == '1':
                # 判断是否在上课时间内
                # 生成时间-课程文件
                time_table.append({
                    'start': start,
                    'end': end,
                    'course': course['KCM'],
                    'classroom': course['JASMC']
                })
        except IndexError:
            pass

# 去重
# time_table = list({v['start']:v for v in time_table}.values())
# 排序
time_table.sort(key=lambda x: x['start'])

# 写入文件
with open('time_table.json', 'w', encoding='utf-8') as f:
    json.dump(time_table, f, ensure_ascii=False, indent=4)