import rcu


# The robot class
class RobotController:
    @staticmethod
    def set_motor_straight(speed):
        rcu.SetMotor(1, speed)
        rcu.SetMotor(2, speed)
        rcu.SetWaitForTime(1)
        rcu.SetMotor(1, -speed)
        rcu.SetMotor(2, -speed)
        rcu.SetWaitForTime(1)


# entry point
def main():
    RobotController.set_motor_straight(50)


main()
