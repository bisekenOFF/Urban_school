def champ(num1, num2, score2, team1_time, score1, challenge_result, task_total, time_avg):
    print("В команде Мастера кода участников: %s" % num1)
    print('Итого сегодня в командах участников: %s и %s!' % (num1, num2))
    print('Команда Волшебники данных решила задач: {}'.format(score2))
    print('Волшебники данных решили задачи за {} c !'.format(team1_time))
    print(f'Команды решили {score1} и {score2} задач.')
    print(f'Результат битвы:{challenge_result}')
    print(f'Сегодня было решено {task_total} задач, в среднем по {time_avg} секунды на задачу!')


champ(5, 6, 42, 1552.512, 40, 'Победа команды Волшебники данных!', 82, 45.2)
