from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from . models import CustomerDetails
from django.contrib.auth.decorators import login_required
from Shop.models import Categories,GreeneryProducts
from Cart.models import Orders
# Create your views here.

def register(request):
    if request.method == 'POST':
        f_name = request.POST['c_fname']
        l_name = request.POST['c_lname']
        mail = request.POST['c_email']
        contact = request.POST['c_phone']
        passwd = request.POST['c_password']
        cpasswd = request.POST['con_password']
        address = request.POST['c_message']
        photo = request.FILES['image']
        if passwd==cpasswd:
            if User.objects.filter(username=mail).exists():
                messages.info(request, 'User already exists')
            else:
                user = User.objects.create_user(username=mail, password=passwd)
                customer = CustomerDetails(id=user, first_name=f_name, last_name=l_name, phone=contact,
                                           address=address, photo=photo)
                user.save()
                customer.save()
                return redirect('Customer:login')
        else:
            messages.info(request, 'Mismatch Password')
    return render(request, 'Register.html')



def login(request):
    if request.method == 'POST':
        mail = request.POST['c_email']
        password = request.POST['c_password']
        
        if mail == 'admin@123' and password == '1234':
            request.session['aid'] = mail
            cate_count = Categories.objects.all().count()
            product_count = GreeneryProducts.objects.all().count()
            order_count = Orders.objects.all().count()
            user_count = User.objects.all().count()
            
            return render(request,'admin.html',{'category':cate_count,'product':product_count,'order':order_count,'user':user_count})
        else:
            user = auth.authenticate(username=mail, password=password)

        if user is not None and CustomerDetails.objects.filter(id=user.id).exists():
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials')
    return render(request, 'Login.html')


def Logout(request):
    auth.logout(request)
    return redirect("/")

@login_required(login_url='Customer:login')
def Customer_Profile(request):
    profile = CustomerDetails.objects.get(id=request.user.id)
    return render(request, 'Profile.html', {'profile':profile})

#admin section start


def view_category(request):
    if 'aid' in request.session:
        if request.method == 'POST':
            category = request.POST.get('category')
            link = request.POST.get('link')

            if category and link:

                if Categories.objects.filter(category=category).exists():
                    return HttpResponse("<script>alert('Category already exists!'); window.history.back();</script>")
                try:
                    Categories.objects.create(category=category, link=link)
                except:
                    return HttpResponse("<script>alert('Failed to add category! Make sure slug is unique.'); window.history.back();</script>")

        cate = Categories.objects.all()
        return render(request, 'view_category.html', {'cate': cate})

    return HttpResponse("<script>alert('Unauthorized access.'); window.location.href='/login/';</script>")