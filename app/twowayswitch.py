class TwoWaySwitch:
    def __init__(self):
        # Light state: False = OFF, True = ON
        self.light_on = False
        self.switch1 = 0  # position of switch 1 (0 or 1)
        self.switch2 = 0  # position of switch 2 (0 or 1)
        self.update_light()

    def update_light(self):
        # In real two-way switch wiring, the light turns ON
        # when both switches are in the SAME position,
        # and OFF when they are in DIFFERENT positions.
        self.light_on = (self.switch1 == self.switch2)

    def toggle_switch1(self):
        self.switch1 = 1 - self.switch1  # flip between 0 and 1
        self.update_light()
        self.show_status("Switch 1")

    def toggle_switch2(self):
        self.switch2 = 1 - self.switch2
        self.update_light()
        self.show_status("Switch 2")

    def show_status(self, toggled_by):
        state = "ON 💡" if self.light_on else "OFF ⚫"
        print(f"{toggled_by} toggled -> Switch1={self.switch1}, Switch2={self.switch2}, Light is {state}")