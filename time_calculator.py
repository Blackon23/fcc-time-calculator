def add_time(start, duration, day=""):

  start_time, start_period = start.split()[0], start.split()[1]
  start_time_hour, start_time_minute = map(int, start_time.split(":"))
  duration_hour, duration_minute = map(int, duration.split(":"))

  if start_period == "PM":
       start_time_hour += 12

  new_time_hour = start_time_hour + duration_hour
  new_time_minute = start_time_minute + duration_minute

  if new_time_minute >= 60:
    new_time_hour += new_time_minute // 60
    new_time_minute %= 60

  days_after = new_time_hour // 24
  new_time_hour %= 24

  new_time_period = "AM"
  if new_time_hour >= 12:
    new_time_period = "PM"
    if new_time_hour > 12:
      new_time_hour -= 12
  if new_time_hour == 0:
    new_time_hour = 12
    
  #new_time = f"{new_time_hour}:{str(new_time_minute).zfill(2)} {new_time_period}"
  new_time = str(new_time_hour) + ":" + str(new_time_minute).zfill(2) + " " + new_time_period
  
  
    
  if day:
    day = day.lower()
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    day_index = days.index(day)
    new_day_index = (day_index + days_after) % 7
    new_day = days[new_day_index]
    #new_time += f", {new_day.capitalize()}"
    new_time += ", " + new_day.capitalize()

  if days_after == 1:
    new_time += " (next day)"
  elif days_after > 1:
    #new_time += f" ({int(days_after)} days later)"
    new_time += " (" + str(int(days_after)) + " days later)"
    
  return new_time

