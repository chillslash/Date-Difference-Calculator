from tkinter import *
from tkinter import ttk
import os
import datetime
import time

def end(event):
    os._exit(1)

def calculate(event):

    dif.delete('1.0', END)

    nummonth = 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31

    def existyear():
        try:
            year + 1
            return True
        except:
            return False

    def existmonth():
        try:
            month + 1
            return True
        except:
            return False

    def existweek():
        try:
            week + 1
            return True
        except:
            return False

    def existday():
        try:
            remday3 + 1
            return True
        except:
            return False

    while True:

        try:
            if str(firstd.get()).split("/")[0] == "today":
                day1 = int(str(datetime.datetime.now())[8:10])
                month1 = int(str(datetime.datetime.now())[5:7])
                year1 = int(str(datetime.datetime.now())[0:4])
                first = datetime.date(year1, month1, day1)

            else:
                day1, month1, year1 = int(str(firstd.get()).split("/")[0]), int(str(firstd.get()).split("/")[1]), int(str(firstd.get()).split("/")[2])
                first = datetime.date(year1, month1, day1)

            if str(secondd.get()).split("/")[0] == "today":
                day2 = int(str(datetime.datetime.now())[8:10])
                month2 = int(str(datetime.datetime.now())[5:7])
                year2 = int(str(datetime.datetime.now())[0:4])
                second = datetime.date(year2, month2, day2)
                break

            else:
                day2, month2, year2 = int(str(secondd.get()).split("/")[0]), int(str(secondd.get()).split("/")[1]), int(str(secondd.get()).split("/")[2])
                second = datetime.date(year2, month2, day2)
                break
        except:
            dif.insert('1.0', "The date entered is out of\nGregorian Calandar\nTry again!\n")
            return False


    if year1 == year2 and month1 == month2 and day1 == day2:
        dif.insert('1.0', "Same day")
        return None

    else:
        year = year2 - year1
        if (month1 > month2) or (month1 == month2 and day1 > day2):
            year -= 1
        if (month1 < month2) or (month1 == month2 and day1 <= day2):
            month = month2 - month1
        else:
            month = (12 - month1) + month2
        if day1 <= day2:
            remday2 = day2 - day1
        else:
            remday2 = (nummonth[month2 - 2] - day1) + day2
            month-=1
        if remday2 >= 7:
            week = int((remday2 - (remday2 % 7)) / 7)
            remday3 = remday2 % 7
        else:
            remday3 = remday2

    if year<0 or month<0 or remday3<0:
        dif.insert('1.0', "Try the other way around")
        return False

    day = int(str(second - first).split(" ")[0])
    years = float(day / 365)
    months = float(day / 30.4166666666666666666)
    weeks = float(day / 7)

    if year == 0: year = None
    if month == 0: month = None
    if remday3 == 0: remday3 = None

    dif.insert('1.0', "\nExact:\n{} year(s)\n{} month(s)\n{} week(s)\n{} day(s)".format(years, months, weeks, day))

    if existyear():
        if existmonth():
            if existweek():
                if existday():
                    dif.insert('1.0', "{} year(s)\n{} month(s)\n{} week(s)\n{} day(s)\n".format(year, month, week, remday3))
                else:
                    dif.insert('1.0', "{} year(s)\n{} month(s)\n{} week(s)\n".format(year, month, week))
            elif existday():
                dif.insert('1.0', "{} year(s)\n{} month(s)\n{} day(s)\n".format(year, month, remday3))
            else:
                dif.insert('1.0', "{} year(s)\n{} month(s)\n".format(year, month))
        elif existweek():
            if existday():
                dif.insert('1.0', "{} year(s)\n{} week(s)\n{} day(s)\n".format(year, week, remday3))
            else:
                dif.insert('1.0', "{} year(s)\n{} week(s)\n".format(year, week))
        else:
            if existday():
                dif.insert('1.0', "{} year(s)\n{} day(s)\n".format(year, remday3))
            else:
                dif.insert('1.0', "{} year(s)\n".format(year))


    elif existmonth():
        if existweek():
            if existday():
                dif.insert('1.0', "{} month(s)\n{} week(s)\n{} day(s)\n".format(month, week, remday3))
            else:
                dif.insert('1.0', "{} month(s)\n{} week(s)\n".format(month, week))
        elif existday():
            dif.insert('1.0', "{} month(s)\n{} day(s)\n".format(month, remday3))
        else:
            dif.insert('1.0', "{} month(s)\n".format(month))


    elif existweek():
        if existday():
            dif.insert('1.0', "{}week(s)\n{} day(s)\n".format(week, remday3))
        else:
            dif.insert('1.0', "{} week(s)\n".format(week))
    else:
        dif.insert('1.0', "{} day(s)\n".format(remday3))


root = Tk()

root.title("DDC")

Label(root, text='First date').grid(row=1, column=0, sticky=W)
Label(root, text='Second date\n(Try "today")').grid(row=2, column=0, sticky=W)

firstd = Entry(root)
firstd.grid(row=1, column=1, sticky=W)

Label(root, text='Format: day/month/year').grid(row=4, column=2, sticky=W)

secondd = Entry(root)
secondd.grid(row=2, column=1, sticky=W)

button = Button(root, text='Calculate')
button.bind("<Button-1>", calculate)
button.grid(row=4, column=0, sticky=W)
endbutton = Button(root, text='Stop')
endbutton.bind("<Button-1>", end)
endbutton.grid(row=4, column=1, sticky=W)

dif = Text(root, width=30, height=11)
dif.grid(row=1, column=2, rowspan=3, sticky=W)

dif.insert('1.0', "Welcome to Date Difference\nCalculator\nVersion 2.1")

root.mainloop()