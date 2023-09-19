import requests
import json
import time

config = json.load(open('config.json', 'r', encoding='utf-8'))

token = config['token']

headers = {
    "Authorization": "Bearer " + token,
    "content-type": "application/json",
}

i = 0
for calender in config['calenders']:
    i += 1
    print(f'[{i}]请选择你要添加的日历：{calender["friendly_name"]}')

calender_index = int(input('请输入序号：')) - 1

courses = json.load(open('time_table.json', 'r', encoding='utf-8'))

for course in courses:
    start_date_time = time.strptime(course['start'], '%Y-%m-%d %H:%M')
    end_date_time = time.strptime(course['end'], '%Y-%m-%d %H:%M')
    start_date_time = time.strftime("%Y-%m-%dT%H:%M:%S+08:00", start_date_time)
    end_date_time = time.strftime("%Y-%m-%dT%H:%M:%S+08:00", end_date_time)
    data = {
        "entity_id": config['calenders'][calender_index]['entity_id'],
        "summary": course['course'],
        "description": course['classroom'],
        "start_date_time": start_date_time,
        "end_date_time": end_date_time,
    }

    response = requests.post(
        "http://192.168.3.2:8123/api/services/calendar/create_event", headers=headers, json=data
    )

    name = course['course']
    if response.status_code == 200:
        print(f'课程{name}添加成功。')
    else:
        print('创建事件失败:', response.status_code)
        print(response.text)
