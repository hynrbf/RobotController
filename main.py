import rcu


# entry point
def main():
    rcu.SetMotorStraightAngle(1, 2, 50, 1000)
    rcu.SetMotor(1, 50)
    rcu.SetMotorStraight(1, 2, 50)
    rcu.SetWaitForAngle(1, 50, 90)
    rcu.SetMotorServo(1, 50, 90)
    rcu.SetCarTurn(1, 2, 50, 1000)
    rcu.SetMotorStraightTurn(1, 2, 50, 45)


main()
