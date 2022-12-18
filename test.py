li = [
    ('Журавлева', '206', '5,5,4,4,5,4', 'good'),
    ('Данилов', '201', '5,2,4,5,4,5', 'poor'),
    ('Петров', '201', '5,5,4,5,4', 'good'),
    ('Сидоров', '303', '3,2,5,4,3', 'poor'),
]

print(li)

def bads(lst):
    for el in lst:
        if 'good' in el:
            return True

print(list(filter(bads, li)))

# def bad_marks(marks):
#     weak_students = []
#     for el in marks:
#         for mark in ['1', '2', '3']:
#             if mark in el[2]:
#                 weak_students.append(el)
#                 break
#     return weak_students


# print(bad_marks(li))
