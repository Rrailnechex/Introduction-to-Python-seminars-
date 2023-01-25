import database_controller as DC
import View as V


def start():
    while True:
        V.print_ui()
        DC.main_controller()
