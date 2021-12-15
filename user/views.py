from django.shortcuts import render, redirect
from .models import User
from .serializers import UserSerializer
from user_profile.models import UserProfile

from django.contrib.auth import authenticate

from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  # <-- Here
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny

from django.contrib.auth.hashers import  check_password




class users(APIView):
    ###permission_classes = [IsAuthenticated]

    def post(self, request):
        print("5"*100)
        # user_data = JSONParser().parse(request)
        # if not user_data:
        #     return JsonResponse({'message':'Data not provided'}, status=status.HTTP_204_NO_CONTENT)

        if request.POST.get('password')!=request.POST.get('confirmpassword'):
            return HttpResponse("Enter same passwordin both field")

            
        email = None
        password = None
        username = None

        if 'email' in request.POST:
            email = request.POST.get('email')
            username = request.POST.get('email')
        if 'password' in request.POST:
            password = request.POST.get('password') 

        data1 = {"email":email,
                "username":email,
                "password":password}

        serializer = UserSerializer(data=data1)
        data = {}
        print("/"*100)
        if serializer.is_valid():
            user = serializer.save()
            data['email'] = user.email
            data['id'] = user.id
            return render(request, 'user/registration_p2.html',{'user':data})
        #    token = Token.objects.get_or_create(user=user)
        #    data['token'] = token[0].key
            # return JsonResponse(data, status=status.HTTP_201_CREATED)
             
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except:
            return JsonResponse({'message':'The user does not exist'}, status=status.HTTP_404_NOT_FOUND)

        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(user, data= user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except user.DoesNotExist: 
            return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND)

        user_serializer = UserSerializer(user) 
        return JsonResponse(user_serializer.data)

    def delete(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except:
            return JsonResponse({'message':'The user does not exist'}, status=status.HTTP_404_NOT_FOUND)

        user.deleted = True
        user.save()
        return JsonResponse({'message': 'User was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def user_list(request):
    user_data = User.objects.all()
    user_serializer = UserSerializer(user_data, many=True)
    return JsonResponse(user_serializer.data, safe=False)

def user_form(request):
    return render(request, 'user/login.html')

def registration_form(request):
    return render(request,'user/register.html')

def admin_form(request):
    return render(request, 'user/Admin_index.html')

def delivery_dashboard(request):
    return render(request,'user/Delivery_person_dashboard.html')

def staff_dashboard(request):
    return render(request,'user/Staff_index.html')

def logout(request):
    request.session.clear()
    return redirect('user_form')

def customer_login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    customer = User.objects.filter(username=email)
    print(customer)
    print('/'*100)
    if customer:
        flag = check_password(password, customer.password)
        if flag:
            return render(request,'user/home.html')
        else:
            return HttpResponse("wrong email or password")
    else:
        return HttpResponse("something went wrong")
    # email = request.POST.get('username')
    # password = request.POST.get('password') 

    # user = User.objects.filter(username=email)
    # print(user)
    # if user:
    #     flag = check_password(password,user.password)
    #     if flag:
    #         return render(request,'user/home.html')
    #     else:
    #         return HttpResponse("wrong email or password")
    # else:
    #     return HttpResponse("something went wrong")

from rest_framework import parsers, renderers
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework.schemas import ManualSchema
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken  # <-- Here


class LoginAPI(ObtainAuthToken):
    
    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        print("$"*100)
        serializer = self.get_serializer(data=request.data)
        print("*"*100)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']



        customer = list(User.objects.values_list('id', flat = True).filter(email=request.POST.get('username')))
        request.session['customer_id']=customer[0]
        request.session['customer_email']=request.POST.get('username')
        
        first_name = list(UserProfile.objects.values_list('first_name',flat=True).filter(user_id=request.session.get('customer_id')))
        print(first_name[0])

        request.session['name'] = first_name[0]

        print(request.session.get('customer_id'))
        print(request.session.get('customer_email'))
        
        user_is_staff = list(User.objects.values_list('is_staff', flat = True).filter(email=request.POST.get('username')))
        user_is_admin = list(User.objects.values_list('is_admin', flat = True).filter(email=request.POST.get('username')))
        user_is_delivery_person = list(User.objects.values_list('is_delivery_person', flat = True).filter(email=request.POST.get('username')))
        print(user_is_staff[0],user_is_admin[0],user_is_delivery_person[0])
        if user_is_staff[0]:
            if user_is_admin[0]:
                return render(request,'user/Admin_index.html')
            elif user_is_delivery_person[0]:
                return render(request,'user/Delivery_person_dashboard.html')
            else:
                return render(request,'user/Staff_index.html')
        else:
            return render(request,'user/Home.html')
        # return Response({'abc':'dhruvi gandi che'})
        # token, created = Token.objects.get_or_create(user=user)
        # return Response({'token': token.key})


obtain_auth_token = LoginAPI.as_view()
