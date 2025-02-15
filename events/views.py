from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404

from .models import User, Event, Ticket
from .serializers import UserSerializer, EventSerializer, TicketSerializer

# User resgistration API
class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

# JWT Token generate (Login)
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Logged out successfully"}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

# Event Mgmt
class EventCreateView(generics.CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        if request.user.role != "admin":
            return Response({"error": "Only admins can create events"}, status=status.HTTP_403_FORBIDDEN)
        return super().create(request, *args, **kwargs)

class EventListView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]  

# Ticket  
class TicketPurchaseView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, event_id):
        user = request.user
        if user.role != "user":
            return Response({"error": "Only users can purchase tickets"}, status=status.HTTP_403_FORBIDDEN)

        event = get_object_or_404(Event, id=event_id)
        quantity = request.data.get("quantity", 0)

        # Check ticket availability
        if event.tickets_sold + quantity > event.total_tickets:
            return Response({"error": "Not enough tickets available"}, status=status.HTTP_400_BAD_REQUEST)

        # Create ticket and update event ticket count
        Ticket.objects.create(user=user, event=event, quantity=quantity)
        event.tickets_sold += quantity
        event.save()

        return Response({"message": "Tickets purchased successfully"}, status=status.HTTP_201_CREATED)
