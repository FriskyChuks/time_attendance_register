from django.shortcuts import render,redirect
from django.contrib import messages
import datetime

from .models import *


def home(request):
    msg = ''
    last_clock, clock_out = None, False
    user = request.user
    try:
        last_clock = ClockInClockOut.objects.filter(user_id=user.id).last()
    except:
        pass
    if not last_clock:
        clock_out=True
    if last_clock:
        if last_clock.clock_out:
            clock_out = True
    context = {"clock_out":clock_out, 'last_clock':last_clock, "msg":msg}
    return render(request, 'main/home.html',context)


def clock_in_view(request):
    time = datetime.datetime.now()
    ClockInClockOut.objects.create(
        user_id=request.user.id,clock_in=datetime.datetime.now())
    messages.info(request, f'You Clocked in at {time}')
    return redirect('attendance_records')


def clock_out_view(request):
    time = datetime.datetime.now()
    ClockInClockOut.objects.filter(user_id=request.user.id, clock_out=None).update(
                                        clock_out=datetime.datetime.now())
    messages.success(request, f"You Clocked out at {time}")
    return redirect('attendance_records')


def attendance_records_view(request):
    clocks = ClockInClockOut.objects.filter(user_id=request.user.id).order_by('-id')
    for clock in clocks:
        print('In: ', clock.clock_in, 'out: ', clock.clock_out)
    context = {'clocks':clocks}
    return render(request,'main/attendance_record.html',context)