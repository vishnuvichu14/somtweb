from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test

from web.models import Farm,Cow
from payment.models import Order,Delivery


@login_required
@user_passes_test(lambda user: user.groups.filter(name='Admin').exists())
def dashboard_page(request):
    return render(request, 'admins/dashboard_page.html')


@login_required
@user_passes_test(lambda user: user.groups.filter(name='Admin').exists())
def farms_detail_page(request):
    all_farms = Farm.objects.all()

    if request.POST:
        data = request.POST
        farm_name = data["farm_name"]
        # farm_address = data["farm_address"]
        # farm_pincode = data["farm_pincode"] 
        # farm_latitude = data["farm_latitude"] 
        # farm_longitude = data["farm_longitude"] 
        # farm_totalcows = data["farm_totalcows"] 
        Farm.objects.create(name=farm_name)
        # Farm.objects.create(name=farm_address)
        # Farm.objects.create(name=farm_pincode)
        # Farm.objects.create(name=farm_latitude)
        # Farm.objects.create(name=farm_longitude)
        # Farm.objects.create(name=farm_totalcows)
        # added other details too
    return render(request, 'admins/farms_details_page.html', {'all_farms': all_farms})


@login_required
@user_passes_test(lambda user: user.groups.filter(name='Admin').exists())
def cows_detail_page(request):
    all_cows = Cow.objects.all()

    if request.POST:
        data = request.POST
        cow_name = data["cow_name"]
        Cow.objects.create(name=cow_name)
        # added other details too
    return render(request, 'admins/cows_details_page.html',{'all_cows': all_cows})


@login_required
@user_passes_test(lambda user: user.groups.filter(name='Admin').exists())
def customers_detail_page(request):
    
    return render(request, 'admins/customers_details_page.html')


@login_required
@user_passes_test(lambda user: user.groups.filter(name='Admin').exists())
def carriers_detail_page(request):
    return render(request, 'admins/carriers_details_page.html')


@login_required
@user_passes_test(lambda user: user.groups.filter(name='Admin').exists())
def transaction_detail_page(request):
    return render(request, 'admins/transaction_details_page.html')


@login_required
@user_passes_test(lambda user: user.groups.filter(name='Admin').exists())
def order_detail_page(request):
    all_orders = Order.objects.all()

    if request.POST:
        data = request.POST
        order_farm = data["order_farm"]
        Order.objects.create(name=order_farm)
        # added other details too
    return render(request, 'admins/orders_details_page.html', {'all_orders': all_orders})


@login_required
@user_passes_test(lambda user: user.groups.filter(name='Admin').exists())
def notification_page(request):
    return render(request, 'admins/notification_page.html')


@login_required
@user_passes_test(lambda user: user.groups.filter(name='Admin').exists())
def send_message_page(request):
    return render(request, 'admins/send_message_page.html')


@login_required
@user_passes_test(lambda user: user.groups.filter(name='Admin').exists())
def edit_farm_page(request, type, id):
    farm = Farm.objects.get(id=id)
    if type == "delete":
        farm.delete()
        return redirect('farms_details_page')
    if request.POST:
        # retrieve post data
        data = request.POST
        # get farm_name data
        farm_name = data["farm_name"]
        farm_address = data["farm_address"]
        farm_pincode = data["farm_pincode"] 
        farm_latitude = data["farm_latitude"] 
        farm_longitude = data["farm_longitude"] 
        farm_totalcows = data["farm_totalcows"]

        # check if the data has change
        if (farm.name != farm_name or farm.address != farm_address or farm.pin_code != farm_pincode or farm.latitude != farm_latitude or farm.longitude != farm_longitude or farm.get_total_number_of_cows != farm_totalcows) :
            # if data has change then change the data
            farm.name = farm_name
            farm.address = farm_address
            farm.pin_code = farm_pincode
            farm.latitude = farm_latitude
            farm.longitude = farm_longitude
            farm.get_total_number_of_cows = farm_totalcows

        # add other fields too eg. pin_code , latitude , .. etc HINT : Check web/models.py

        # save changes
        farm.save()
        # redirect to the details page
        return redirect('farms_details_page')
    return render(request, 'admins/edit_farm_page.html', {'farm': farm})


@login_required
@user_passes_test(lambda user: user.groups.filter(name='Admin').exists())
def edit_cow_page(request, type, id):
    cow = Cow.objects.get(id=id)
    if type == "delete":
        cow.delete()
        return redirect('cows_details_page')
    if request.POST:
        # retrieve post data
        data = request.POST
        # get farm_name data
        cow_name = data["cow_name"]
        cow_tag = data["cow_tag"]
        # cow_dob = data["cow_dob"] 
        cow_breed = data["cow_breed"] 
        cow_farm = data["cow_farm"] 
        cow_quantity = data["cow_quantity"]
        cow_image = data["cow_image"]
        cow_qr = data["cow_qr"]

        # check if the data has change
        if (cow.name != cow_name or cow.tag != cow_tag  or  cow.breed != cow_breed or cow.farm != cow_farm or cow.default_quantity != cow_quantity or cow.photo != cow_image or cow.qr_code != cow_qr) :
            # if data has change then change the data
            cow.name = cow_name
            cow.tag = cow_tag
            # cow.get_age = cow_dob
            cow.breed = cow_breed
            cow.farm = cow_farm
            cow.default_quantity = cow_quantity
            cow.photo = cow_image
            cow.qr_code = cow_qr

        # add other fields too eg. pin_code , latitude , .. etc HINT : Check web/models.py

        # save changes
        cow.save()
        # redirect to the details page
        return redirect('cows_details_page')
    return render(request, 'admins/edit_cow_page.html', {'cow': cow})

@login_required
@user_passes_test(lambda user: user.groups.filter(name='Admin').exists())
def edit_order_page(request,type,id):
    order = Order.objects.get(id=id)
    if type == "delete":
        order.delete()
        return redirect('orders_details_page')
    if request.POST:
        # retrieve post data
        data = request.POST
        # get farm_name data
        order_farm = data["order_farm"]
        order_cow = data["farm_address"]
        order_customer = data["order_customer"]
        order_order_number = data["order_order_number"] 
        order_quantity = data["order_quantity"] 
        order_amount = data["order_amount"] 
        order_is_paid = data["order_is_paid"]
        order_start_date = data["order_start_date"]
        order_end_date = data["order_end_date"]

        # check if the data has change
        if (order.farm != order_farm or order.cow != order_cow or order.customer != order_customer or order.order_number != order_order_number or order.quantity != order_quantity or order.amount != order_amount or order.is_paid != order_is_paid or order.start_date != order_start_date or order.end_date != order_end_date) :
            # if data has change then change the data
            order.farm = order_farm
            order.cow = order_cow
            order.customer = order_customer
            order.order_number = order_order_number
            order.quantity = order_quantity
            order.amount = order_amount
            order.is_paid = order_is_paid 
            order.start_date = order_start_date
            order.end_date = order_end_date

        # add other fields too eg. pin_code , latitude , .. etc HINT : Check web/models.py

        # save changes
        order.save()
        # redirect to the details page
        return redirect('orders_details_page')
    return render(request, 'admins/edit_order_page.html', {'order': order})
