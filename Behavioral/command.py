# Command interface
class Command:
    def execute(self):
        pass


class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()


class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()


# Receiver class
class Light:
    def on(self):
        print("Light is turned on")

    def off(self):
        print("Light is turned off")

# Invoker class
class RemoteControl:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name, command):
        self.commands[command_name] = command

    def execute_command(self, command_name):
        if command_name in self.commands:
            self.commands[command_name].execute()


# Usage
light = Light()
light_on_command = LightOnCommand(light)
light_off_command = LightOffCommand(light)

remote_control = RemoteControl()
remote_control.register_command("ON", light_on_command)
remote_control.register_command("OFF", light_off_command)

remote_control.execute_command("ON")
remote_control.execute_command("OFF")

