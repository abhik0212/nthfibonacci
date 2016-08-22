from django.shortcuts import render
from .forms import NthfiboForm
from nthfibo.generator import *
import time

# Create your views here.
def index(request):
    result = None
    t = None
    if request.method == 'POST':
	form = NthfiboForm(request.POST)
	try:
	    n = int(request.POST.get('n'))
	    t1=time.time()
	    result = fib_cache[n]
	    t2=time.time()
	    t=t2-t1
     	    print result
	    print t
	except:
	    return Http404
    else:
	form = NthfiboForm()
    return render(request, 'nthfibo/index.html', {'form': form, 'result': result, 'time': t})
