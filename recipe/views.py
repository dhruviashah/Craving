from django.shortcuts import render, redirect
from .serializers import RecipeSerializer
from .models import Recipe
from recipe_ingredient.models import RecipeIngredient
from ingredient.models import Ingredient

from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.views import APIView

from rest_framework.decorators import api_view
from rest_framework.parsers import FileUploadParser

# Create your views here.

class RecipeView(APIView):
    parser_class = (FileUploadParser,)
    
    def post(self, request):
        # obj=FileUploadParser()
        # print("="*100,request.POST, request.FILES['img'])
        # print("+"*100,self.parser_class(request.FILES['img']))
        # if 'img' in request.FILES:
        #   print("+"*100)
        image = None
        cooking_serving = None
        cooking_time = None
        reicpe_name= None

        if 'img' in request.FILES:
            image = request.FILES['img']
        if 'cooking_serving' in request.POST:
            cooking_serving = request.POST.get('cooking_serving')
        if 'cooking_time' in request.POST:
            cooking_time = request.POST.get('cooking_time') 
        if 'recipe_name' in request.POST:
            recipe_name = request.POST.get('recipe_name')

        data = {'img':image,
                'cooking_serving':cooking_serving,
                'cooking_time':cooking_time,
                'recipe_name':recipe_name}

        if not data:
            return JsonResponse({'message':'Data not provided'}, status=status.HTTP_204_NO_CONTENT)

        recipe_serializer = RecipeSerializer(data = data)
        print('/'*100)
        if recipe_serializer.is_valid():
            recipe_serializer.save()
            return JsonResponse(recipe_serializer.data, status = status.HTTP_200_OK)
        return JsonResponse(recipe_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            recipe = Recipe.objects.get(pk = pk)
        except:
            return JsonResponse({'message': 'recipe not exist'}, status=status.HTTP_404_NOT_FOUND)
    
        #data = JSONParser().parse(request)

        image = None
        cooking_serving = None
        cooking_time = None
        reicpe_name = None
        recipe_price = None

        if 'img' in request.FILES:
            image = request.FILES['img']
        if 'cooking_serving' in request.POST:
            cooking_serving = request.POST.get('cooking_serving')
        if 'cooking_time' in request.POST:
            cooking_time = request.POST.get('cooking_time') 
        if 'recipe_name' in request.POST:
            recipe_name = request.POST.get('recipe_name')
        if 'recipe_price' in request.POST:
            recipe_price = request.POST.get('recipe_price')

        data = {'img':image,
                'cooking_serving':cooking_serving,
                'cooking_time':cooking_time,
                'recipe_name':recipe_name,
                'recipe_price':recipe_price}
    
        recipe_serializer = RecipeSerializer(recipe, data = data)
        if recipe_serializer.is_valid():
            recipe_serializer.save()
            return render(request,'recipe/View_products.html',{'recipe_list':recipe})
            # return JsonResponse(recipe_serializer.data, status = status.HTTP_200_OK)
        return JsonResponse(recipe_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        try:
            recipe = Recipe.objects.get(pk = pk)
        except:
            return JsonResponse({'message': 'recipe not exist'}, status=status.HTTP_404_NOT_FOUND)
        recipe_serializer = RecipeSerializer(recipe)
        return JsonResponse(recipe_serializer.data)

    def delete(self, request, pk):
        try:
            recipe = Recipe.objects.get(pk = pk)
        except:
            return JsonResponse({'message': 'recipe not exist'}, status=status.HTTP_404_NOT_FOUND)
        recipe.delete()
        return JsonResponse({'message': 'ingredient was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

#@api_view(['GET'])
def recipe_list(request):
    category = request.POST.get('category_id')
    recipe = Recipe.objects.all()
    #category = request.POST.get('category_id')
    print(category)
    recipe_serializer = RecipeSerializer(recipe,many=True)
    print(request.session.get('customer_email'))
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    print(cart)
    #return JsonResponse(recipe_serializer.data, safe = False)
    return render(request,'recipe/Recipe_list.html',{'recipe_list':recipe})

@api_view(['GET'])
def product_list(request):
    recipe = Recipe.objects.all()
    recipe_serializer = RecipeSerializer(recipe,many=True)
    #return JsonResponse(recipe_serializer.data, safe = False)
    return render(request,'recipe/View_products.html',{'recipe_list':recipe})


@api_view(['PUT'])
def price_cal(self, pk):
    price_list = [] 
    total_price = 0
    ingredient_set = RecipeIngredient.objects.filter(recipe_id=pk).values_list('ingredient_id', flat = True)
    g = RecipeIngredient.objects.values_list('quantity', flat = True).filter(recipe_id=pk)
    length = len(g)
    
    for i in ingredient_set:
        k = Ingredient.objects.values_list('price', flat = True).get(pk=i)
        price_list.append(k)

    for i in range(length):
        price = (g[i]*price_list[i])/1000
        total_price = total_price+price

    # for i in price_list:
    #   total_price = total_price+i

    Recipe.objects.filter(pk=pk).update(recipe_price=total_price)

    return JsonResponse({'message': 'price updated successfully!'})

def add_product(request):
    return render(request,'recipe/Add_product_1.html')

def edit_product(request,pk):
    recipe = Recipe.objects.get(pk = pk)
    return render(request,'recipe/Edit_product_1.html',{'recipe':recipe})

def cart(request):
    product = request.POST.get('recipe_id')
    remove = request.POST.get('remove')
    recipe = Recipe.objects.get(pk=product)
    print(remove)
    cart = request.session.get('cart')
    if cart:
        quantity = cart.get(product)
        if quantity:
            if remove:
                if quantity<=1:
                    cart.pop(product)
                else:
                    cart[product] = quantity-1
            else:
                cart[product] = quantity+1
        else:
            cart[product] = 1
    else:
        cart={}
        cart[product] = 1
        
    request.session['cart']=cart
    print(cart)
    print(recipe)
    # recipe = Recipe.objects.get(pk = pk)
    # print(recipe)
    # quantity = 1
    # data={'id':recipe.id,
    #     'recipe_name':recipe.recipe_name,
    #     'recipe_price':recipe.recipe_price,
    #     'quantity':1}
    return redirect('recipe_list')

def cart_display(request):
    key = list(request.session.get('cart').keys())
    recipes = Recipe.objects.filter(id__in=key)
    print(recipes)
    return render(request,'recipe/Cart.html',{'products':recipes})

def breakfast_recipe_list(request):
    recipe = Recipe.objects.filter(category=1)
    recipe_serializer = RecipeSerializer(recipe,many=True)
    print(request.session.get('customer_email'))
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    print(cart)
    #return JsonResponse(recipe_serializer.data, safe = False)
    return render(request,'recipe/Recipe_list.html',{'recipe_list':recipe})


def update(self, request, pk):
        try:
            recipe = Recipe.objects.get(pk = pk)
        except:
            return JsonResponse({'message': 'recipe not exist'}, status=status.HTTP_404_NOT_FOUND)
    
        #data = JSONParser().parse(request)

        # image = None
        cooking_serving = None
        cooking_time = None
        reicpe_name = None
        recipe_price = None

        # if 'img' in request.FILES:
        #   image = request.FILES['img']
        if 'cooking_serving' in request.POST:
            cooking_serving = request.POST.get('cooking_serving')
        if 'cooking_time' in request.POST:
            cooking_time = request.POST.get('cooking_time') 
        if 'recipe_name' in request.POST:
            recipe_name = request.POST.get('recipe_name')
        # if 'recipe_price' in request.POST:
        #   recipe_price = request.POST.get('recipe_price')

        data = {'cooking_serving':cooking_serving,
                'cooking_time':cooking_time,
                'recipe_name':recipe_name}
    
        recipe_serializer = RecipeSerializer(recipe, data = data)
        if recipe_serializer.is_valid():
            recipe_serializer.save()
            return render(request,'recipe/Add_products.html')
            # return JsonResponse(recipe_serializer.data, status = status.HTTP_200_OK)
        return JsonResponse(recipe_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

