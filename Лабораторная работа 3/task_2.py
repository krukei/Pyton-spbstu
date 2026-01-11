# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

def find_common_participants(str1, str2, a=","):
    list_1 = str1.split(a)
    list_2 = str2.split(a)
    list_3 = []
    for i in 0, 1, 2:
        for j in 0, 1, 2:
            if list_1[i] == list_2[j]:
                list_3.append(list_1[i])
    list_3.sort()
    return list_3

find_common_participants(participants_first_group, participants_second_group, a="|")