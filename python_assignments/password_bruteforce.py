from datetime import datetime
from datetime import timedelta

log_dict = {}
fmt = '%m:%d:%Y %H:%M:%S'

login = int(input('Enter the number of failed login for brute forcing: '))
minute = int(input('Enter the time limit in minutes: '))

with open('logfile_password.txt') as file:
    log_list = [line.rstrip() for line in file]


for line in log_list:
    counter = 0
    line = line.split(" ", 1)
    line_time = datetime.strptime(line[1], fmt)
    delta_time = line_time + timedelta(minutes= minute)
    for itm in log_list:
        itm = itm.split(" ", 1)
        item_time = datetime.strptime(itm[1], fmt)
        if line_time <= item_time < delta_time and itm[0] == line[0]:
            counter += 1
    if counter >= login and line[0] not in log_dict:
        log_dict[line[0]] = counter

with open('output_file.txt', 'w') as op_file:
    for line in log_dict:
        login_det = 'Number of failed login : ' + str(log_dict[line]) + '\n'
        op_file.write(login_det)
        attacker = ' Detected brute force attacks : ' + str(line) + '\n'
        op_file.write(attacker)
        time_limit = ' Time limit in minutes: ' + str(minute) + '\n'
        op_file.write(time_limit)
        op_file.write('\n')