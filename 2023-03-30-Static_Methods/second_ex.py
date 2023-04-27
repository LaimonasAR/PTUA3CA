# pylint: disable= missing-docstring

class TimeUtils:

    @staticmethod
    def time_to_seconds(time_string: str):
        hour, mins, secs = map(int, time_string.split(":"))
        time = (hour * 60 * 60) + mins * 60 + secs
        return time


print(TimeUtils.time_to_seconds("15:36:20"))
