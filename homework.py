class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self,
                 training_type: str,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float
                 ) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self) -> str:
        message: str = (f'Тип тренировки: {self.training_type}; '
                        f'Длительность: {self.duration:.3f} ч.; '
                        f'Дистанция: {self.distance:.3f} км; '
                        f'Ср. скорость: {self.speed:.3f} км/ч; '
                        f'Потрачено ккал: {self.calories:.3f}.')
        return message


class Training:
    """Базовый класс тренировки."""
    M_IN_KM = 1000
    LEN_STEP = 0.65
    MIN = 60

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance = self.action * self.LEN_STEP / self.M_IN_KM
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        mean_spead = self.get_distance() / self.duration
        return mean_spead

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(self.__class__.__name__,
                           self.duration,
                           self.get_distance(),
                           self.get_mean_speed(),
                           self.get_spent_calories())


class Running(Training):
    """Тренировка: бег."""
    CALORIES_MEAN_SPEED_SHIFT = 1.79
    CALORIES_MEAN_SPEED_MULTIPLIER = 18

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        super().__init__(action,
                         duration,
                         weight)

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        step_1 = self.CALORIES_MEAN_SPEED_MULTIPLIER * self.get_mean_speed()
        step_2 = step_1 + self.CALORIES_MEAN_SPEED_SHIFT
        step_3 = step_2 * self.weight / self.M_IN_KM * self.duration * self.MIN
        return step_3


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    CALORIES_KOEF_1 = 0.035
    CALORIES_KOEF_2 = 0.029
    ROST_V_M = 100
    KM_V_M = 0.278
    MIN = 60

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: int
                 ) -> None:
        super().__init__(action,
                         duration,
                         weight)
        self.height = height

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        return ((self.CALORIES_KOEF_1 * self.weight
                + ((self.get_mean_speed() * self.KM_V_M)**2
                 / (self.height / self.ROST_V_M)) * self.CALORIES_KOEF_2
                * self.weight) * (self.duration * self.MIN)
                )


class Swimming(Training):
    """Тренировка: плавание."""
    KOEF_NUM = 1.1
    KOEF_NUM_2 = 2
    LEN_STEP = 1.38

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: int,
                 count_pool: int
                 ) -> None:
        super().__init__(action,
                         duration,
                         weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance = self.action * self.LEN_STEP / self.M_IN_KM
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        msd = self.length_pool * self.count_pool / self.M_IN_KM / self.duration
        return msd

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        specal_one = (self.get_mean_speed() + self.KOEF_NUM) * self.KOEF_NUM_2
        specal_two = specal_one * self.weight * self.duration
        return specal_two


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    some_dictionary = {'SWM': Swimming,
                       'RUN': Running,
                       'WLK': SportsWalking}

    return some_dictionary[workout_type](*data)


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
