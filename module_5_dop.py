import time
class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return self.nickname

class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == user.nickname:
                if  password == user.password:
                    self.current_user = user
                    return
                else:
                    print("Неверный логин или пароль")
                    return
            else:
                print("Неверный логин или пароль")
                return

    def register(self, nickname, password, age):
        for user in  self.users:
            if user.nickname == nickname:
                print(f'пользователь {nickname} уже существует')
                return
        new_user = User(nickname,password,age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            exists = False
            for v in self.videos:
                if v.title == video.title:
                    exists = True
                    break
            if not exists:
                self.videos.append(video)

    def get_videos(self, search):
        search_list = []
        search_l = search.lower()
        for video in self.videos:
            if search_l in video.title.lower():
                search_list.append(video.title)
        return search_list

    def watch_video(self, watch_video):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        v = 0
        for video in self.videos:

            if watch_video == video.title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return
                for i in range(1, video.duration + 1):
                    print(i, end=' ')
                    time.sleep(1)
                print("Конец видео")
                video.time_now = 0
                v = 1
        if v == 0:
            print(f"Видео '{watch_video}' не существует")







ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')





