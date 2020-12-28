from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import User, Receipt, Shop

class IndexView(generic.TemplateView):
    template_name = 'spending/index.html'

class LoginView(generic.TemplateView):
    template_name = 'spending/login.html'

class CreateUserView(generic.TemplateView):
    template_name = 'spending/createUser.html'

class UserView(generic.DetailView):
    model = User
    template_name = 'spending/user.html'

def createReceipt(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    shops = Shop.objects.all()
    return render(request, 'spending/createReceipt.html', {'user': user, 'shops': shops})

def postCreateReceipt(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    shop = get_object_or_404(Shop, pk=request.POST['shop'])
    totalSum = request.POST['sum']
    date = request.POST['date']
    receipt = Receipt(totalSum = totalSum, receiptDate = date, user = user, shop = shop)
    receipt.save()
    return HttpResponseRedirect(reverse('spending:user', args=(user_id,)))

def postlogin(request):
    username = request.POST['username']
    password = request.POST['password']
    query = "SELECT * FROM spending_user WHERE username='%s' AND password='%s'" % (username, password)
    userSet = User.objects.raw(query)
    try:
        user = userSet[0]
    except:
        return render(request, 'spending/login.html', {'error_message': 'Wrong username or password!'})
    else:
        return HttpResponseRedirect(reverse('spending:user', args=(user.id,)))

def postCreateUser(request):
    if request.POST['password'] != request.POST['passwordRepeat']:
        return render(request, 'spending/createUser.html', {'error_message': 'Passwords don\'t match'})
    try:
        username = request.POST['username']
        query = "SELECT * FROM spending_user WHERE username='%s'" % username
        userSet = User.objects.raw(query)
        user = userSet[0]
    except:
        user = User(
            username=request.POST['username'],name=request.POST['name'],ssn=request.POST['ssn'],address=request.POST['address'],password=request.POST['password']
        )
    else:
        return render(request, 'spending/createUser.html', {'error_message': 'Username already exists'})

    user.save()
    return HttpResponseRedirect(reverse('spending:login'))

def addStyle(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user.nameStyle = request.POST['style']
    user.save()
    return HttpResponseRedirect(reverse('spending:user', args=(user.id,)))



