grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

#изменим тип students на list и отсортируем 
students_list = list(students)
students_list_sort = sorted(students_list)

for i in range(len(students_list_sort)):
    
        grades_i_sum = sum(grades[i]) #сумма каждого элемента grades
        grades_i_len = len(grades[i]) #количество элементов в каждом grades
        grades_average= grades_i_sum/grades_i_len # вычисляем среднее значение
        print(students_list_sort[i],"=",grades_average)
    