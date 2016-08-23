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
	    msg="Out of range. displaying the number modulo 18446744073709551557"
	    t1=time.time()
	    result = fibln(n)
	    t2=time.time()
	    t=t2-t1
	    return render(request, 'nthfibo/index.html', {'form': form, 'errormsg':msg, 'result': result, 'time': t})
	    
    else:
	form = NthfiboForm()
   
    return render(request, 'nthfibo/index.html', {'form': form, 'result': result, 'time': t})

def fibln(n):
	M=18446744073709551557
	if n<= 1400:
		return fib_cache[n]%M
	k=n/2
	if (n%2==0):
		return (fibln(k)*fibln(k) + fibln(k-1)*fibln(k-1)) % M
	else:
		return (fibln(k)*fibln(k+1) + fibln(k-1)*fibln(k)) % M;
