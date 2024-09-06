from django.urls import path
from .views import LogarithmView, SquareRootView, PowerView, FactorialView

urlpatterns = [
    path('log', LogarithmView.as_view(), name='logarithm'),
    path('sqrt', SquareRootView.as_view(), name='sqrt'),
    path('pow', PowerView.as_view(), name='power'),
    path('fact', FactorialView.as_view(), name='factorial'),
]