class Counter:
    def __init__(self):
        """Initialize the counter with a value of 0."""
        self.value = 0

    def increment(self):
        """Increase the counter value by one."""
        self.value += 1

    def get_value(self):
        """Return the current value of the counter."""
        return self.value
