#from django.http import HttpResponse
#from django.template.loader import get_template
#from django.template import Context
from django.core.mail import send_mail
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from DjangoBook.forms import ContactForm
import datetime

#def hello(request):
#	return HttpResponse("Hello world!")


def time(request):
    now = datetime.datetime.now()
    #t = get_template('time.html')
    #html = t.render(Context({'time' : now}))
    #return HttpResponse(html)
    return render(request, 'timeapp/time.html', {'time': now, 'current_section': request.path})


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
            return render(request, 'timeapp/wronginput.html', {'current_section': 'Error'})

    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render(request, 'timeapp/future.html',
                  {'offset': offset, 'hours_ahead': dt, 'current_section': request.path})


def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    k_list = []
    v_list = []
    for k, v in values:
        k_list.append(k)
        v_list.append(v)
        # html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    # return HttpResponse('<table>%s</table>' % '\n'.join(html))
    return render(request, 'meta.html', {'meta': zip(k_list, v_list)})


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@gmail.com'),
                ['gobrol@gmail.com'])
            return HttpResponseRedirect('/contacts/thanks/')
    else:
        form = ContactForm()
    return render(request, 'contacts_form.html', {'form': form, 'current_section': 'Contact us'})


def home_method(request):
    return render(request, 'home.html', {'current_section': request.path})
