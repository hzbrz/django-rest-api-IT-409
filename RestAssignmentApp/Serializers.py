from datetime import date
from rest_framework import serializers
from .models import Customer, Address, Order, OrderItem


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

    def create(self, validated_data):
        return Customer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.customer_since = validated_data.get('customer_since', instance.customer_since)
        instance.prime_customer = validated_data.get('prime_customer', instance.prime_customer)

        instance.save()
        return instance


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

    def create(self, validated_data):
        return Address.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.customer = validated_data.get('customer', instance.customer)
        instance.street = validated_data.get('street', instance.street)
        instance.city = validated_data.get('city', instance.city)
        instance.state = validated_data.get('state', instance.state)
        instance.zip = validated_data.get('zip', instance.zip)

        instance.save()
        return instance


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['order_date', 'order_total', 'expiration_date']

    def create(self, validated_data):
        print(validated_data)
        c = date.today()
        order = Order(
            customer=validated_data['customer'],
            order_num=validated_data['order_num'],
            order_date=date.today(),
            order_total=0,
            payment_type=validated_data['payment_type'],
            account_number=validated_data['account_number'],
            expiration_date=date(c.year + 1, c.month, c.day)
        )
        order.save()
        return order

    def update(self, instance, validated_data):
        instance.customer = validated_data.get('customer', instance.customer)
        instance.order_num = validated_data.get('order_num', instance.order_num)
        instance.order_date = validated_data.get('order_date', instance.order_date)
        instance.order_total = validated_data.get('order_total', instance.order_total)
        instance.payment_type = validated_data.get('payment_type', instance.payment_type)
        instance.account_number = validated_data.get('account_number', instance.account_number)
        instance.expiration_date = validated_data.get('expiration_date', instance.expiration_date)

        instance.save()
        return instance


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

    def create(self, validated_data):
        return OrderItem.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.order = validated_data.get('order', instance.order)
        instance.item_description = validated_data.get('item_description', instance.item_description)
        instance.item_quantity = validated_data.get('item_quantity', instance.item_quantity)

        instance.save()
        return instance
