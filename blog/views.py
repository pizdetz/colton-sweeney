from django.shortcuts import render
from django.views import generic
from .models import BlogPost
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return render(
        request,
        'index.html',
        context={},
    )

class BlogListView(generic.ListView):
    model = BlogPost

    def get_queryset(self):
        return BlogPost.objects.order_by('-date')

class BlogDetailView(generic.DetailView):
    model = BlogPost

def portfolio(request):
    return render(
        request,
        'portfolio.html',
        context={},
    )
