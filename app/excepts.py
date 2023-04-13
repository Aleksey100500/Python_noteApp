import log_creater as lc
import main_menu as mm

def check_number():
    try:
        mm.user_menu()
        number = int(input())
        return number
    except:
        print("not ok")
        lc.excepts_log()
        return check_number()
