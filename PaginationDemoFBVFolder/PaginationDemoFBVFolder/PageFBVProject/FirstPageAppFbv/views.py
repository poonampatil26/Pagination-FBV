from django.shortcuts import render
from .models import Student
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def studentpagination_view(request):
    records=Student.objects.all()
    p = Paginator(records,4)
    page = request.GET.get('page', 1)
    try:
        data = p.page(page)
    except PageNotAnInteger:
        data = p.page(1)
    except EmptyPage:
        data = p.page(p.num_pages)

    return render(request, 'FirstPageAppFbv/show.html', {'data': data})

