from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .models import Customer, Address, Order, OrderItem
from .Serializers import CustomerSerializer, AddressSerializer, OrderSerializer, OrderItemSerializer


# home page shows all the endpoints
def endpoints(request):
    return render(request, 'home.html')


# get/post – Customer
class CustomerListCreate(generics.ListCreateAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            customer = serializer.create(serializer.validated_data)
            return Response(CustomerSerializer(customer).data, 'header.html')

# get/post Address
class GetAddresses(generics.RetrieveAPIView):
    queryset = Address.objects.all()

    def retrieve(self, request, *args, **kwargs):
        fk = kwargs["fk"]
        addresses = Address.objects.filter(customer=fk)
        addressData = AddressSerializer(addresses, many=True)
        return Response(addressData.data)

class AddAddress(generics.CreateAPIView):
    serializer_class = AddressSerializer

    def create(self, request, *args, **kwargs):
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            address = serializer.create(serializer.validated_data)
            return Response(AddressSerializer(address).data)


# get/post Order
class GetOrders(generics.RetrieveAPIView):
    queryset = Order.objects.all()

    def retrieve(self, request, *args, **kwargs):
        fk = kwargs["fk"]
        orders = Order.objects.filter(customer=fk)
        orderData = OrderSerializer(orders, many=True)
        return Response(orderData.data)

class AddOrder(generics.CreateAPIView):
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            order = serializer.create(serializer.validated_data)
            return Response(OrderSerializer(order).data)


# post (create)/ get Product
class GetProducts(generics.RetrieveAPIView):
    queryset = Order.objects.all()

    def retrieve(self, request, *args, **kwargs):
        fk = kwargs["fk"]
        orders = OrderItem.objects.filter(order=fk)
        orderData = OrderItemSerializer(orders, many=True)
        return Response(orderData.data)

class AddProduct(generics.CreateAPIView):
    serializer_class = OrderItemSerializer

    def create(self, request, *args, **kwargs):
        serializer = OrderItemSerializer(data=request.data)
        if serializer.is_valid():
            product = serializer.save()
            total = product.order.order_total + (serializer.validated_data['item_quantity'] * 50)
            product.order.order_total = total
            product.order.save()
            return Response(OrderItemSerializer(product).data)


