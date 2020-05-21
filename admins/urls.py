from django.urls import path

from .views import dashboard_page, cows_detail_page, farms_detail_page, customers_detail_page, carriers_detail_page, \
    transaction_detail_page, order_detail_page, send_message_page, notification_page

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
]
