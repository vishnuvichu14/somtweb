from django.urls import path

from .views import dashboard_page, cows_detail_page, farms_detail_page, customers_detail_page, carriers_detail_page, \
    transaction_detail_page, order_detail_page, send_message_page, notification_page,edit_farm_page,edit_cow_page,edit_order_page,edit_customer_page,edit_carrier_page,edit_transaction_page

urlpatterns = [
    path("", dashboard_page, name="dashboard_page"),
    path("cows_details/", cows_detail_page, name="cows_details_page"),
    path("farms_details/", farms_detail_page, name="farms_details_page"),
    path("customers_details", customers_detail_page, name="customers_details_page"),
    path("carriers_details", carriers_detail_page, name="carriers_details_page"),
    path("transactions_details", transaction_detail_page, name="transactions_details_page"),
    path("order_details", order_detail_page, name="orders_details_page"),
    path("send_message", send_message_page, name="send_message_page"),
    path("notification", notification_page, name="notification_page"),

    path("edit_farm/<type>/<id>", edit_farm_page, name="edit_farm_page"),
    path("edit_cow/<type>/<id>", edit_cow_page, name="edit_cow_page"),
    path("edit_order/<type>/<id>", edit_order_page, name="edit_order_page"),
    path("edit_customer/<type>/<id>", edit_customer_page, name="edit_customer_page"),
    path("edit_carrier/<type>/<id>", edit_carrier_page, name="edit_carrier_page"),
    path("edit_transaction/<type>/<id>", edit_transaction_page, name="edit_transaction_page"),

]
