from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test

from web.models import Farm


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
        Farm.objects.create(name=farm_name)
        # added other details too
    return render(request, 'admins/farms_details_page.html', {'all_farms': all_farms})


@login_required
@user_passes_test(lambda user: user.groups.filter(name='Admin').exists())
def cows_detail_page(request):
    return render(request, 'admins/cows_details_page.html')


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
    return render(request, 'admins/orders_details_page.html')


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

        # check if the data has change
        if farm.name != farm_name:
            # if data has change then change the data
            farm.name = farm_name

        # add other fields too eg. pin_code , latitude , .. etc HINT : Check web/models.py

        # save changes
        farm.save()
        # redirect to the details page
        return redirect('farms_details_page')
    return render(request, 'admins/edit_farm_page.html', {'farm': farm})
