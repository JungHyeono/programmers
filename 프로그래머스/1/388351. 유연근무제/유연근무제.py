def solution(schedules, timelogs, startday):
    staff = [ True for _ in range(len(schedules))]
    count = 0
    
    for i in range(0, len(schedules)):
        num = -1
        endtime = calc_time(schedules[i])
        for timelog in timelogs[i]:
            num += 1
            if (startday+num) % 7 == 0 or (startday+num) % 7 == 6:
                continue
            elif endtime < timelog:
                staff[i] = False
                break
        
    return sum(staff)
                
def calc_time(time):
    if (time + 10) % 100 <= 59 :
        return time+10
    else: return (time + 50)
    
                