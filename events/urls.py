from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterUserView, LogoutView, EventCreateView, EventListView, TicketPurchaseView

urlpatterns = [
    path('api/register/', RegisterUserView.as_view(), name='register'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
    path('api/events/', EventListView.as_view(), name='event-list'),
    path('api/events/create/', EventCreateView.as_view(), name='event-create'),
    path('api/events/<int:event_id>/purchase/', TicketPurchaseView.as_view(), name='ticket-purchase'),
]
