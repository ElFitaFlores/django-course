from django.urls import path
from platzigram.views import hello_world, hi, order_numbers, say_hi

urlpatterns = [
    path('hello-world/', hello_world),
    path('hi/', hi),
    path('numbers/', order_numbers),
    path('hi/<str:name>/<int:age>/', say_hi),
]
