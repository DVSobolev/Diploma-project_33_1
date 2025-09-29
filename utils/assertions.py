from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Assertions:
    """
    Класс для централизованных проверок UI с использованием ожиданий (Waiter).
    """

    def __init__(self, waiter):
        """
        :param waiter: экземпляр Waiter (utils/waits.py), чтобы использовать его условия
        """
        self.waiter = waiter

    def element_visible(self, locator, msg=None):
        """
        Проверяет, что элемент стал видимым.

        :param locator: локатор элемента (By, value)
        :param msg: кастомное сообщение об ошибке
        """
        try:
            self.waiter.visible(locator)
        except TimeoutException:
            raise AssertionError(msg or f"Элемент {locator} не стал видимым")

    def element_clickable(self, locator, msg=None):
        """
        Проверяет, что элемент кликабелен.

        :param locator: локатор элемента (By, value)
        :param msg: кастомное сообщение об ошибке
        """
        try:
            self.waiter.clickable(locator)
        except TimeoutException:
            raise AssertionError(msg or f"Элемент {locator} не стал кликабельным")

    def element_not_visible(self, locator, msg=None):
        """
        Проверяет, что элемент исчез со страницы.

        :param locator: локатор элемента (By, value)
        :param msg: кастомное сообщение об ошибке
        """
        try:
            self.waiter.gone(locator)
        except TimeoutException:
            raise AssertionError(msg or f"Элемент {locator} не исчез")

    def text_present(self, locator, text, msg=None):
        """
        Проверяет, что у элемента появился ожидаемый текст.

        :param locator: локатор элемента (By, value)
        :param text: текст, который должен появиться
        :param msg: кастомное сообщение об ошибке
        """
        try:
            self.waiter.text_to_be(locator, text)
        except TimeoutException:
            raise AssertionError(msg or f"Текст '{text}' не найден в {locator}")

        def equal(self, expected, actual, msg=None):
            """
            Проверяет равенство двух значений.
            """
            if expected != actual:
                raise AssertionError(msg or f"Ожидалось {expected}, но получили {actual}")

        def not_equal(self, first, second, msg=None):
            """
            Проверяет, что два значения не равны.
            """
            if first == second:
                raise AssertionError(msg or f"Значения не должны быть равны: {first}")

        def contains(self, member, container, msg=None):
            """
            Проверяет, что элемент содержится в последовательности/строке.
            """
            if member not in container:
                raise AssertionError(msg or f"'{member}' не найдено в {container}")

        def not_contains(self, member, container, msg=None):
            """
            Проверяет, что элемент отсутствует в последовательности/строке.
            """
            if member in container:
                raise AssertionError(msg or f"'{member}' не должно быть в {container}")