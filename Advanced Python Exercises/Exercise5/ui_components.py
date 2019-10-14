from abc import abstractmethod


class Button:
    """Mock button"""

    @abstractmethod
    def __init__(self):
        self.clicked = False

    @abstractmethod
    def click(self):
        self.clicked = True


class WindowsButton(Button):
    """Mock Windows button"""

    def __init__(self):
        super().__init__()

    def click(self):
        self.clicked = True


class LinuxButton(Button):
    """Mock Linux button"""

    def __init__(self):
        super().__init__()

    def click(self):
        self.clicked = True


class Text:
    """Mock text"""

    @abstractmethod
    def __init__(self):
        self.text = ''

    def set_text(self, text):
        self.text = text


class WindowsText(Text):
    """Mock Windows text"""

    def __init__(self):
        super().__init__()


class LinuxText(Text):
    """Mock Linux text"""

    def __init__(self):
        super().__init__()
