import rcu


# All about motor controller
class MotorController:
    @staticmethod
    def set_motor_straight(speed):
        rcu.SetMotor(1, speed)
        rcu.SetMotor(2, speed)
        rcu.SetWaitForTime(1)
        rcu.SetMotor(1, -speed)
        rcu.SetMotor(2, -speed)
        rcu.SetWaitForTime(1)


# All about color controller
class ColorController:
    _yellowColor = 0xFFE0
    _blackColor = 0x0000

    @staticmethod
    def display_color_in_screen():
        while True:
            display = str(rcu.GetLightSensor(1)) + " " + str(rcu.GetLightSensor(2)) + " " + str(
                rcu.GetLightSensor(3)) + " " + str(rcu.GetLightSensor(4)) + " " + str(
                rcu.GetLightSensor(5)) + " " + str(rcu.GetLightSensor(6)) + " " + str(rcu.GetLightSensor(7))
            rcu.SetDisplayString(1, display, ColorController._yellowColor, ColorController._blackColor)
            rcu.SetWaitForTime(0.5)


# entry point
def main():
    # MotorController.set_motor_straight(50)
    ColorController.display_color_in_screen()


main()
