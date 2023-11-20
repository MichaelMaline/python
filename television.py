class Television:
    """
    A class representing a Television.

    Attributes:
        MIN_VOLUME (int): The minimum volume level.
        MAX_VOLUME (int): The maximum volume level.
        MIN_CHANNEL (int): The minimum channel number.
        MAX_CHANNEL (int): The maximum channel number.

    Methods:
        __init__(): Initializes a Television object.
        power(): Toggles the power status of the Television.
        mute(): Mutes or unmutes the Television.
        channel_up(): Increases the channel by one.
        channel_down(): Decreases the channel by one.
    """

    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        Initializes a Television object.

        Attributes:
            self.__status (bool): The power status of the Television.
            self.__muted (bool): The mute status of the Television.
            self.__volume (int): The current volume level.
            self.__channel (int): The current channel number.
            self.stack (list): A stack to store volume levels when muted.
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = self.MIN_VOLUME
        self.__channel: int = self.MIN_CHANNEL
        self.stack: list[int] = []

    def power(self) -> None:
        """
        Toggles the power status of the Television.
        """
        if not self.__status:
            self.__status = True
        else:
            self.__status = False

    def mute(self) -> None:
        """
        Mutes or unmutes the Television.
        """
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

    def channel_up(self) -> None:
        """
        Increases the channel by one.
        """
        if self.__status:
            if self.__channel != 3:
                self.__channel += 1
            else:
                self.__channel = 0
        else:
            return

    def channel_down(self) -> None:
        """
        Decreases the channel by one.
        """
        if self.__status:
            if self.__channel != self.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = 3
        else:
            return

    def volume_up(self) -> None:
        """
        Increases the volume by one.
        """
        if self.__status:
            if self.__volume != self.MAX_VOLUME and not self.__muted:
                self.__volume += 1
            elif self.__volume != self.MAX_VOLUME and self.__muted:
                self.__volume = self.stack.pop()
                self.__muted = False
                self.__volume += 1
            else:
                self.__volume = 2
        else:
            return

    def volume_down(self) -> None:
        """
        Decreases the volume by one.
        """
        if self.__status:
            if self.__volume != self.MIN_VOLUME and not self.__muted:
                self.__volume -= 1
            elif self.__volume != self.MAX_VOLUME and self.__muted:
                self.__volume = self.stack.pop()
                self.__muted = False
                self.__volume -= 1
            else:
                self.__volume = 0
        else:
            return

    def __str__(self) -> str:
        """
        Defines the string Method for Television.
        """
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
