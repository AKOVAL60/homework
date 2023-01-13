# 1. Создать класс TrafficLight (светофор). определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный; в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
# зелёный; продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
# третьего (зелёный) — на ваше усмотрение; переключение между режимами должно осуществляться только в указанном
# порядке (красный, жёлтый, зелёный); проверить работу примера, создав экземпляр и вызвав описанный метод. Задачу
# можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и
# завершать скрипт.

from time import sleep


class TrafficLight:
    __color = ["\033[31m", "\033[33m", "\033[32m"]

    def running(self):
        step = 1
        index = 0
        while True:
            print(f"{self.__color[index]} ● - цвет светофора = цвет текста", end='')
            if index == 0:
                step = 1
                sleep(7)
            elif index == 1:
                sleep(2)
            elif index == 2:
                step = -1
                sleep(5)
            index += step
            print("\r", end='')


TrafficLight().running()
