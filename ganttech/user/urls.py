from django.urls import path
from user.views import login_form, index, user_update,user_password,\
    user_orders,user_order_product,user_orderdetail,user_order_product_detail,\
    user_comments, user_deletecomment,logout_func, signup_form

urlpatterns = [
    path('', index, name='user_index'),
    path('update/', user_update, name='user_update'),
    path('password/', user_password, name='user_password'),
    path('orders/', user_orders, name='user_orders'),
    path('orders_product/', user_order_product, name='user_order_product'),
    path('orderdetail/<int:id>', user_orderdetail, name='user_orderdetail'),
    path('order_product_detail/<int:id>/<int:oid>', user_order_product_detail, name='user_order_product_detail'),
    path('comments/', user_comments, name='user_comments'),
    path('deletecomment/<int:id>', user_deletecomment, name='user_deletecomment'),


    path('login/', login_form, name='login_form'),
    path('logout/', logout_func, name='logout'),
    path('signup/', signup_form, name='register'),
]