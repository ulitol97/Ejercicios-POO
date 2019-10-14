from abc import abstractmethod
import ui_components


class AbstractFactory:
    """Abstract factory generating concrete factories"""

    @abstractmethod
    def __init__(self):
        pass

    @staticmethod
    def get_factory(factory_type):
        if factory_type == 'Windows':
            return WindowsFactory()
        else:
            return LinuxFactory()

    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_text(self):
        pass


class WindowsFactory(AbstractFactory):

    def __init__(self):
        pass

    def create_button(self):
        return ui_components.WindowsButton()

    def create_text(self):
        return ui_components.WindowsText()


class LinuxFactory(AbstractFactory):

    def __init__(self):
        pass

    def create_button(self):
        return ui_components.LinuxButton()

    def create_text(self):
        return ui_components.LinuxText()


if __name__ == '__main__':
    """Sample main to test functionality. Create each factory and call their methods"""

    win_factory = AbstractFactory.get_factory('Windows')
    linux_factory = AbstractFactory.get_factory('Linux')

    win_button = win_factory.create_button()
    linux_button = linux_factory.create_button()
    win_button.click()
    linux_button.click()

    print (win_button.clicked)
    print (linux_button.clicked)

    win_text = win_factory.create_text()
    linux_text = linux_factory.create_text()
    win_text.set_text('Windows Text')
    linux_text.set_text('Linux Text')

    print (win_text.text)
    print (linux_text.text)
