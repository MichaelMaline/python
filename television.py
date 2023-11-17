class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL
        self.stack = []

    def power(self):
        if not self.__status:
            self.__status = True
        else:
            self.__status = False

    def mute(self):
        if self.__status:
            if not self.__muted:
                self.stack.append(self.__volume)
                self.__muted = True
                self.__volume = 0
            else:
                self.__volume = self.stack.pop()
                self.__muted = False
        else:
            return

    def channel_up(self):
        if self.__status:
            if self.__channel != 3:
                self.__channel += 1
            else:
                self.__channel = 0
        else:
            return

    def channel_down(self):
        if self.__status:
            if self.__channel != 0:
                self.__channel -= 1
            else:
                self.__channel = 3
        else:
            return

    def volume_up(self):
        if self.__status:
            if self.__volume != 2 and not self.__muted:
                self.__volume += 1
            elif self.__volume != 2 and self.__muted:
                self.__volume = self.stack.pop()
                self.__muted = False
                self.__volume += 1
            else:
                self.__volume = 2
        else:
            return

    def volume_down(self):
        if self.__status:
            if self.__volume != 0 and not self.__muted:
                self.__volume -= 1
            elif self.__volume != 2 and self.__muted:
                self.__volume = self.stack.pop()
                self.__muted = False
                self.__volume -= 1
            else:
                self.__volume = 0
        else:
            return

    def __str__(self):
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
