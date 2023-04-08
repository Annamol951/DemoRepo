from rest_framework import serializers  
from ecomapp.models import Customer, Order  
  
class CustomerSerializer(serializers.ModelSerializer):  
    first_name = serializers.CharField(max_length=200, required=True)  
    last_name = serializers.CharField(max_length=200, required=True)  
    user = serializers.CharField(max_length =50, required=True)
    date_created = serializers.DateField('',required=True)
    
    class Meta:  
        model = Customer 
        fields = ('__all__') 


    def create(self, validated_data):  
        """ 
        Create and return a new `Customer` instance, given the validated data. 
        """  
        return Customer.objects.create(**validated_data)  
  
    def update(self, instance, validated_data):  
        """ 
        Update and return an existing `Customer` instance, given the validated data. 
        """  
        instance.first_name = validated_data.get('first_name', instance.first_name)  
        instance.last_name = validated_data.get('last_name', instance.last_name)  
        instance.user = validated_data.get('user', instance.user)       
        instance.date = validated_data.get('date', instance.date)  
           
        instance.save()  
        return instance  


 
class OrderSerializer(serializers.ModelSerializer):  
   product = serializers.CharField(max_length=200, required=True)  
   customer = serializers.CharField(max_length=200, required=True)  
   date_ordered = serializers.DateField(required=True)  
   status = serializers.CharField(max_length=10, required=True)  
  
class Meta:  
        model = Order
        fields = ('__all__')  


def create(self, validated_data):  
        """ 
        Create and return a new `Students` instance, given the validated data. 
        """  
        return Order.objects.create(**validated_data)  
  
def update(self, instance, validated_data):  
        """ 
        Update and return an existing `Students` instance, given the validated data. 
        """  
        instance.product = validated_data.get('product', instance.product)  
        instance.customer = validated_data.get('customer', instance.customer)  
        instance.date_ordered = validated_data.get('data_ordered', instance.data_ordered)  
        instance.status = validated_data.get('status', instance.status)  
  
        instance.save()  
        return instance          
