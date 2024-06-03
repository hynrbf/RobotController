# read here first, https://geekdaxue.co/read/zmrobo@robocode/elb5c7#5kyz7i
import rcu


class SensorColors:
    Red = 1
    Green = 2
    Blue = 3
    Yellow = 4
    Black = 5
    White = 6


class ColorController:
    _displayTextYellowColor = 0xFFE0
    _screenBackgroundGreenColor = 0x07E0

    @staticmethod
    def display_color_in_screen():
        while True:
            display = "Color detected is not either black or white"

            if rcu.GetColorSensor(1, 4) == SensorColors.Black:
                display = "Black color detected"
                rcu.SetDisplayString(1, display, ColorController._displayTextYellowColor,
                                     ColorController._screenBackgroundGreenColor)
                continue

            if rcu.GetColorSensor(1, 4) == SensorColors.White:
                display = "White color detected"
                rcu.SetDisplayString(1, display, ColorController._displayTextYellowColor,
                                     ColorController._screenBackgroundGreenColor)
                continue

            rcu.SetWaitForTime(0.5)


# entry point
def main():
    ColorController.display_color_in_screen()


main()
