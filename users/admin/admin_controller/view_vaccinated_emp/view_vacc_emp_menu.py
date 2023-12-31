from config.prints import Prints
from users.admin.admin_controller.view_vaccinated_emp import view_vacc_emp_filters as filter
from config.prompts import PromptsConfig


def view_vacc_status_menu():
    while True:
        choice = int(input(PromptsConfig.VIEW_VACC_STATUS_PROMPT))
        if choice == 1:
            filter.view_all()
        elif choice == 2:
            filter.view_by_dose(1)
        elif choice == 3:
            filter.view_by_dose(2)
        elif choice == 4:
            filter.view_by_dose(0)
        elif choice == 5:
            filter.view_by_vaccine()
        elif choice == 6:
            filter.view_by_dose_date(1)
        elif choice == 7:
            filter.view_by_dose_date(2)
        elif choice ==8:
            return
        else:
            print(Prints.ENTER_VALID)
            continue