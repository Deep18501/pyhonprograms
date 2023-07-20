def add_time(start, duration,day=""):
    startTime=start.split(":")
    tempt=startTime[1].split(" ")
    startTime[1]=tempt[0]
    startTime[0]=int(startTime[0])
    startTime[1]=int(startTime[1])
    if tempt[1]=='PM':
        if startTime!=12:
            startTime[0]+=12
    if tempt[1]=='AM' and startTime[0]==12:
        startTime[0]=0
      
    timePeriod=duration.split(":")
    timePeriod[0]=int(timePeriod[0])
    timePeriod[1]=int(timePeriod[1])
    endTime=[]
    endTime.append(startTime[0]+timePeriod[0])
    endTime.append(startTime[1]+timePeriod[1])
    if endTime[1]>=60:
        endTime[0]+=int(endTime[1]/60)
        endTime[1]=endTime[1]%60
    days=0
    if endTime[0]>=24:
        days+=int(endTime[0]/24)
        endTime[0]=endTime[0]%24

    endTime[0]=str(endTime[0])
    if endTime[1]<10:
        endTime[1]="0"+str(endTime[1])
    else:
        endTime[1]=str(endTime[1])

    new_time=""
    if endTime[0]=="12":
        new_time+="12:"+endTime[1]+" PM"
    elif endTime[0]=="0":
        new_time+="12:"+endTime[1]+" AM"

    elif int(endTime[0])<12:
        new_time+=endTime[0]+":"+endTime[1]+" AM"
    else :
        format=int(endTime[0])%12
        new_time+=str(format)+":"+endTime[1]+" PM"

    totalDays=["Sunday","Monday","Tuesday","Wednesday","Thrusday","Friday","Saturday"]
    if day!="":
        day=day.capitalize()
        nday=0
        for i in range(7):
            if day==totalDays[i]:
                nday=i
                break;

        nday+=days
        nday=nday%7
        new_time+=", "+ totalDays[nday]
    if days==1:
        new_time+=" (next day)"
    elif days>1:
        new_time+=" ("+str(days) +" days later)"
                
        
  




    return new_time