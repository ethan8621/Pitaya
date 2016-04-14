from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'pwd'

    def get_queryset(self):
        """ 
        Return the last five published question. (not including those set to be
        published in the future)
        """
        pwd = 'userregister:index.html'
        return pwd
'''
def index(request):
    pwd = "userregister:index.html"
    context = {
        'pwd': pwd,
    }
    return render(request, 'index.html', context)
'''