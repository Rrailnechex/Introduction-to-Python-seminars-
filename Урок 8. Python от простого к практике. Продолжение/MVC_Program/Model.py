import View
import Controller
import Data


def start():
    while True:
        Controller.load_csv()
        View.do_ui()
        Controller.main_controller()
        Controller.save_csv(Data.Cabinets_DB, Data.Classes_DB,
                            Data.Students_DB, Data.Teachers_DB)
