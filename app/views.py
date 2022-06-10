from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib import messages
from app.forms import CustomerRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login , logout , authenticate
from .models import Product , Seller ,Customer

# Create your views here.


#for login
def loginPage(request):
    page = "login"
    if request.user.is_authenticated:  #if user is already logged in so it redirect to home except login page again 
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Your username doesn't exists!")
            
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"User does not exist.")

    context = {'page':page}
    return render(request , 'app/login_register_page.html' , context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    page = 'register'
    form = CustomerRegistrationForm()
    if request.method == "POST":
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request , user)
            return redirect('home')

        #messages.error(request, "bad Credentails")
        #return redirect('register')
    context ={'form':form, 'page':page}
    return render(request,'app/login_register_page.html' , context)


def home(request):
    pro = Product.objects.all()
    slr = Seller.objects.all()
    return render(request,'app/home.html',{'products':pro,'seller':slr})

@login_required(login_url='login')
def buy(request,pk):
    print(pk)
    pro = Product.objects.get(pk=pk)

    if request.method == "POST":
        name = request.POST['name']
        address = request.POST['address']
        phone = request.POST['phone']
        quantity = int(request.POST['quantity'])
        
        by = Customer(name=name,address=address,phone=phone)
        by.save()
        amount = float(pro.price)
        pid = pro.id
        pn = pro.title
        dis = pro.description
        price = amount
        pro_quantity =quantity
        pro_total = amount*quantity         
        slr = Seller.objects.all()
        data = {'pname':pn,'pid':pid,'pprice':price,'bname':name,'baddress':address,'bphone':phone,'pdis':dis,'pquantity':pro_quantity, 'ptotal':pro_total}
        return render(request, 'app/pdf.html', {'data': data, 'seller': slr})

    return render(request, 'app/buy.html')

@login_required(login_url='login')
def pdf(request):
    seller = Seller.objects.all()
    return render(request,'app/pdf.html',{'seller':seller})

