# (b)
import calendar

cal = calendar.TextCalendar(firstweekday=3)
cal.pryear(2012)

# (c)
# July 13rd is my birthday
cal = calendar.TextCalendar()
cal.prmonth(2016, 7)

# (d)
# it works
cal = calendar.LocaleTextCalendar(0, "GERMAN")
cal.pryear(2016)
# it works
cal = calendar.LocaleTextCalendar(0, "ITALIAN")
cal.pryear(2016)
# eccentric display
cal = calendar.LocaleTextCalendar(0, "JAPANESE")
cal.pryear(2016)

# (f) calendar.isleap (a year as integer) returns a boolean
