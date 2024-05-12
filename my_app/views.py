from django.shortcuts import render,HttpResponseRedirect
from .models import *
from django.urls import reverse
# Create your views here.
def Home_page(request):
    if request.POST:
        name = request.POST.get('name')
        email = request.POST.get('email')
        teme = request.POST.get('teme')
        message = request.POST.get('message')

        data = MessageChat(
            name = name,
            email = email,
            teme = teme,
            message = message,
        )
        data.save()
        return HttpResponseRedirect(reverse('success') + '?success=true')
    return render(request,"index.html")

def SuccessView(request):
    alert_html = '''<div class="alert alert-warning alert-dismissible fade show" role="alert">
  <strong>Jeberildi!</strong> Sizdiń jazıp jebergen xabarińız jaberildi, telefon arqalı xabar beriledi, xabar jebergen ushın Sizge raxmet 😊👍
  <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
</div>'''
    return render(request, "index.html", {'alert_html': alert_html})