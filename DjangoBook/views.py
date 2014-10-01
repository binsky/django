#from django.http import HttpResponse
#from django.template.loader import get_template
#from django.template import Context
from django.http import Http404
from django.shortcuts import render
import datetime

#def hello(request):
#	return HttpResponse("Hello world!")


def time(request):
    now = datetime.datetime.now()
    #t = get_template('time.html')
    #html = t.render(Context({'time' : now}))
    #return HttpResponse(html)
    return render(request, 'timeapp/time.html', {'time' : now, 'current_section' : 'Current time'})


def future(request, offset=0):
    if offset:
        try:
            offset = int(offset)
        except ValueError:
            raise Http404()
    elif request.POST.get("hours", ""):
        offset = request.POST.get("hours", "")
        try:
            offset = int(offset)
        except ValueError:
            return render(request, 'timeapp/wronginput.html', {'current_section' : 'Error'})
  
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render(request, 'timeapp/future.html', {'offset' : offset, 'hours_ahead' : dt, 'current_section' : 'Future'})


def home_method(request):
    return render(request, 'home.html', {'current_section' : 'Home'})
