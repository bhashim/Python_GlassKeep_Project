from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


def index(request):
    return render(request, 'index.html')


def register(request):
    # print(request.POST)
    error = False
    if len(request.POST['first_name']) < 2:
        error = True
        messages.error(
            request, "First name must be a minimum length of three characters!")

    if request.POST['first_name'].isalpha() == False:
        error = True
        messages.error(
            request, "First name cannot have a number in it or be blank!")

    if len(request.POST['last_name']) < 2:
        error = True
        messages.error(
            request, "Last name must be a minimum length of three characters!")

    if request.POST['last_name'].isalpha() == False:
        error = True
        messages.error(
            request, "Last name cannot have a number in it or be blank!")

    if len(request.POST['email']) < 7:
        error = True
        messages.error(
            request, "Email must be a minimum length of three characters!")

    if not EMAIL_REGEX.match(request.POST['email']):
        error = True
        messages.error(request, "Email must be a valid email address!")

    if len(request.POST['password']) < 8:
        error = True
        messages.error(
            request, "Password must be a minimum length of eight characters!")

    if request.POST['password'] != request.POST['confirm_password']:
        error = True
        messages.error(request, "Passwords must match!")

    if User.objects.filter(email=request.POST['email']):
        error = True
        messages.error(request, "User already exists!")

    if error:
        return redirect('/')

    hashed = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    decoded_hash = hashed.decode('utf-8')

    user = User.objects.create(
        first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=decoded_hash)
    print(user)
    request.session['u_id'] = user.id
    request.session['u_fname'] = user.first_name
    return redirect('/dashboard')


def login(request):
    user_list = User.objects.filter(email=request.POST['email'])
    if not user_list:
        messages.error(request, "Invalid credentials!")
        return redirect('/')

    user = user_list[0]

    if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
        request.session['u_id'] = user.id
        request.session['u_fname'] = user.first_name
        return redirect('/dashboard')
    else:
        messages.error(request, "Invalid credentials!")
        return redirect('/')


def dashboard(request):
    print("*" * 80)
    if request.session['u_id'] == None:
        return redirect('/')

    print(request.session['u_fname'], 'u_fname')

    return render(request, 'dashboard.html')


def logout(request):
    request.session['u_id'] = None
    messages.error(request, "You have successfully logged out")
    return redirect('/')


def about(request):
    return render(request, 'about.html')


def purchase_confirmation(request):
    return render(request, 'purchase.html')


def purchase(request):
    print(request.POST)
    errors = Purchase.objects.basic_validator(request.POST)
    print(errors)
    # check if any errors were found
    if len(errors) > 0:
        for key, value in errors.items():
            # put each message in the messages.error
            if key != "field_missing":
                messages.error(request, value, extra_tags=key)
        return redirect("/purchase")

    else:
        u_id = request.session['u_id']
        new_purchase = Purchase.objects.create(
            name=request.POST["purchase_name"],  email=request.POST["email"], shipping_address=request.POST["shipping_address"], quantity=request.POST["quantity"], user_id_creator=u_id)
        new_purchase_id = new_purchase.id
        return redirect(f"/purchase/{new_purchase_id}")


def display_purchase(request, purchase_id):
    print("Display")
    new_purchase = Purchase.objects.get(id=purchase_id)
    user_list = User.objects.filter(id=new_purchase.user_id_creator)
    if not user_list:
        messages.error(request, "Invalid credentials!")
        return redirect('/')

    user = user_list[0]
    user_name = user.first_name + " " + user.last_name
    context = {
        "purchase_html": new_purchase,
        "creator_name": user_name
    }
    return render(request, "purchase_confirmation.html", context)


def confirm_display_purchase(request, purchase_id):
    print(request.POST)
    print("confirm_display_purchase")
    # errors = Purchase.objects.basic_validator(request.POST)
    # print(errors)
    # if len(errors) > 0:
    #     for key, value in errors.items():
    #         messages.error(request, value, extra_tags=key)
    #     return redirect(f"/purchase/{purchase_id}")

    purchase = Purchase.objects.get(id=purchase_id)
    print(purchase)
    print(purchase_id)
    # purchase.name = request.POST["purchase_name"]
    # purchase.email = request.POST["email"]
    # purchase.shipping_address = request.POST["shipping_address"]
    # purchase.quantity = request.POST["quantity"]
    # purchase.save(update_fields=['purchase_name',
    #                              'email', 'shipping_address', 'quantity'], force_update=True)
    purchase.save()
    return redirect(f"/orders")


def orders(request):
    all_purchases = Purchase.objects.all()
    context = {
        "all_purchases_html": all_purchases
    }
    return render(request, 'orders.html', context)


def edit_order(request, purchase_id):
    purchase = Purchase.objects.get(id=purchase_id)
    context = {
        "purchase_html": purchase
    }
    return render(request, "edit_order.html", context)


def process_order(request, purchase_id):
    print(request.POST)
    errors = Purchase.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect(f"/orders/edit/{purchase_id}")
    else:
        purchase = Purchase.objects.get(id=purchase_id)
        purchase.name = request.POST["purchase_name"]
        purchase.email = request.POST["email"]
        purchase.shipping_address = request.POST["shipping_address"]
        purchase.quantity = request.POST["quantity"]
        purchase.save(update_fields=['name',
                                     'email', 'shipping_address', 'quantity'], force_update=True)
        return redirect(f"/orders")


def delete_order(request, purchase_id):
    purchase = Purchase.objects.get(id=purchase_id)
    purchase.delete()

    return redirect("/orders")
# Create your views here.
