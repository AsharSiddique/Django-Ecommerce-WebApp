from django.shortcuts import render, redirect, get_object_or_404
from .models import Electronics, Garments, Groceries, Products, Shoppingcarts, Customers, Cartcontainers, Orders
from django.contrib.auth import authenticate, login, logout
from .forms import SigninForm, SignupForm
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.db import connection

# Create your views here.

def index(request):
    electronics = Electronics.objects.all()
    garments = Garments.objects.all()
    groceries = Groceries.objects.all()

    electronic_ids = [electronic.prodid.prodid for electronic in electronics]
    garment_ids = [garment.prodid.prodid for garment in garments]
    grocery_ids = [grocery.prodid.prodid for grocery in groceries]

    electronics_prod =[Products.objects.get(prodid=str(id)) for id in electronic_ids]
    garments_prod =[Products.objects.get(prodid=str(id)) for id in garment_ids]
    groceries_prod =[Products.objects.get(prodid=str(id)) for id in grocery_ids]

    for item in electronics_prod:
         item.pimage = item.pimage.decode('utf-8')
    for item in garments_prod:
        item.pimage = item.pimage.decode('utf-8')
    for item in groceries_prod:
        item.pimage = item.pimage.decode('utf-8')


    context = {
        'electronics': electronics_prod,
        'garments': garments_prod,
        'groceries': groceries_prod,
    }
    return render(request, 'index.html', context)

def customer_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            cpassword = form.cleaned_data['cpassword']
            cre_password = form.cleaned_data['cre_password']
            print(cpassword)
            print(cre_password)
            
            form.save()
            return redirect('customer_signin')
    else:
        form = SignupForm()
    context = {
        'form': form
    }
    return render(request, 'customer_signup.html', context=context)


