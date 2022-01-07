from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
import datetime
from .models import contact_us
# Create your views here.
def home(request):
    return render(request, "index.html")


def contact(request):
    return render(request, "contact.html")


def get_about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def pricing(request):
    return render(request, 'pricing.html')


def portfolio(request):
    return render(request, 'portfolio.html')


def blog(request):
    return render(request, 'blog.html')


def gallery(request):
    return render(request, 'gallery.html')


def portfolio_details(request):
    return render(request, 'portfolio-details.html')


def blog_details(request):
    return render(request, 'blog-details.html')


def get_contact_details(request):
    #import pdb; pdb.set_trace()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        website = request.POST.get('website')
        message = request.POST.get('message')
        obj = contact_us(name=name, email=email, website=website, message=message).save()
        return
    #return reverse("home")
        #return render(request, {"data":obj.name})
        #return HttpResponse(ok)
    # now = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    # return HttpResponse(html,)