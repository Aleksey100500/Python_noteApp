import datetime

def excepts_log():
    name_exc = "ValueError"
    time = f"{datetime.datetime.now().strftime('%Y-%m-%d_%H-%S')}_{name_exc}"
    with open('log_file.csv', 'a') as file:
        file.write(f'{time}\n')