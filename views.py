from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer


def index(request):
    """View to serve static HTML content for Little Lemon restaurant."""
    return render(request, 'index.html', {})


class MenuItemsView(generics.ListCreateAPIView):
    """API view to list all menu items (GET) and create a new menu item (POST)."""
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    """API view to retrieve (GET), update (PUT), and delete (DELETE) a single menu item."""
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]


class BookingViewSet(viewsets.ModelViewSet):
    """ViewSet to handle table bookings (GET, POST, PUT, DELETE) - requires authentication."""
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
