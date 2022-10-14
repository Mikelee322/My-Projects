def add_time(start, duration, dayOfWeek=''):

  startMinutes = convertTime(start)
  durationMinutes = convertTime(duration)
  new_time = startMinutes + durationMinutes

  #Convert back to time

  newTimeDict = {
    'days': 0,
    'hour': 0,
    'minutes': 0
  }
  print('newtime',new_time)
  newTimeDict['days'] = int(new_time / 1440)
  print('days',newTimeDict['days'])
  #print('newtime without days', new_time - days * 1440 + startMinutes)\
  #if new_time - days * 1440 + startMinutes > 1440:
  newTimeDict['hour'] = int((new_time - newTimeDict['days']*1440 )/ 60)
  newTimeDict['minute'] = new_time - newTimeDict['days']*1440 - newTimeDict['hour']*60
  
  print(newTimeDict)
 #print(f"days:{days} hour: {hour} minute: {minutes}")
  
  flag = 'AM'
  if newTimeDict['hour'] >= 12:
    flag = 'PM'
    if newTimeDict['hour'] > 12:
      newTimeDict['hour'] -= 12
  if newTimeDict['hour'] == 0:
      newTimeDict['hour'] = 12

  if newTimeDict['minute']< 10 :
    newTimeDict['minute'] = '0' + str(newTimeDict['minute'])

  if newTimeDict['days'] == 0:
    new_time = f"{newTimeDict['hour']}:{newTimeDict['minute']} {flag}"
  elif newTimeDict['days'] == 1:
    new_time = f"{newTimeDict['hour']}:{newTimeDict['minute']} {flag} (next day)"
  else:
    new_time = f"{newTimeDict['hour']}:{newTimeDict['minute']} {flag} ({newTimeDict['days']} days later)"
  print(new_time)

  return new_time

def dayOfWeekIndex(day):
  if day == '':
    return -1
  return ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
  daysOfWeek.Index(startDay.title())

  
  
  #print("start:" + start)
  #print("duration:" + duration)
  
  #startMinutes = convertTime(start)
  #print(f"startMinutes: {startMinutes}")
  #durationMinutes = convertTime(duration)
  
  #print(f"startMinutes: {startMinutes}")
  #print(f"durationMinutes: {durationMinutes}")

  #print(startMinutes+durationMinutes)
  
  #new_time = start + duration 
  #return new_time

#Working in minutes
def convertTime(timeString):
  minuteTime = 0
  
#Find colon
  Findcolon = timeString.index(':')

  hours = int(timeString[0:Findcolon])
  print(f"hours: {hours}")
  
#grab the 
  if timeString[-2]=='A'and hours == 12:
    hour = 0
    print(f"hours:{hours}")

  if timeString[-2]=='P'and hours > 12:
    minuteTime+=12*60

  minutes = int(timeString[Findcolon+1: Findcolon+3])
  print(f"minutes:{minutes}")

#12:30
  minuteTime += hours*60 + minutes
  return minuteTime