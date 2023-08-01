from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated

def index(request):
    return render(request, 'index.html', {})


class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
    
    
    
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
    
    
    
@permission_classes([IsAuthenticated])
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
    
    
    
    
@api_view()
@permission_classes([IsAuthenticated])
#@authentication_classes([TokenAuthentication])
def msg(request):
    return HttpResponse({"message":"This view is protected"})