import View
import Controller


def start():
    while True:
        Controller.load_csv()
        View.do_ui()
        Controller.main_controller()
        Controller.save_csv()
