my_programing_school = {
    'People': {
        'Role': {
                'students': { 1: 
                                {
                                "name": 'Laimonas',
                                "age": '39',
                                'experience': {
                                            'level': 'Rookie',
                                            'degree': 'Computer technics engineer'
                                            },
                                },
                            2 :{
                                "name": 'Jonas',
                                "age": '25',
                                'experience': {
                                            'level': 'Advanced',
                                            'degree': 'C++ programmer'
                                            },
                                }   
                            },
                'teachers': { 1: {
                                "name": 'Mindaugas',
                                "age": 'unknown',
                                'experience': {
                                            'level': 'Pro',
                                            'degree': 'Python programmer'
                                            },
                                 },
                              2: {
                                "name": 'Vytautas',
                                "age": 'unknown',
                                'experience': {
                                            'level': 'Pro',
                                            'degree': 'Data science'
                                            },
                                 },
                             }
                    }
                    },
    'classrooms': {},
    'equipment' : {}
}
#print(my_programing_school)

for student, info in my_programing_school['People']['Role']['students'].items():
    print("\nStudent:", student)
    for key in info:
        print(key + ':',info[key])
