from django.shortcuts import render
from courses.models import Course
from django.shortcuts import HttpResponse
from django.views.generic import ListView
from django.db.models import Q



class SearchView(ListView):
    model = Course
    template_name = 'courses/search.html'
    #queryset = Course.objects.filter(name__icontains='Django') # new



    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Course.objects.filter(
            Q(name__icontains=query) | Q(price__icontains=query)
        )
        return object_list