from unicodedata import name
from django.urls import path
from .views import (
    exercise2_validation_view,
    generator_view,
    truth_table_view,
    score_view,
    exercise1_validation_view,
    exercise2_validation_view
)

app_name = 'truthTable'
urlpatterns = [
    path('', generator_view, name='generator'),
    path('result/', truth_table_view, name='truth_table'),
    path('exercise1/', exercise1_validation_view, name='exercise1'),
    path('exercise2/', exercise2_validation_view, name='exercise2'),
    path('exercise1_validation/', exercise1_validation_view, name='exercise1_validation'),
    path('exercise2_validation/', exercise2_validation_view, name='exercise1_validation'),
    path('score/', score_view, name='result')
]
