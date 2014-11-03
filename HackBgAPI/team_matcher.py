import requests
import json


r = requests.get('https://hackbulgaria.com/api/students/', verify=False)
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)

def list_courses():
    result = []
    data = r.json()
    for student in data:
        for course in student['courses']:
            if(course['name']) not in result:
                result.append(course['name'])

    dict = {}
    k = 0
    for elem in result:
        dict[k] = elem
        #print("\n".join(elem))
        k += 1
    print(dict)


def match_command(course_id, team_size, group_time):
    result = []
    data = r.json()
    for student in data:
        for course in student['courses']:
            if(course['name']) not in result:
                result.append(course['name'])

    dict = {}
    k = 0
    for elem in result:
        dict[k] = elem
        #print("\n".join(elem))
        k += 1
        count = 0
    print(dict)
    f = open("test.json", "r")
    my_test_data = f.read()
    jsondata = json.loads(my_test_data)
    f.close()
    for student in jsondata:
        for course in student['courses']:
            if course['name'] == dict[course_id] and course['group'] == group_time:
                print(student['name'])
                count += 1
                if count == team_size:
                    continue

print("choose a command:")
comm = input()
if comm == "list_courses":
    print("Here are the courses:")
    list_courses()
if comm == "match_teams":
    match_command(1, 2, 2)


