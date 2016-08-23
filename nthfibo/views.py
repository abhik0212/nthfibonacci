from django.shortcuts import render
from .forms import NthfiboForm
from nthfibo.generator import *
import time

# Create your views here.
def index(request):
    result = None
    t = None
    msg=None
    if request.method == 'POST':
	form = NthfiboForm(request.POST)
	try:
	    n = int(request.POST.get('n'))
	    if n<=0:
		msg="Try a positive integer"
		return render(request, 'nthfibo/index.html', {'form': form, 'errormsg':msg})
	    t1=time.time()
	    result = fib_cache[n]
	    t2=time.time()
	    t=t2-t1
     	    #print result
	    #print t
	except:
	    msg="Out of range"
    else:
	form = NthfiboForm()
    if msg:
	return render(request, 'nthfibo/index.html', {'form': form, 'errormsg':msg})
    else:
    	return render(request, 'nthfibo/index.html', {'form': form, 'result': result, 'time': t})
