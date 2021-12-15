from django.shortcuts import render, redirect
from .models import Order
from .serializers import OrderSerializer

from recipe.models import Recipe
from user_profile.models import UserProfile
from user_profile.serializers import UserProfileSerializer
from order_delivery.models import OrderDelivery
from order_delivery_integration.models import OrderDeliveryJoin
from order_delivery_integration.serializers import OrderDeliveryJoinSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.views import APIView

from rest_framework.decorators import api_view
from rest_framework.parsers import FileUploadParser

from datetime import datetime,date
from django.db.models import Count

# Create your views here.
class OrderView(APIView):

    def post(self, request):
        product = None
        customer = None
        quantity = 1
        price = None
        status = False
        address = None
        phone = None


        if 'product' in request.POST:
            product = request.POST.get('product')
            print('+++++'+product)
        if 'customer' in request.POST:
            customer = request.POST.get('customer')
            print('//////'+customer)
        if 'quantity' in request.POST:
            quantity = request.POST.get('quantity')
        if 'price' in request.POST:
            price = request.POST.get('price')
        if 'status' in request.POST:
            status = request.POST.get('status')
        if 'address' in request.POST:
            address = request.POST.get('address')
        if 'phone' in request.POST:
            phone = request.POST.get('phone')


        data = {'product':product,
                'customer':customer,
                'quantity':quantity,
                'price':price,
                'status':status,
                'address':address,
                'phone':phone,
                'date':date.today()}

        print(data)
        if not data:
            return JsonResponse({'message':'Data not provided'}, status=status.HTTP_204_NO_CONTENT)

        order_serializer = OrderSerializer(data=data)

        if order_serializer.is_valid():
            order_serializer.save()
            return JsonResponse(order_serializer.data, status = status.HTTP_200_OK)
        return JsonResponse(order_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

def order_display(request):
    temp=0
    customer = request.session.get('customer_id')
    UserPro_id = list(UserProfile.objects.filter(user_id=customer).values_list('id', flat = True))
    
    Profile_id = UserPro_id[0] 
    print(Profile_id)

    user = list(UserProfile.objects.values_list('address', flat = True).filter(user_id=customer))
    user_no = list(UserProfile.objects.values_list('contact_number', flat = True).filter(user_id=customer))
    address = user[0]
    contact_number = user_no[0]

    cart = request.session.get('cart')
    key = list(request.session.get('cart').keys())
    recipes = list(Recipe.objects.filter(id__in=key))

    print(customer , address, contact_number, cart, recipes)

    for product in recipes:
        data = {'customer':Profile_id,
                'product':product.id,
                'price':product.recipe_price,
                'address':address,
                'phone':contact_number,
                'quantity':cart.get(str(product.id)),
                'date':date.today(),
                'total':0}

        print('+'*100)
        print(data)
        order_serializer = OrderSerializer(data=data)
        print('$'*100)
        if order_serializer.is_valid():
            print('-'*100)
            order_serializer.save()
            temp=1
    
    if temp==0:
        return HttpResponse("something went wrong")        
    request.session['cart']={}
    return redirect("cart_item_display")

    
    # user_serializer = OrderSerializer(user, many=True)
    # return JsonResponse(user_serializer.data, safe = False)

def customer_order_display(request):
    # user_id=request.session.get('customer_id')
    total=0
    profile_id = list(UserProfile.objects.values_list('id',flat=True).filter(user_id=request.session.get('customer_id')))
    print(profile_id[0])
    order = Order.objects.filter(customer=profile_id[0]).order_by('-date')  
    print(order)
    return render(request,'order/Customer_order_history.html',{'orders':order})

def staff_order_display(request):
    profile_id = list(UserProfile.objects.values_list('id',flat=True).filter(user_id=request.session.get('customer_id')))
    count = Order.objects.filter(customer_id=profile_id[0]).count()
    order = Order.objects.filter(customer=profile_id[0]).order_by('-date') 
    user_name = list(UserProfile.objects.values_list('first_name', flat = True).filter(id=profile_id[0]))
    data={'orders':order,
          'count':count}
    print(data)
    return render(request,'order/Order_history.html',{'orders':order,
                                                      'count':count,
                                                      'user_name':user_name[0]})

def staff_view_order(request):

    profile_id = request.POST.get('profile_id')
    # profile_id = list(UserProfile.objects.values_list('id',flat=True).filter(user_id=request.session.get('customer_id')))
    order = Order.objects.filter(customer=profile_id).filter(delivered=False).order_by('-date')  
    user = list(UserProfile.objects.values_list('address', flat = True).filter(id=profile_id))
    count = Order.objects.filter(customer_id=profile_id).count()
    user_name = list(UserProfile.objects.values_list('first_name', flat = True).filter(id=profile_id))
    print(profile_id,order,user)

    delivery_person = OrderDelivery.objects.filter(status='True')
    print(delivery_person)

    return render(request,'order/View_order.html',{'orders':order,
                                                'address':user[0],
                                                'count':count,
                                                'user_name':user_name[0],
                                                'user':profile_id,
                                                'delivery':delivery_person})

def staff_display(request):
    order = Order.objects.values('customer').filter(delivered=False).annotate(dcount=Count('customer'))
    print(order)
    # return HttpResponse("wait")
    return render(request,'order/Order_history.html',{'orders':order})

def delivery(request):
    deli = request.POST.get('delivery_person')
    user = request.POST.get('user')

    print(deli, user)

    data = {'delivery_person':request.POST.get('delivery_person'),
            'user':request.POST.get('user')}

    serializer = OrderDeliveryJoinSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return redirect('staff_dashboard')
    return HttpResponse("wait")

def deliver_order_display(request):
    person_id=list(OrderDelivery.objects.values_list('id',flat=True).filter(user_id=request.session.get('customer_id')))
    customer_id=list(OrderDeliveryJoin.objects.values_list('user',flat=True).filter(delivery_person=person_id[0]))
    orders = Order.objects.filter(customer__in=customer_id)
    final_order = orders.values('customer').filter(delivered=False).annotate(dcount=Count('customer'))
    print(final_order)
    print(orders)
    print(customer_id)
    print(person_id[0])
    return render(request,'order/Order_history_delivery_person.html',{'orders':final_order})

def deliver_order_detail(request):
    profile_id = request.POST.get('profile_id')
    # profile_id = list(UserProfile.objects.values_list('id',flat=True).filter(user_id=request.session.get('customer_id')))
    order = Order.objects.filter(customer=profile_id).order_by('-date').filter(delivered=False)  
    user = list(UserProfile.objects.values_list('address', flat = True).filter(id=profile_id))
    count = Order.objects.filter(customer_id=profile_id).count()
    user_name = list(UserProfile.objects.values_list('first_name', flat = True).filter(id=profile_id))
    print(profile_id,order,user)

    delivery_person = OrderDelivery.objects.filter(status='True')
    print(delivery_person)
    print(profile_id)
    return render(request,'order/Assigned_delivery.html',{'orders':order,
                                                'address':user[0],
                                                'count':count,
                                                'user_name':user_name[0],
                                                'user':profile_id,
                                                'delivery':delivery_person})

def status_change(request):
    cust_id = request.POST.get('customer_id')
    Order.objects.filter(customer=cust_id).update(delivered=True)
    print(cust_id)
    return redirect('delivery_dashboard')

def staff_order_history(request):
    order = Order.objects.values('customer').filter(delivered=True).annotate(dcount=Count('customer'))
    print(order)
    # return HttpResponse("wait")
    return render(request,'order/Order_history.html',{'orders':order})

def staff_order_history_detail(request):

    profile_id = request.POST.get('profile_id')
    # profile_id = list(UserProfile.objects.values_list('id',flat=True).filter(user_id=request.session.get('customer_id')))
    order = Order.objects.filter(customer=profile_id).filter(delivered=True).order_by('-date')  
    user = list(UserProfile.objects.values_list('address', flat = True).filter(id=profile_id))
    count = Order.objects.filter(customer_id=profile_id).count()
    user_name = list(UserProfile.objects.values_list('first_name', flat = True).filter(id=profile_id))
    print(profile_id,order,user)

    delivery_person = OrderDelivery.objects.filter(status='True')
    print(delivery_person)

    return render(request,'order/View_order.html',{'orders':order,
                                                'address':user[0],
                                                'count':count,
                                                'user_name':user_name[0],
                                                'user':profile_id,
                                                'delivery':delivery_person})

