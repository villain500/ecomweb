from asyncio.windows_events import NULL
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render,redirect
from Slider_Blogs_and_others.models import Slider,Blog,Visitors
from productmanagement.models import Product,Categories,Cart,Placed_Order
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse

# Home page programs starts here
def index(request):
    slider=Slider.objects.all()
    count_product=Product.objects.all().count()
    count_orders=Placed_Order.objects.all().count()
    # user_counter=request.user.count()
    ip = get_ip(request)
    visitors=Visitors(Visitors=ip)
    print(ip)
    count_visitor=Visitors.objects.filter(Q(Visitors__icontains=ip))
    if len(count_visitor)==1:
        print('user exist')
    elif len(count_visitor)>1:
        print('user exist more')
    else:
        visitors.save()
        print('user is added')
    counted_visitors=Visitors.objects.all().count()
    print('total user', count_product)
    data={
        'slider':slider,
        'count_product':count_product,
        'counted_visitors':counted_visitors,
        'count_orders':count_orders
    }

    return render(request,'index.html',data)

#Web page visitors ip getting program starts here
def get_ip(request):
        address = request.META.get('HTTP_X_FORWARDED_FOR')
        if address:
            ip=address.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip


# Ecomweb Blogs page Program starts here
def blogs(request):
    blog=Blog.objects.all()
    paginator=Paginator(blog,6)
    page_num=request.GET.get('pagenumber')
    page=paginator.get_page(page_num)
    total_page=page.paginator.num_pages
    data={
    'blog':page,
    'totalpage':[n+1 for n in range(total_page)]
    }
    return render(request,'blogs.html',data)


# Ecomweb Blog viewing page Program starts here
def fulllblog(request,slug):
    blog=Blog.objects.get(Blog_slug=slug)
    data={
    'blog':blog
    }
    return render(request,'fullblog.html',data)



# Sign up page programs starts here
def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        phonenum=request.POST['phonenum']
        password=request.POST['password']
        confirm_pass=request.POST['confirm_pass']

        if len(phonenum)<11 or len(phonenum)>11:
            messages.warning(request,"Please enter a valid phone number")
        elif password != confirm_pass:
            messages.warning(request,"Password didn't matched")
        elif len(password) < 5:
            messages.warning(request,"Your Password is less than 6 characters")
        
        myuser=User.objects.create_user(username,email,password)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,"Successfully signed up. Please Login your account....")
        return redirect('login')
    return render(request,'signup.html')


