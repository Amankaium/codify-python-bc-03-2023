class Computer:
    has_mouse = True
    has_keyboard = True
    monitor_size = 24

    def __init__(self, ram, cpu, monitor_size):
        self.ram = ram
        self.cpu = cpu
        self.monitor_size = monitor_size

    def make_report(self):
        if self.ram > 12:
            return "Report is ready"
        else:
            return "Not enough RAM"


comp_1 = Computer(16, 2.5, 22)
comp_2 = Computer(monitor_size=27, ram=12, cpu=3)
print(comp_1.monitor_size, comp_2.monitor_size)
print(comp_1.has_keyboard, comp_2.has_keyboard)
print(comp_1.ram, comp_2.ram)

print(comp_1.make_report())
print(comp_2.make_report())
