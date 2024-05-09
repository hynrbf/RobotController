import rcu


# The robot class
class RobotController:
    @staticmethod
    def set_motor_straight(motor1, motor2, speed):
        rcu.SetMotorStraight(motor1, motor2, speed)


# entry point
def main():
    RobotController.set_motor_straight(1, 2, 300)


if __name__ == "__main__":
    main()
