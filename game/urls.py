from django.urls import path
from .views import (
    home ,
    even_odd_game ,
    multiplication_game,
    summation_game,
    math_level,

    )
    

urlpatterns = [

    path('',home),
    path('even_odd_game/', even_odd_game, name='even_odd_game'),
    path('multiplication_game/', multiplication_game, name='multiplication_game'),
    path('summation_game/', summation_game, name='summation_game'),
    path('math_level/', math_level, name='math_level'),

]
