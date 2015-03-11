from django.template.loader import get_template
from django.template import Context

from django.shortcuts import render_to_response

from django.http import HttpResponse, Http404
import datetime

def hello(request):
    return HttpResponse("Hello world<p>Welcome to the page at %s<p>Header info: %s" 
            % (request.path, request.META))

def current_datetime(request):
    now = datetime.datetime.now()

    # 1. original method
    #html = "<html><body>It is now %s.</body></html>" % now
    #return HttpResponse(html)

    # 2. use the template to get the html string
    #t = get_template('current_datetime.html')
    #html = t.render(Context({'current_date': now}))
    #return HttpResponse(html)

    # 3. shortcut of get_template() and render() and HrrtResponse()
    #return render_to_response('current_datetime.html', {'current_date': now})

    # 4. shortcut of Context parameter
    current_date = now
    return render_to_response('current_datetime.html', locals())

    # 4. shortcut of Context parameter
    #current_date = now
    #return render_to_response('child_dir/current_datetime.html', locals())

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    #assert False
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    #html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    #return HttpResponse(html)
    return render_to_response('hours_ahead.html', {'hour_offset': offset, 'next_time': dt})

