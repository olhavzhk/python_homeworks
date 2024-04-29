CHANNELS = ["BBC", "Discovery", "TV1000"]


class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.channel_index = 0

    def first_channel(self):
        self.channel_index = 0
        return self.current_channel()

    def last_channel(self):
        self.channel_index -= 1
        return self.current_channel()

    def turn_channel(self, number):
        if 1 <= number <= len(self.channels):
            self.channel_index = number - 1
            return self.current_channel()
        else:
            return "Channel not found"

    def next_channel(self):
        self.channel_index = (self.channel_index + 1) % len(self.channels)
        return self.current_channel()

    def previous_channel(self):
        self.channel_index = (self.channel_index - 1) % len(self.channels)
        return self.current_channel()

    def current_channel(self):
        return self.channels[self.channel_index]

    def is_exist(self, name_or_number):
        if name_or_number in self.channels:
            return "Yes"
        elif 1 <= name_or_number <= len(self.channels):
            return "Yes"
        else:
            return "No"


controller = TVController(CHANNELS)

assert controller.first_channel() == "BBC"
assert controller.last_channel() == "TV1000"
assert controller.turn_channel(1) == "BBC"
assert controller.next_channel() == "Discovery"
assert controller.previous_channel() == "BBC"
assert controller.current_channel() == "BBC"
assert controller.is_exist(4) == "No"
assert controller.is_exist("BBC") == "Yes"
