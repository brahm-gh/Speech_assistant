import requests
import json

##### based on muscle group #####

muscle = 'biceps'
api_url = 'https://api.api-ninjas.com/v1/exercises?muscle={}'.format(muscle)
response = requests.get(api_url, headers={'X-Api-Key': 'vpAYANxEoWbSkSd98N00cA==6gBqp74hGUIBWnjp'}).text
obj = response
#obj = obj[1:-1]
obj1 = json.loads(obj)    
#print(type(obj), "   ", type(obj1))

def get_exercises(muscle):
    output = ''
    output += f"Exercises for {muscle}" + '\n'
    for i, exercise in enumerate(obj1):
        output += f'Exercise {i + 1}: ' + exercise['name'] + '\n'
        output += 'Equipment: ' + exercise['equipment'] + '\n'
        output += 'Instruction : ' + exercise['instructions'] + '\n'
        if i == 4:
            break
        return output


print(get_exercises(muscle))

##### based on type of exercise #####
"""
type = 'cardio'
api_url2 = 'https://api.api-ninjas.com/v1/exercises?type={}'.format(type)
response2 = requests.get(api_url2, headers={'X-Api-Key': 'vpAYANxEoWbSkSd98N00cA==6gBqp74hGUIBWnjp'}).text
obj2 = response2
obj3 = json.loads(obj2)  
print(f"Exercises for {type}", '\n')
for i, exercise in enumerate(obj3):
    print(f'Exercise {i + 1}: ', exercise['name'], '\n')
    print('Equipment: ', exercise['equipment'], '\n')
    print('Instruction : ', exercise['instructions'], '\n')
    if i == 4:
        break
    """