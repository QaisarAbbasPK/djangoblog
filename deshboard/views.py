from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Posts, Article


# Create your views here.

def index(request):
    return render(request, 'deshboard/index.html')


def senddata(request):
  
    fname   = request.POST['fname']
    lname   = request.POST['lname']
    phone   = request.POST['phone']
    email   = request.POST['email']
    address = request.POST['address']

    postssend = Posts(fname=fname,lname=lname,phone=phone,email=email,address=address)
    result = postssend.save()

    if not result:
        return redirect('/data')

    else:
        return HttpResponse("you data wrong")



def data(request):
    post = Posts.objects.all()
    return render(request, 'deshboard/save.html', {'post':post})  

def delete(request, id):
    dels = Posts.objects.get(id=id)
    dels.delete()
    return redirect('/data')


def edit(request, id):
    edits = Posts.objects.get(id=id)
    return render(request, 'deshboard/edit.html',{'edits':edits})


def update(request):
  
    fname   = request.POST['fname']
    lname   = request.POST['lname']
    phone   = request.POST['phone']
    email   = request.POST['email']
    address = request.POST['address']
    ids = request.POST['id']

    postssend = Posts(fname=fname,lname=lname,phone=phone,email=email,address=address, id=ids)
    result = postssend.save()

    if not result:
        return redirect('/data')

    else:
        return HttpResponse("you data wrong")


def blog(request):
    post = Article.objects.all()
    return render(request, 'deshboard/blog.html',{'post':post})



def details(request, slug):
    detail = Article.objects.get(slug=slug)
    return render(request, 'deshboard/details.html',{'detail':detail})








    