def customer_signin(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            cemail = form.cleaned_data['cemail']
            cpassword = form.cleaned_data['cpassword']
            user = authenticate(request, cemail=cemail, cpassword=cpassword)
            if user is not None:
                login(request, user)
                customer_id= request.user.custid
                return redirect('product_view', customer_id=customer_id)           
            else:
                form.add_error(None, 'Invalid email or password')
                return render(request, 'customer_signin.html', {'form': form})
    else:
        form = SigninForm()
    return render(request, 'customer_signin.html', {'form': form})

def customer_profile(request, customer_id):
    customer = Customers.objects.get(custid=customer_id)
    orders = Orders.objects.all()
    customer_products = []
    customer_orders = []
    for order in orders:
        if order.custid.custid == customer_id:
            customer_products.append(order.prodid)
            customer_orders.append(order)

    for customer_product in customer_products:
        customer_product.pimage = customer_product.pimage.decode('utf-8')
    print(customer)
    print(customer_orders)
    
    context = {'customer': customer,
               'customers_products': customer_products,
               'customer_orders': customer_orders,
    }

    return render(request, 'customer_profile.html', context)

    

def product_view(request, customer_id):
    if request.method == 'POST':
        current_customer = Customers.objects.get(custid=customer_id)
        # orders = Orders.objects.get(custid=current_customer)
        # products = Products.objects.get(prodid=orders.prodid.prodid)
        print(customer_id)
        # context = {
        #     'products': products,
        #     'customer': current_customer,
        # }
        

        return render(request, 'customer_profile.html', {'customer': current_customer})
    
    electronics = Electronics.objects.all()
    garments = Garments.objects.all()
    groceries = Groceries.objects.all()
    products = Products.objects.all()
    eletronic_prod_id = {}
    garment_prod_id = {}
    grocery_prod_id = {}
        
    electronic_ids = [electronic.prodid.prodid for electronic in electronics]
    garment_ids = [garment.prodid.prodid for garment in garments]
    grocery_ids = [grocery.prodid.prodid for grocery in groceries]

    product_id_rating = [(product.prodid, product.rating) for product in products]
    for product_id, prodcut_rating in product_id_rating:
        if product_id in electronic_ids:
            eletronic_prod_id[product_id] = float(prodcut_rating)
        elif product_id in garment_ids:
            garment_prod_id[product_id] = float(prodcut_rating)
        elif product_id in grocery_ids:
            grocery_prod_id[product_id] = float(prodcut_rating)

    sorted_electronic_prod_id = dict(sorted(eletronic_prod_id.items(), key=lambda item: item[1], reverse=True))
    sorted_garment_prod_id = dict(sorted(garment_prod_id.items(), key=lambda item: item[1], reverse=True))
    sorted_grocery_prod_id = dict(sorted(grocery_prod_id.items(), key=lambda item: item[1], reverse=True))

    electronics_prod = [Products.objects.get(prodid=str(id)) for id in sorted_electronic_prod_id.keys()]
    garments_prod = [Products.objects.get(prodid=str(id)) for id in sorted_garment_prod_id.keys()]
    groceries_prod = [Products.objects.get(prodid=str(id)) for id in sorted_grocery_prod_id.keys()]

    for item in electronics_prod:
        item.pimage = item.pimage.decode('utf-8')
    for item in garments_prod:
        item.pimage = item.pimage.decode('utf-8')
    for item in groceries_prod:
        item.pimage = item.pimage.decode('utf-8')


    context = {
        'electronics': electronics_prod,
        'garments': garments_prod,
        'groceries': groceries_prod,
        'customer_id': customer_id,
    }
    return render(request, 'product_view.html', context)

def product_detail(request, category_name, customer_id):
    if request.method == 'POST':
        custom_method = request.GET.get('custom_method')
        if custom_method == 'POST_RATING':
            
            prodid = request.POST.get('prodid')
            rating = request.POST.get('rating')

            # Construct the raw SQL query
            sql_query = """
                UPDATE products
                SET rating = (rating * persons_rated + %s) / (persons_rated + 1),
                    persons_rated = persons_rated + 1
                WHERE prodid = %s
            """

            # Execute the raw SQL query
            with connection.cursor() as cursor:
                cursor.execute(sql_query, [rating, prodid])

            return redirect('product_detail', category_name=category_name, customer_id=customer_id)

        else:
            product_id = request.POST.get('prodid')
            product_object = Products.objects.get(prodid=product_id)        
            customer_object = Customers.objects.get(custid=customer_id)
            shoppingcart_object = Shoppingcarts.objects.create(custid=customer_object)
            cartcontainer_object = Cartcontainers.objects.create(cartid=shoppingcart_object, prodid=product_object)
            return redirect('product_detail', category_name=category_name, customer_id=customer_id)

        '''
        product_id = request.POST.get('prodid')
        customer_instance = get_object_or_404(Customers, custid=customer_id)
        product_instance = get_object_or_404(Products, prodid=int(product_id))
        shoppingcarts = Shoppingcarts.objects.all() 
        for shoppingcart in shoppingcarts:
            if int(customer_id) == shoppingcart.custid.custid:
                cartcontainers_instance = get_object_or_404(Cartcontainers, cartid=shoppingcart.cartid)
                print("old customer")
                if int(product_id) == cartcontainers_instance.prodid.prodid:
                    print('product already in cart')
                else:
                    shoppingcart_instance = get_object_or_404(Shoppingcarts, custid = customer_instance)
                    Cartcontainers.objects.create(prodid=product_instance, cartid=shoppingcart_instance)
                    print('cart container created')
            elif int(customer_id) != shoppingcart.custid.custid:
                print("new customer")
                Shoppingcarts.objects.create(custid=customer_instance)
                shoppingcart_instance = get_object_or_404(Shoppingcarts, custid = customer_instance)
                Cartcontainers.objects.create(prodid=product_instance, cartid=shoppingcart_instance)

        return redirect('product_detail', category_name=category_name, customer_id=customer_id)
        '''
    elif request.method == 'GET':                
        if category_name == 'category_electronics':
            electronics = Electronics.objects.all()
            electronic_ids = [electronic.prodid.prodid for electronic in electronics]
            electronics_prod =[Products.objects.get(prodid=str(id)) for id in electronic_ids]
            for item in electronics_prod:
                path = 'media/' + str(item.pspecs)
                with open(path, 'r') as file:
                    file_contents = file.read()
                item.pspecs = file_contents
                item.pimage = item.pimage.decode('utf-8')
            context = {
            'products': electronics_prod,
            'customer_id': customer_id,
            'category_name': 'category_electronics',
            }
            return render(request, 'product_detail.html', context=context)
        
        elif category_name == 'category_garments':
            garments = Garments.objects.all()
            garment_ids = [garment.prodid.prodid for garment in garments]
            garments_prod =[Products.objects.get(prodid=str(id)) for id in garment_ids]
            for item in garments_prod:
                path = 'media/' + str(item.pspecs)
                with open(path, 'r') as file:
                    file_contents = file.read()
                item.pspecs = file_contents
                item.pimage = item.pimage.decode('utf-8')
            context = {
            'products': garments_prod,
            'customer_id': customer_id,
            'category_name': 'category_garments',
            }
            return render(request, 'product_detail.html', context=context)
        
        else:
            groceries = Groceries.objects.all()
            grocery_ids = [grocery.prodid.prodid for grocery in groceries]
            groceries_prod =[Products.objects.get(prodid=str(id)) for id in grocery_ids]
            for item in groceries_prod:
                path = 'media/' + str(item.pspecs)
                with open(path, 'r') as file:
                    file_contents = file.read()
                item.pspecs = file_contents
                item.pimage = item.pimage.decode('utf-8')
            context = {
            'products': groceries_prod,
            'customer_id': customer_id,
            'category_name': 'category_groceries',
            }
            return render(request, 'product_detail.html', context=context)

def order_confirmation(request):
    return render(request, 'order_confirmation.html')
    
def shopping_history(request):
    return render(request, 'shopping_history.html')

def customer_signout(request, customer_id):
    user = Customers.objects.get(custid=customer_id)
    logout(request, user)
    return redirect('customer_signout.html')

def cart(request, customer_id, category_name):
    if request.method == 'POST':
        custom_method = request.POST.get('custom_method')
        products = request.POST.get('products')
        if custom_method == 'POST_CHECKOUT':
            customer_shopping_carts = []
            cart_containers = []
            product_ids = []
            shopping_carts = Shoppingcarts.objects.all()
            for shopping_cart in shopping_carts:
                # print(shopping_cart)
                if shopping_cart.custid.custid == customer_id:
                    # print(shopping_cart.custid.custid)
                    customer_shopping_carts.append(shopping_cart)

            for customer_shopping_cart in customer_shopping_carts:
                cart_containers.append(Cartcontainers.objects.get(cartid=customer_shopping_cart))
            for cart_container in cart_containers:
                if cart_container.prodid.prodid not in product_ids:
                    product_ids.append(cart_container.prodid.prodid)
            print(product_ids)

            customer_object = Customers.objects.get(custid=customer_id)
            for id in product_ids:
                product_object = Products.objects.get(prodid=id)
                Orders.objects.create(custid=customer_object, prodid=product_object, orderquantity=1)

            for shopping_cart in shopping_carts:
                if shopping_cart.custid.custid == customer_id:
                    s = Shoppingcarts.objects.get(cartid=shopping_cart.cartid)
                    s.delete()
            
            return redirect('customer_profile', customer_id=customer_id)
            
        product_id = request.POST.get('prodid')
        print(product_id)
        cart_objects = []
        cart_container_objects = []
        customer_carts = []        
        cart_container_objects = Cartcontainers.objects.all()
        for cart_container_object in cart_container_objects:
            if cart_container_object.prodid.prodid == int(product_id):                
                cart_objects.append(cart_container_object.cartid)        
        for cart_object in cart_objects:
            if cart_object.custid.custid == customer_id:              
                customer_carts.append(cart_object)
        for customer_cart in customer_carts:                    
            s = Shoppingcarts.objects.get(cartid=customer_cart.cartid)
            s.delete()
            print(s)
            '''
            c = Cartcontainers.objects.get(cartid=customer_cart)
            c.delete
            print(c)
            '''
        return redirect('cart', customer_id=customer_id, category_name=category_name)
    else:
        customer_cart_ids = []
        customer_carts = []
        product_ids = []
        products = []

        customer_object = Customers.objects.get(custid=customer_id)
        shopping_carts = Shoppingcarts.objects.all()
        for shopping_cart in shopping_carts:
            if shopping_cart.custid == customer_object:
                customer_carts.append(shopping_cart)
        customer_object = Customers.objects.get(custid=customer_id)
        shopping_carts = Shoppingcarts.objects.all()
        for shopping_cart in shopping_carts:
            if shopping_cart.custid == customer_object:
                customer_carts.append(shopping_cart)

        for customer_cart in customer_carts:
            customer_cart_ids.append(customer_cart.cartid)
            customer_cart_container =  Cartcontainers.objects.get(cartid=customer_cart)
            product_id = customer_cart_container.prodid.prodid
            if product_id not in product_ids:
                product_ids.append(product_id)
                print(product_id)
        
        cart_price = 0
        for id in product_ids:
            product = Products.objects.get(prodid=id)
            cart_price += product.pprice
            product.pimage = product.pimage.decode('utf-8')
            products.append(product)
        
        customer = Customers.objects.get(custid=customer_id)
        context = {'products': products, 'customer': customer, 'cart_price': cart_price, 'category_name': category_name, 'customer_id': customer_id}
        return render(request, 'cart.html', context)
        
    