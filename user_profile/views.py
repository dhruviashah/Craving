from django.shortcuts import render
from .serializers import UserProfileSerializer
from .models import UserProfile

from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.views import APIView

from rest_framework.decorators import api_view
# Create your views here.

class UserProfileView(APIView):

    def post(self, request):
        # user_data = JSONParser().parse(request)
        # if not user_data:
        #   return JsonResponse({'message':'Data not provided'}, status=status.HTTP_204_NO_CONTENT)
        
        first_name = None
        last_name = None
        address = None
        contact_number = None
        user_id = None
        user_email=None

        if 'first_name' in request.POST:
            first_name = request.POST.get('first_name')
        if 'last_name' in request.POST:
            last_name = request.POST.get('last_name')
        if 'address' in request.POST:
            address = request.POST.get('address')
        if 'contact_number' in request.POST:
            contact_number = request.POST.get('contact_number') 
        if 'user_id' in request.POST:
            user_id = request.POST.get('user_id') 
        if 'user_email' in request.POST:
            user_email = request.POST.get('user_email') 

        data = {"first_name":first_name,
                "last_name":last_name,
                "address":address,
                "contact_number":contact_number,
                "user_id":user_id}

        user_serializer = UserProfileSerializer(data = data)
        if user_serializer.is_valid():
            user_serializer.save()
            request.session['customer_id'] = user_id
            request.session['customer_email'] = user_email
            request.session['name'] = first_name
            # request.session['address'] = address
            # request.session['contact_number'] = contact_number
            return render(request,'user_profile/Home.html')
            # return JsonResponse(user_serializer.data, status = status.HTTP_200_OK)
        return JsonResponse(user_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            user = UserProfile.objects.get(pk=pk)
        except user.DoesNotExist:
            return JsonResponse({'message': 'The role does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
        first_name = None
        last_name = None
        address = None
        contact_number = None

        if 'first_name' in request.POST:
            first_name = request.POST.get('first_name')
        if 'last_name' in request.POST:
            last_name = request.POST.get('last_name')
        if 'address' in request.POST:
            address = request.POST.get('address')
        if 'contact_number' in request.POST:
            contact_number = request.POST.get('contact_number') 

        data = {"first_name":first_name,
                "last_name":last_name,
                "address":address,
                "contact_number":contact_number,
                }

            
        user_data = JSONParser().parse(request)
        user_serializer = UserProfileSerializer(user, data = data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data,status = status.HTTP_200_OK)
        return JsonResponse(user_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        try:
            user = UserProfile.objects.get(pk=pk)
        except user.DoesNotExist:
            return JsonResponse({'message': 'The role does not exist'}, status=status.HTTP_404_NOT_FOUND)
        user_serializer = UserProfileSerializer(user)
        return JsonResponse(user_serializer.data)

    def delete(self, request, pk):
        try:
            user = UserProfile.objects.get(pk=pk)
        except user.DoesNotExist:
            return JsonResponse({'message': 'The role does not exist'}, status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return JsonResponse({'message': 'User was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def user_list(request):
    user_data = UserProfile.objects.all()
    user_serializer = UserProfileSerializer(user_data, many = True)
    return JsonResponse(user_serializer.data, safe = False)

def home_form(request):
    return render(request,'user_profile/Home.html')

def edit_profile(request):
    user_data = UserProfile.objects.filter(user_id=request.session.get('customer_id'))
    print(user_data)
    user_eamil = request.session.get('customer_email')
    return render(request,'user_profile/Edit_profile_customer.html',{"user_data":user_data})


