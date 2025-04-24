def solution(video_len, pos, op_start, op_end, commands):
    video_sec = mintosec(video_len)
    pos_sec = mintosec(pos)
    op_start_sec = mintosec(op_start)
    op_end_sec = mintosec(op_end)
    
    for i in commands:
        if pos_sec >= op_start_sec and pos_sec <= op_end_sec:
            pos_sec = op_end_sec
        if i == "next":
            pos_sec += 10
            if pos_sec > video_sec:
                pos_sec = video_sec
                
        elif i == "prev":
            pos_sec -= 10
            if pos_sec < 0:
                pos_sec = 0
    if pos_sec > op_start_sec and pos_sec < op_end_sec:
            pos_sec = op_end_sec
    
    mm = pos_sec//60
    ss = pos_sec%60
    
    result = f"{mm:02}:{ss:02}"
    return result

def mintosec(name):     #분:초를 초로 바꾸는 함수
    min, sec = name.split(":")
    name_sec = int(min)*60+int(sec)
    return name_sec