# Log in and log out page programs starts here
def login_here(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')

        user = authenticate(username=email,password=password)
        print(user)
        if user is not None:
            login(request, user)
            messages.success(request,'Login in successfull')
            return redirect('home')
    return render(request,'login.html')



def log_out(request):
    logout(request)
    messages.warning(request,'Logged out')
    return redirect('login')



# All Products page programs starts here
def allproducts(request):
    categories=Categories.objects.all()
    category=request.GET.get("category")
    if category==None:
        allproducts=Product.objects.all()
    else:
        allproducts=Product.objects.filter(Category__name=category)


    # Product searching Prorams
    search=request.GET.get("search")
    if search!=None:
            allproducts=Product.objects.filter(Product_Name__icontains=search)
    

    data={
        'categories':categories,
        'allproducts':allproducts,
    }
    return render(request,'allproducts.html',data)



# Product view page programs starts here
def prodview(request):
    prodview=request.GET.get('Product-name')
    if prodview!=NULL:
        allproducts=Product.objects.filter(Product_Name=prodview)
    add_to_cart(request)
    data={
        'allproducts':allproducts
    }
    return render(request,'prodview.html',data)


# Add to cart programs
def add_to_cart(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            prod_id=int(request.POST.get('product_id'))
            product_id=Product.objects.get(id=prod_id)
            if (product_id):
                if (Cart.objects.filter(Username=request.user,Product=product_id)):
                    return messages.warning(request,'Sorry! Product already in cart, please go to cart page and increase the quantity')  

                else:
                    Cart.objects.create(Username=request.user,Product=product_id)
                    return messages.success(request,'Product added in cart successfully, If you need to increase quantity than go to Cart page')      
        data={}    
    else:
        return messages.warning(request,"Please login first, else you can't add products in cart")
    return JsonResponse(data)

    

    
# Cart page programs starts here
@login_required(login_url='login')
def cart_page(request):
    if request.user.is_authenticated:
        user=request.user
        cart=Cart.objects.filter(Username=user)
    else:
        return redirect ('login')

    amount=0
    cart_products=[p for p in Cart.objects.all() if user == user]
    if cart_products:
        for p in cart_products:
            products_total=(p.Quantity * p.Product.Price)
            amount+=products_total
        data={
                'cart':cart,
                'products_total':products_total,
                'amount':amount
            }
        return render(request, 'cart.html',data)
    else:
        return render(request,'empty_cart.html')


# quantity increasing programs starts here
def increase_quantity(request):
    if request.method == "GET":
        prod_id=request.GET['prod_id']
        c=Cart.objects.get(Q(Product=prod_id) & Q(Username = request.user))
        c.Quantity+=1
        c.save()
        amount=0
        cart_products=[p for p in Cart.objects.all() if p.Username == request.user]
        for p in cart_products:
            products_total=(p.Quantity * p.Product.Price)
            amount+=products_total
        data={
            'quantity':c.Quantity,
            'amount':amount
        }
        return JsonResponse(data)
    



# quantity decreasing programs starts here
def decrease_quantity(request):
    if request.method == "GET":
        prod_id=request.GET['prod_id']
        c=Cart.objects.get(Q(Product=prod_id) & Q(Username = request.user))
        c.Quantity-=1
        c.save()
        amount=0
        cart_products=[p for p in Cart.objects.all() if p.Username == request.user]
        for p in cart_products:
            products_total=(p.Quantity * p.Product.Price)
            amount+=products_total
        data={
            'quantity':c.Quantity,
            'amount':amount
        }
        return JsonResponse(data)
    



# quantity decreasing programs starts here
def remove_quantity(request):
    if request.method == "GET":
        prod_id=request.GET['prod_id']
        c=Cart.objects.get(Q(Product=prod_id) & Q(Username = request.user))
        c.delete()
        amount=0
        cart_products=[p for p in Cart.objects.all() if p.Username == request.user]
        for p in cart_products:
            products_total=(p.Quantity * p.Product.Price)
            amount+=products_total
        data={
            'amount':amount
        }
        return JsonResponse(data)
    


# About us programs starts here
def About_us(request):
    return render(request,'about.html')    



# About us programs starts here
def privacy_policy(request):
    return render(request,'privacypolicy.html')    



# Checkout programs starts here
@login_required(login_url='login')
def checkout(request):
    user=request.user
    cart_items=Cart.objects.filter(Username=user)
    cart_products=[p for p in Cart.objects.all() if p.Username == request.user]
    amount=0
    Shiping_amount=70
    if cart_items:
        for p in cart_products:
            products_total=(p.Quantity * p.Product.Price)
            amount+=products_total
        total_amount=amount+Shiping_amount
        data={
            'total_amount':total_amount,
            'cart_items':cart_items
        }
    if request.method=='POST':
        name=request.POST.get('name')
        city=request.POST.get('city')
        address=request.POST.get('address')
        phnnum=request.POST.get('phnnum')
        zipcode=request.POST.get('zipcode')
        for c in cart_items:
            Placed_Order(Username=user,Name=name,City=city,Full_Address=address,Phone_Number=phnnum,Zipcode=zipcode ,Product=c.Product,Quantity=c.Quantity).save()
            c.delete()
            return redirect('orders')

    return render(request,'checkout.html',data)    



def orders(request):
    orders=Placed_Order.objects.filter(Username=request.user)
    return render(request, 'orders.html',{'orders':orders})