from django.shortcuts import render,redirect
from  django.http import HttpResponse
from  . import models
import telebot


def index(request):
     all_products = models.Products.objects.all()
     categories = models.Category.objects.all()
     return  render(request,'index.html',{'products':all_products,'categories':categories})

def about(request):
     return HttpResponse('Про нас')


def about_product(request,pk):
     product = models.Products.objects.get(product_name=pk)
     return render(request,'about_product.html',{'product':product})

def user_cart(request):

     user_products = models.UserCart.objects.filter(user_id = request.user.id)
     total_amount = sum([total.quantity*total.product.product_price for total in user_products])
     return render(request,'user_cart.html',{'product': user_products,'total':total_amount})


def add_pr_to_cart(request, pk):
     if request.method == 'POST':
          quantity = int(request.POST.get('quantity'))
          user_id = request.user.id
          product_id = models.Products.objects.get(id=pk)

          if product_id.product_count >= quantity:
               #Уменьшение
               product_id.product_count -=quantity
               product_id.save()

               chekcker = models.UserCart.objects.filter(user_id=user_id,product=product_id)
               if not chekcker:
                    models.UserCart.objects.create(user_id=user_id,product = product_id,quantity = quantity)

               else:
                    pr_to_add = models.UserCart.objects.get(user_id=user_id,product=product_id)
                    pr_to_add.quantity += quantity
                    pr_to_add.save()
               return redirect('/')
          else:
               return redirect(f'/product/{product_id.product_name}')

def delete_from_cart(request,pk):
     if request.method == 'POST':
          product_to_delete = models.Products.objects.get(id=pk)
          user_cart= models.UserCart.objects.get(product=product_to_delete,user_id = request.user.id)
          product_to_delete.product_count += user_cart.quantity
          user_cart.delete()
          product_to_delete.save()
          return redirect('/usercart')

def confirm_order(request,pk):
     if request.method=='POST':
          user_cart = models.UserCart.objects.filter(user_id = request.user.id)
          full_message = 'Новый заказ:\n\n'
          for item in user_cart:
               full_message+=f'Продукт: {item.product.product_name}: {item.quantity}шт'

          total = [i.product.product_price*i.quantity for i in user_cart]

          full_message += f'\n\nВсего на заказ:{sum(total)}'

          bot = telebot.TeleBot('5518127518:AAGOngZBvQNwMzO2XzxowhYygTt740uZwBo')
          bot.send_message(347476275,full_message)



          user_cart.delete()
          return redirect('/')