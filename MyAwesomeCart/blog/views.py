from django.shortcuts import render
from .models import Blogpost
from django.http import HttpResponse

# Create your views here.
def index(request):
    mypost = Blogpost.objects.all()
    for item in mypost:
        print(item.category, item.product_id)
    return HttpResponse("We are at blog Home")

def blog_index(request,id):
    post = Blogpost.objects.filter(product_id=id)[0]
    print(post)
    return render(request, 'blog/blog_index.html', {'post': post})