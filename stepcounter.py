import datetime
import random



'''def stepcount(min=1000, max=15000):
    a = random.randint(min, max)
    return a'''

def main():
    '''f = open('steps.txt', 'w')
    f.write("Date""          ""Steps\n")
    f.close
    start_date = datetime.date(2022, 12, 31)
    end_date = datetime.date(2023, 12, 31)
    current_date = start_date

    while current_date <= end_date:
        for i in range(365):
            L = str(current_date)
            s = stepcount(1000, 15000)
            S = str(s)
            with open('steps.txt', 'a') as file1:
                file1.write(L+"     "+S+'\n')
                current_date += datetime.timedelta(days = 1)
                break
            
    file1.close'''

    
    with open('steps.txt', 'r') as f:
        lines = f.readlines()
        step_counter = {}
        for line in lines:
            alist = line.strip().split()
            step_counter[alist[0]] = alist[1]
            

    
    f.close
    d = step_counter
    Step_counter = {}
    for key, value in d.items():
        if value == "Steps":
            continue
        else:
            Step_counter[key] = int(value) 

   
    months = []
    count = 0
    for i in range (1, 13):
        months.append(i)
    months = ["%02d" % n for n in months]

    for key, value in Step_counter.items():
            if value >= 10000:
                count+=1
    
      
    
    from itertools import groupby
    month_count = {key:sum(list(zip(*val))[1]) for key, val in groupby(Step_counter.items(), key = lambda x:x[0][5:7])}
    calender = {'01': 31, '02': 28, '03':31, '04': 30, '05': 31, '06': 30, '07': 31, '08': 30, '09': 30, '10': 31, '11': 30, '12':31}
    month_averages = {key:month_count[key]//calender[key] for key in month_count.keys()}
    
      
    for key, value in month_averages.items():
        print('Your average steps for month: ' + str(key) + ' is '+ str(value))
    print('This year you achieved ' + str(count) + 'days with steps count above 10000')

            
      
main()
