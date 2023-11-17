# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from .models import *
# from django.contrib.auth import logout
# from ecommerece.settings import EMAIL_HOST_USER
# from django.contrib import messages
# from django.core.mail import send_mail
# import datetime
# import re
# from datetime import timedelta
# # Create your views here.
# def index(request):
#     return render(request,'index.html')
#
# def seller_reg(request):
#     if request.method == 'POST':
#         sname = request.POST.get('sname')
#         email = request.POST.get('email')
#         img_name = request.FILES.get('img_name')
#         phone = request.POST.get('phone')
#         cname = request.POST.get('cname')
#         com_details = request.POST.get('com_details')
#         password = request.POST.get('password')
#         cpassword = request.POST.get('cpassword')
#         if password == cpassword:
#             a = reg_seller(sname=sname,email=email,img_name=img_name,phone=phone,cname=cname,com_details=com_details,password=password)
#             a.save()
#             return HttpResponse("Registration Success")
#
#     return render(request,'seller_reg.html')
# def seller_login(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         l = reg_seller.objects.all()
#         for i in l:
#             if (i.email == email and i.password == password):
#                 request.session['seller_id'] = i.id#global
#                 return redirect(seller_profile)
#         else:
#             return HttpResponse("Login Failed")
#     return render(request,'seller_login.html')
#
# def addproduct(request):
#     if request.method == 'POST':
#         man_name = request.POST.get('man_name')
#         med_name = request.POST.get('med_name')
#         dosage = request.POST.get('dosage')
#         qty = request.POST.get('qty')
#         type = request.POST.get('type')
#         price = request.POST.get('price')
#         mtf = request.POST.get('mtf')
#         med_pic = request.FILES.get('med_pic')
#         a = product_add(man_name=man_name,med_name=med_name,dosage=dosage,qty=qty,type=type,price=price,mtf=mtf,med_pic=med_pic)
#         a.save()
#         # return HttpResponse('Product Added Successfully')
#         return redirect(product_view)
#
#     return render(request,'Add_product.html')
#
# def seller_profile(request):
#     id1=request.session['seller_id']
#     a= reg_seller.objects.get(id=id1)
#     image = str(a.img_name).split('/')[-1]
#     return render(request,'seller_profile.html',{'data':a,'img':image})
#
# def edit_seller_profile(request,id):
#     a = reg_seller.objects.get(id=id)
#     img = str(a.img_name).split('/')[-1]
#     if request.method == 'POST':
#         a.sname = request.POST.get('sname')
#         a.email = request.POST.get('email')
#         if request.FILES.get('img_name') == None:
#             a.save()
#         else:
#             a.img_name = request.FILES['img_name']
#             a.save()
#         a.phone = request.POST.get('phone')
#         a.cname = request.POST.get('cname')
#         a.com_details = request.POST.get('com_details')
#         a.save()
#         return redirect(seller_profile)
#     return render(request,'edit_seller_profile.html',{'data':a,'img':img})
#
# def product_view(request):
#     # id1 = request.session['id']
#     a = product_add.objects.all()
#     # img = str(a.med_pic).split('/')[-1]
#     id = []
#     man_name = []
#     med_name = []
#     dosage = []
#     type = []
#     price = []
#     qty = []
#     mtf = []
#     med_pic = []
#     for i in a:
#         id1 = i.id
#         id.append(id1)
#
#         man_name1 = i.man_name
#         man_name.append(man_name1)
#         med_name1 = i.med_name
#         med_name.append(med_name1)
#         dosage1 = i.dosage
#         dosage.append(dosage1)
#         type1 = i.type
#         type.append(type1)
#         price1 = i.price
#         price.append(price1)
#         qty1 = i.price
#         qty.append(qty1)
#         mtf1 = i.mtf
#         mtf.append(mtf1)
#         med_pic1 = str(i.med_pic).split('/')[-1]
#         med_pic.append(med_pic1)
#     mylist=zip(id,man_name,med_name,dosage,type,price,mtf,med_pic,qty)
#     return render(request,'product_view.html',{'data':mylist})
#
# def edit_product(request,id):
#     a = product_add.objects.get(id=id)
#     img = str(a.med_pic).split('/')[-1]
#     if request.method == 'POST':
#         a.man_name = request.POST.get('man_name')
#         a.med_name = request.POST.get('med_name')
#         a.dosage = request.POST.get('dosage')
#         a.type = request.POST.get('type')
#         a.qty = request.POST.get('qty')
#         a.price = request.POST.get('price')
#         a.mtf = request.POST.get('mtf')
#         if request.FILES.get('med_pic') == None:
#             a.save()
#         else:
#             a.med_pic = request.FILES['med_pic']
#             a.save()
#         a.save()
#         return redirect(product_view)
#     return render(request,'edit_products.html',{'data':a,'img':img})
#
# def buyer_reg(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         buyer_img = request.FILES.get('buyer_img')
#         phone = request.POST.get('phone')
#         password = request.POST.get('password')
#         cpassword = request.POST.get('cpassword')
#
#         a = reg_buyer.objects.all()
#         buy_name = []
#         buy_email = []
#         if password == cpassword:
#             for i in a:
#                 buy_name.append(i.username)
#                 buy_email.append(i.email)
#                 if username in buy_name:
#                     return HttpResponse('Username is already taken!')
#                 elif email in buy_email:
#                     return HttpResponse('Email is already taken!')
#
#             b = reg_buyer(username=username,email=email,buyer_img=buyer_img,phone=phone,password=password)
#             b.save()
#             return redirect(buyer_login)
#     return render(request,'Buyer_reg.html')
#
# def buyer_login(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         a = reg_buyer.objects.all()
#         for i in a:
#             if (i.email == email and i.password == password):
#                 request.session['user_id'] = i.id
#                 request.session['username'] = i.username# global
#                 return redirect(buyer_index)
#         else:
#             # return HttpResponse('Login Failed!')
#             messages.error(request,'Login failed!')
#             return render(buyer_login)
#     return render(request,'buyer_login.html')
#
# def buyer_profile(request):
#     id1 = request.session['user_id']
#     a = reg_buyer.objects.get(id=id1)
#     image = str(a.buyer_img).split('/')[-1]
#     return render(request,'buyer_profile.html',{'data':a,'img':image})
#
# def edit_buyer_profile(request):
#     try:
#         id1 = request.session['user_id']
#         a = reg_buyer.objects.get(id=id1)
#         img = str(a.buyer_img).split('/')[-1]
#         if request.method == 'POST':
#             a.username = request.POST.get('username')
#             a.email = request.POST.get('email')
#             a.phone =  request.POST.get('phone')
#             if request.FILES.get('buyer_img') == None:
#                 a.save()
#             else:
#                 a.buyer_img = request.FILES['buyer_img']
#                 a.save()
#             a.save()
#             return redirect(buyer_index)
#     except:
#         request.session['user_id'] = None
#         return redirect(buyer_login)
#     return render(request,'edit_buyer_profile.html',{'data':a,'img':img})
#
# def buyer_logout(request):
#     logout(request)
#     return redirect(buyer_login)
#
# def buyer_index(request):
#     id1 = request.session['user_id']
#     a = reg_buyer.objects.get(id=id1)
#     img = str(a.buyer_img).split('/')[-1]
#     if request.method == 'POST':
#         a.username = request.POST.get('username')
#         a.email = request.POST.get('email')
#         a.phone = request.POST.get('phone')
#         if request.FILES.get('buyer_img') == None:
#             a.save()
#         else:
#             a.buyer_img = request.FILES['img_name']
#             a.save()
#         a.save()
#         return redirect(buyer_profile)
#     return render(request,'buyer_index.html',{'data':a,'img':img})
# def filt_product_view(request, category):
#     id1 = request.session['user_id']
#     b = reg_buyer.objects.get(id=id1)
#     img = str(b.buyer_img).split('/')[-1]
#     a = product_add.objects.filter(type=category)
#     # img = str(a.med_pic).split('/')[-1]
#     id = []
#     man_name = []
#     med_name = []
#     dosage = []
#     type = []
#     price = []
#     qty = []
#     mtf = []
#     med_pic = []
#     for i in a:
#         id1 = i.id
#         id.append(id1)
#
#         man_name1 = i.man_name
#         man_name.append(man_name1)
#         med_name1 = i.med_name
#         med_name.append(med_name1)
#         dosage1 = i.dosage
#         dosage.append(dosage1)
#         type1 = i.type
#         type.append(type1)
#         price1 = i.price
#         price.append(price1)
#         qty1 = i.price
#         qty.append(qty1)
#         mtf1 = i.mtf
#         mtf.append(mtf1)
#         med_pic1 = str(i.med_pic).split('/')[-1]
#         med_pic.append(med_pic1)
#     mylist=zip(id,man_name,med_name,dosage,type,price,mtf,med_pic,qty)
#     return render(request,'filt_prod_view.html',{'data':mylist,"img":img})
#
# def prod_wishlist(request,id):
#     a = product_add.objects.get(id=id)
#     id1 = request.session['user_id']
#     c = wishlist.objects.all()
#     for i in c:
#         if id == i.prod_id and id1 == i.user_id:
#             return HttpResponse('Item already exist')
#     else:
#         b = wishlist(prod_id=a.id,user_id = id1,med_name1 = a.med_name , man_name1 = a.man_name, dosage1 = a.dosage,type1=a.type,qty1=a.qty,price1=a.price,mtf1=a.mtf,med_pic1=a.med_pic)
#         b.save()
#         return HttpResponse("item added succesfully")
#
# def wishlist_view(request):
#     id2 = request.session['user_id']
#     b = reg_buyer.objects.get(id=id2)
#     img = str(b.buyer_img).split('/')[-1]
#     print(id2)
#     a = wishlist.objects.all()
#     # img = str(a.med_pic).split('/')[-1]
#     id = []
#     prod_id = []
#
#     man_name = []
#     med_name = []
#     dosage = []
#     type = []
#     price = []
#     qty = []
#     mtf = []
#     med_pic = []
#     abc=[]
#
#     for i in a:
#
#         abc.append(i.user_id)
#         prodid1 = i.prod_id
#         prod_id.append(prodid1)
#         id1 = i.id
#         id.append(id1)
#
#         man_name1 = i.man_name1
#         man_name.append(man_name1)
#         med_name1 = i.med_name1
#         med_name.append(med_name1)
#         dosage1 = i.dosage1
#         dosage.append(dosage1)
#         type1 = i.type1
#         type.append(type1)
#         price1 = i.price1
#         price.append(price1)
#         qty1 = i.qty1
#         qty.append(qty1)
#         mtf1 = i.mtf1
#         mtf.append(mtf1)
#         med_pic1 = str(i.med_pic1).split('/')[-1]
#         med_pic.append(med_pic1)
#     mylist=list(zip(abc,prod_id,id,man_name,med_name,dosage,type,price,mtf,med_pic,qty))
#     return render(request,'wishlist_view.html',{'data':mylist,'id':id2,'img':img})
#
# def delete_wish(request,id):
#     a = wishlist.objects.get(id=id)
#     id1 = request.session['user_id']
#     a.delete()
#     return redirect("http://127.0.0.1:8000/ecommapp/wishlist_view/")
#
#
# def prod_cart(request,id):
#     a = product_add.objects.get(id=id)
#     id1 = request.session['user_id']
#     c = cart.objects.all()
#     for i in c:
#         if id == i.prod_id and id1 == i.user_id:
#             i.qty1 +=1
#             i.price1 = a.price * i.qty1
#             i.save()
#             # return HttpResponse('Product Incremented')
#             messages.success(request, 'Product Incremented')
#     else:
#         count=1
#         b = cart(prod_id=a.id,user_id = id1,med_name1 = a.med_name , man_name1 = a.man_name, dosage1 = a.dosage,qty1=count,type1=a.type,price1=a.price,mtf1=a.mtf,med_pic1=a.med_pic)
#         b.save()
#         # return HttpResponse("Added to cart")
#         messages.success(request, 'Added to cart')
#
#         return redirect(wishlist_view)
# def cart_view(request):
#     id2 = request.session['user_id']
#     b = reg_buyer.objects.get(id=id2)
#     img = str(b.buyer_img).split('/')[-1]
#     print(id2)
#     a = cart.objects.all()
#     # img = str(a.med_pic).split('/')[-1]
#     id = []
#     prod_id = []
#
#     man_name = []
#     med_name = []
#     dosage = []
#     type = []
#     price = []
#     qty = []
#     mtf = []
#     med_pic = []
#     userid = []
#
#     for i in a:
#         userid.append(i.user_id)
#         prodid1 = i.prod_id
#         prod_id.append(prodid1)
#         id1 = i.id
#         id.append(id1)
#
#         man_name1 = i.man_name1
#         man_name.append(man_name1)
#         med_name1 = i.med_name1
#         med_name.append(med_name1)
#         dosage1 = i.dosage1
#         dosage.append(dosage1)
#         type1 = i.type1
#         type.append(type1)
#         price1 = i.price1
#         price.append(price1)
#         qty1 = i.qty1
#         qty.append(qty1)
#         mtf1 = i.mtf1
#         mtf.append(mtf1)
#         med_pic1 = str(i.med_pic1).split('/')[-1]
#         med_pic.append(med_pic1)
#
#     tp1 = []
#     tp2 = []
#     d = cart.objects.filter(user_id=id2)
#     for i in d:
#         # print(i.price)
#         tp1.append(i.price1)
#         # print(tp1)
#     for i in tp1:
#         tp2.append(int(i))
#     # print(tp2)
#     total_price=sum(tp2)
#     request.session['total_price'] = total_price
#     mylist = list(zip(userid, prod_id, id, man_name, med_name, dosage, type, price, mtf, med_pic, qty))
#     return render(request, 'cart.html', {'data': mylist, 'id': id2,'price':total_price,'img':img})
#
# def delete_cart(request,id):
#     a = cart.objects.get(id=id)
#     id1 = request.session['user_id']
#     a.delete()
#     return redirect(cart_view)
#
# def cartinc(request,id):
#     a = cart.objects.get(id=id)
#     b = product_add.objects.get(id=a.prod_id)#main product model
#     a.qty1 += 1
#     a.price1 = b.price * a.qty1
#     a.save()
#     return redirect(cart_view)
#
# def cartdec(request,id):
#     a = cart.objects.get(id=id)
#     b = product_add.objects.get(id=a.prod_id)
#     a.qty1 -= 1
#     a.price1 = b.price * a.qty1
#     a.save()
#     return redirect(cart_view)
#
# def buyer_address(request):
#     try:
#         id2 = request.session['user_id']
#         b = address_buyer.objects.get(user_id=id2)
#         if b.address:
#             return redirect(edit_buyer_address)
#     except:
#         if request.method == 'POST':
#             fullname = request.POST.get('fullname')
#             phone = request.POST.get('phone')
#             email = request.POST.get('email')
#             address = request.POST.get('address')
#             state = request.POST.get('state')
#             district = request.POST.get('district')
#             city = request.POST.get('city')
#             zip = request.POST.get('zip')
#             a = address_buyer(user_id=id2,full_name=fullname,phone=phone,email=email,address=address,state=state,district=district,city=city,zip=zip)
#             a.save()
#             return redirect(cart_view)
#     return render(request,'buyer_address.html')
#
# def edit_buyer_address(request):
#     id1 = request.session['user_id']
#     a = address_buyer.objects.get(user_id=id1)
#     if request.method == 'POST':
#         a.full_name = request.POST.get('fullname')
#         a.phone = request.POST.get('phone')
#         a.email = request.POST.get('email')
#         a.address = request.POST.get('address')
#         a.state = request.POST.get('state')
#         a.district = request.POST.get('district')
#         a.city = request.POST.get('city')
#         a.zip = request.POST.get('zip')
#         a.save()
#         return redirect(cart_view)
#     return render(request,'edit_buyer_address.html',{'data':a})
#
# def details_delivery(request):
#     id1 = request.session['user_id']
#     a = cart.objects.all()
#     b = address_buyer.objects.all()
#
#     price = request.session['total_price']
#     address1 = []
#     prod_str = ''
#     prod_img = ''
#     ord_date = datetime.date.today()
#     est_date = ord_date+timedelta(days=7)
#
#     for i in b:
#         if i.user_id == id1:
#             address1.append(i.address)
#             address1.append(i.state)
#             address1.append(i.district)
#             address1.append(i.city)
#             address1.append(i.zip)
#     print(address1)
#     prod_list=[]
#     for i in a:
#         if i.user_id == id1:
#             prod_str = "med_pic:"+str(i.med_pic1).split('/')[-1]+"|Med_name:"+str(i.med_name1)+"|Dosage:"+str(i.dosage1)+"|Quantiy:"+str(i.qty1)+"|price:"+str(i.price1)
#             prod_list.append(prod_str)
#
#     prod_strlist = "+".join(prod_list)
#     print(prod_strlist)
#     c = final_deliver(user_id=id1,address=address1,order_date=ord_date,est_del_date=est_date,products=prod_strlist,amount=price)
#     c.save()
#     for i in address1:
#         print(i)
#     return HttpResponse('Success')
#
# def deliver_display(request):
#     # print('hahah')
#     id2 = request.session['user_id']
#     med_pic = []
#     med_name = []
#     dosage = []
#     qty = []
#     price = []
#     address = []
#     ord_date = []
#     del_date = []
#     amount = []
#     user_id = []
#     a = final_deliver.objects.all()
#     u_name = request.session['username']
#
#
#     for i in a:
#
#         if i.user_id == id2:
#             items = i.products.split("+")
#             #print(items)
#             #print(i.products,type(i.products), i.user_id)
#             for item in items:
#                 # print(item)
#
#                 # Split the item into key-value pairs
#                 key_value_pairs = item.split('|')
#                 # print(key_value_pairs)
#                 # print(len(key_value_pairs))
#
#                 # Ensure that the product data is in the expected format
#                 if len(key_value_pairs) == 5:
#                     med_pic.append(key_value_pairs[0].split(':')[-1])
#                     med_name.append(key_value_pairs[1].split(':')[-1])
#                     dosage.append(key_value_pairs[2].split(':')[-1])
#                     qty.append(key_value_pairs[3].split(':')[-1])
#                     price.append(key_value_pairs[4].split(':')[-1])
#                 else:
#                     # Handle unexpected data format or log an error
#                     pass
#             user_id.append(i.user_id)
#             address.append(i.address)
#             ord_date.append(i.order_date)
#             del_date.append(i.est_del_date)
#             amount.append(i.amount)
#     print(med_pic)
#     mylist = zip(med_pic,med_name,dosage,qty,price,address,ord_date,del_date,amount,user_id)
#     # for i,j,k,l,m,n,o,p,q,r in mylist:
#     return render(request,'deliver_display.html',{'data':mylist,'u_name':u_name,'id':id2})
#
#
# def buyer_product_view(request):
#
#     id1 = request.session['user_id']
#     b = reg_buyer.objects.get(id=id1)
#     img = str(b.buyer_img).split('/')[-1]
#     a = product_add.objects.all()
#     # img = str(a.med_pic).split('/')[-1]
#     id = []
#     man_name = []
#     med_name = []
#     dosage = []
#     type = []
#     price = []
#     qty = []
#     mtf = []
#     med_pic = []
#     for i in a:
#         id1 = i.id
#         id.append(id1)
#
#         man_name1 = i.man_name
#         man_name.append(man_name1)
#         med_name1 = i.med_name
#         med_name.append(med_name1)
#         dosage1 = i.dosage
#         dosage.append(dosage1)
#         type1 = i.type
#         type.append(type1)
#         price1 = i.price
#         price.append(price1)
#         qty1 = i.price
#         qty.append(qty1)
#         mtf1 = i.mtf
#         mtf.append(mtf1)
#         med_pic1 = str(i.med_pic).split('/')[-1]
#         med_pic.append(med_pic1)
#     mylist=zip(id,man_name,med_name,dosage,type,price,mtf,med_pic,qty)
#     return render(request,'buyer_product_view.html',{'data':mylist,"img":img})

from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth import logout
from ecommerece.settings import EMAIL_HOST_USER
from django.contrib import messages
from django.core.mail import send_mail
import datetime
import ast
import re
from datetime import timedelta
# Create your views here.
def index(request):
    return render(request,'index.html')

def seller_reg(request):
    if request.method == 'POST':
        sname = request.POST.get('sname')
        email = request.POST.get('email')
        img_name = request.FILES.get('img_name')
        phone = request.POST.get('phone')
        cname = request.POST.get('cname')
        com_details = request.POST.get('com_details')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        if password == cpassword:
            a = reg_seller(sname=sname,email=email,img_name=img_name,phone=phone,cname=cname,com_details=com_details,password=password)
            a.save()
            return HttpResponse("Registration Success")

    return render(request,'seller_reg.html')
def seller_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        l = reg_seller.objects.all()
        for i in l:
            if (i.email == email and i.password == password):
                request.session['seller_id'] = i.id#global
                return redirect(seller_profile)
        else:
            return HttpResponse("Login Failed")
    return render(request,'seller_login.html')

def addproduct(request):
    id1 = request.session['seller_id']
    b = reg_seller.objects.get(id=id1)
    img = str(b.img_name).split('/')[-1]
    if request.method == 'POST':
        man_name = request.POST.get('man_name')
        med_name = request.POST.get('med_name')
        dosage = request.POST.get('dosage')
        qty = request.POST.get('qty')
        type = request.POST.get('type')
        price = request.POST.get('price')
        mtf = request.POST.get('mtf')
        med_pic = request.FILES.get('med_pic')
        a = product_add(man_name=man_name,med_name=med_name,dosage=dosage,qty=qty,type=type,price=price,mtf=mtf,med_pic=med_pic)
        a.save()
        # return HttpResponse('Product Added Successfully')
        return redirect(product_view)

    return render(request,'Add_product.html',{'img':img})

def seller_profile(request):
    id1=request.session['seller_id']
    a= reg_seller.objects.get(id=id1)
    image = str(a.img_name).split('/')[-1]
    return render(request,'seller_profile.html',{'data':a,'img':image})

def edit_seller_profile(request,id):
    a = reg_seller.objects.get(id=id)
    img = str(a.img_name).split('/')[-1]
    if request.method == 'POST':
        a.sname = request.POST.get('sname')
        a.email = request.POST.get('email')
        if request.FILES.get('img_name') == None:
            a.save()
        else:
            a.img_name = request.FILES['img_name']
            a.save()
        a.phone = request.POST.get('phone')
        a.cname = request.POST.get('cname')
        a.com_details = request.POST.get('com_details')
        a.save()
        return redirect(seller_profile)
    return render(request,'edit_seller_profile.html',{'data':a,'img':img})

def product_view(request):
    id1 = request.session['seller_id']
    b = reg_seller.objects.get(id=id1)
    img = str(b.img_name).split('/')[-1]
    a = product_add.objects.all()
    # img = str(a.med_pic).split('/')[-1]
    id = []
    man_name = []
    med_name = []
    dosage = []
    type = []
    price = []
    qty = []
    mtf = []
    med_pic = []
    for i in a:
        id1 = i.id
        id.append(id1)

        man_name1 = i.man_name
        man_name.append(man_name1)
        med_name1 = i.med_name
        med_name.append(med_name1)
        dosage1 = i.dosage
        dosage.append(dosage1)
        type1 = i.type
        type.append(type1)
        price1 = i.price
        price.append(price1)
        qty1 = i.price
        qty.append(qty1)
        mtf1 = i.mtf
        mtf.append(mtf1)
        med_pic1 = str(i.med_pic).split('/')[-1]
        med_pic.append(med_pic1)
    mylist=zip(id,man_name,med_name,dosage,type,price,mtf,med_pic,qty)
    return render(request,'product_view.html',{'data':mylist,'img':img})

def edit_product(request,id):
    a = product_add.objects.get(id=id)
    img = str(a.med_pic).split('/')[-1]
    id1 = request.session['seller_id']
    b = reg_seller.objects.get(id=id1)
    img1 = str(b.img_name).split('/')[-1]
    if request.method == 'POST':
        a.man_name = request.POST.get('man_name')
        a.med_name = request.POST.get('med_name')
        a.dosage = request.POST.get('dosage')
        a.type = request.POST.get('type')
        a.qty = request.POST.get('qty')
        a.price = request.POST.get('price')
        a.mtf = request.POST.get('mtf')
        if request.FILES.get('med_pic') == None:
            a.save()
        else:
            a.med_pic = request.FILES['med_pic']
            a.save()
        a.save()
        return redirect(product_view)
    return render(request,'edit_products.html',{'data':a,'img':img,'img1':img1})

def buyer_reg(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        buyer_img = request.FILES.get('buyer_img')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        a = reg_buyer.objects.all()
        buy_name = []
        buy_email = []
        if password == cpassword:
            for i in a:
                buy_name.append(i.username)
                buy_email.append(i.email)
                if username in buy_name:
                    return HttpResponse('Username is already taken!')
                elif email in buy_email:
                    return HttpResponse('Email is already taken!')

            b = reg_buyer(username=username,email=email,buyer_img=buyer_img,phone=phone,password=password)
            b.save()
            return redirect(buyer_login)
    return render(request,'Buyer_reg.html')

def buyer_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        a = reg_buyer.objects.all()
        for i in a:
            if (i.email == email and i.password == password):
                request.session['user_id'] = i.id
                request.session['username'] = i.username# global
                return redirect(buyer_index)
        else:
            return HttpResponse('Login Failed!')
    return render(request,'buyer_login.html')

def buyer_profile(request):
    id1 = request.session['user_id']
    a = reg_buyer.objects.get(id=id1)
    image = str(a.buyer_img).split('/')[-1]
    return render(request,'buyer_profile.html',{'data':a,'img':image})

def edit_buyer_profile(request):
    try:
        id1 = request.session['user_id']
        a = reg_buyer.objects.get(id=id1)
        img = str(a.buyer_img).split('/')[-1]
        if request.method == 'POST':
            a.username = request.POST.get('username')
            a.email = request.POST.get('email')
            a.phone =  request.POST.get('phone')
            if request.FILES.get('buyer_img') == None:
                a.save()
            else:
                a.buyer_img = request.FILES['buyer_img']
                a.save()
            a.save()
            return redirect(buyer_index)
    except:
        request.session['user_id'] = None
        return redirect(buyer_login)
    return render(request,'edit_buyer_profile.html',{'data':a,'img':img})

def buyer_logout(request):
    logout(request)
    return redirect(buyer_login)

def buyer_index(request):
    id1 = request.session['user_id']
    a = reg_buyer.objects.get(id=id1)
    img = str(a.buyer_img).split('/')[-1]
    if request.method == 'POST':
        a.username = request.POST.get('username')
        a.email = request.POST.get('email')
        a.phone = request.POST.get('phone')
        if request.FILES.get('buyer_img') == None:
            a.save()
        else:
            a.buyer_img = request.FILES['img_name']
            a.save()
        a.save()
        return redirect(buyer_profile)
    return render(request,'buyer_index.html',{'data':a,'img':img})
def filt_product_view(request, item):
    id1 = request.session['user_id']
    b = reg_buyer.objects.get(id=id1)
    img = str(b.buyer_img).split('/')[-1]
    a = product_add.objects.all()
    # img = str(a.med_pic).split('/')[-1]
    id = []
    man_name = []
    med_name = []
    dosage = []
    type = []
    price = []
    qty = []
    mtf = []
    med_pic = []
    for i in a:
        id1 = i.id
        id.append(id1)

        man_name1 = i.man_name
        man_name.append(man_name1)
        med_name1 = i.med_name
        med_name.append(med_name1)
        dosage1 = i.dosage
        dosage.append(dosage1)
        type1 = i.type
        type.append(type1)
        price1 = i.price
        price.append(price1)
        qty1 = i.price
        qty.append(qty1)
        mtf1 = i.mtf
        mtf.append(mtf1)
        med_pic1 = str(i.med_pic).split('/')[-1]
        med_pic.append(med_pic1)
    print(type)
    mylist=zip(id,man_name,med_name,dosage,type,price,mtf,med_pic,qty)
    return render(request,'filt_prod_view.html',{'data':mylist,"img":img,'item':item})

def prod_wishlist(request,id):
    a = product_add.objects.get(id=id)
    id1 = request.session['user_id']
    c = wishlist.objects.all()
    for i in c:
        if id == i.prod_id and id1 == i.user_id:
            return HttpResponse('Item already exist')
    else:
        b = wishlist(prod_id=a.id,user_id = id1,med_name1 = a.med_name , man_name1 = a.man_name, dosage1 = a.dosage,type1=a.type,qty1=a.qty,price1=a.price,mtf1=a.mtf,med_pic1=a.med_pic)
        b.save()
        return HttpResponse("item added succesfully")

def wishlist_view(request):
    id2 = request.session['user_id']
    b = reg_buyer.objects.get(id=id2)
    img = str(b.buyer_img).split('/')[-1]
    print(id2)
    a = wishlist.objects.all()
    # img = str(a.med_pic).split('/')[-1]
    id = []
    prod_id = []

    man_name = []
    med_name = []
    dosage = []
    type = []
    price = []
    qty = []
    mtf = []
    med_pic = []
    abc=[]

    for i in a:

        abc.append(i.user_id)
        prodid1 = i.prod_id
        prod_id.append(prodid1)
        id1 = i.id
        id.append(id1)

        man_name1 = i.man_name1
        man_name.append(man_name1)
        med_name1 = i.med_name1
        med_name.append(med_name1)
        dosage1 = i.dosage1
        dosage.append(dosage1)
        type1 = i.type1
        type.append(type1)
        price1 = i.price1
        price.append(price1)
        qty1 = i.qty1
        qty.append(qty1)
        mtf1 = i.mtf1
        mtf.append(mtf1)
        med_pic1 = str(i.med_pic1).split('/')[-1]
        med_pic.append(med_pic1)
    mylist=list(zip(abc,prod_id,id,man_name,med_name,dosage,type,price,mtf,med_pic,qty))
    return render(request,'wishlist_view.html',{'data':mylist,'id':id2,'img':img})

def delete_wish(request,id):
    a = wishlist.objects.get(id=id)
    id1 = request.session['user_id']
    a.delete()
    return redirect("http://127.0.0.1:8000/ecommapp/wishlist_view/")


def prod_cart(request,id):
    a = product_add.objects.get(id=id)
    id1 = request.session['user_id']
    prod_count = 0
    c = cart.objects.all()
    for i in c:
        if id == i.prod_id and id1 == i.user_id:
            i.qty1 +=1
            i.price1 = a.price * i.qty1
            i.save()
            return HttpResponse('Product Incremented')
            # messages.error(request,'Item Incremented')
    else:

        count=1
        b = cart(prod_id=a.id,user_id = id1,med_name1 = a.med_name , man_name1 = a.man_name, dosage1 = a.dosage,qty1=count,type1=a.type,price1=a.price,mtf1=a.mtf,med_pic1=a.med_pic)
        b.save()
        return HttpResponse("Added to cart")


        # messages.success(request, 'Added to cart')

    # return redirect(wishlist_view)
def cart_view(request):

    id2 = request.session['user_id']
    b = reg_buyer.objects.get(id=id2)
    img = str(b.buyer_img).split('/')[-1]
    print(id2)
    a = cart.objects.all()
    # img = str(a.med_pic).split('/')[-1]
    id = []
    prod_id = []

    man_name = []
    med_name = []
    dosage = []
    type = []
    price = []
    qty = []
    mtf = []
    med_pic = []
    userid = []

    for i in a:
        userid.append(i.user_id)
        prodid1 = i.prod_id
        prod_id.append(prodid1)
        id1 = i.id
        id.append(id1)

        man_name1 = i.man_name1
        man_name.append(man_name1)
        med_name1 = i.med_name1
        med_name.append(med_name1)
        dosage1 = i.dosage1
        dosage.append(dosage1)
        type1 = i.type1
        type.append(type1)
        price1 = i.price1
        price.append(price1)
        qty1 = i.qty1
        qty.append(qty1)
        mtf1 = i.mtf1
        mtf.append(mtf1)
        med_pic1 = str(i.med_pic1).split('/')[-1]
        med_pic.append(med_pic1)

    tp1 = []
    tp2 = []
    d = cart.objects.filter(user_id=id2)
    for i in d:
        # print(i.price)
        tp1.append(i.price1)
        # print(tp1)
    for i in tp1:
        tp2.append(int(i))
    # print(tp2)
    total_price=sum(tp2)
    if request.method == 'POST':
        code = request.POST.get('code')
        if code == 'MEDION100':
            if total_price>=1000:
                total_price = total_price-150
            elif total_price>=500:
                total_price = total_price - 100
            elif total_price>=300:
                total_price = total_price - 50
            else:
                total_price = sum(tp2)
        else:
            total_price = sum(tp2)


    prod_count = len(med_name)
    print(med_name)
    request.session['total_price'] = total_price
    mylist = list(zip(userid, prod_id, id, man_name, med_name, dosage, type, price, mtf, med_pic, qty))
    return render(request, 'cart_view.html', {'data': mylist, 'id': id2,'price':total_price,'img':img,'prod_count':prod_count})

def delete_cart(request,id):
    a = cart.objects.get(id=id)
    id1 = request.session['user_id']
    a.delete()
    return redirect(cart_view)

def cartinc(request,id):
    a = cart.objects.get(id=id)
    b = product_add.objects.get(id=a.prod_id)#main product model
    a.qty1 += 1
    a.price1 = b.price * a.qty1
    a.save()
    return redirect(cart_view)

def cartdec(request,id):
    a = cart.objects.get(id=id)
    b = product_add.objects.get(id=a.prod_id)
    a.qty1 -= 1
    a.price1 = b.price * a.qty1
    a.save()
    return redirect(cart_view)

def buyer_address(request):
    try:
        id2 = request.session['user_id']
        b = address_buyer.objects.get(user_id=id2)
        if b.address:
            return redirect(edit_buyer_address)
    except:
        if request.method == 'POST':
            fullname = request.POST.get('fullname')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            address = request.POST.get('address')
            state = request.POST.get('state')
            district = request.POST.get('district')
            city = request.POST.get('city')
            zip = request.POST.get('zip')
            a = address_buyer(user_id=id2,full_name=fullname,phone=phone,email=email,address=address,state=state,district=district,city=city,zip=zip)
            a.save()
            return redirect(buyer_payments)
    return render(request,'buyer_address.html')

def edit_buyer_address(request):
    id1 = request.session['user_id']
    a = address_buyer.objects.get(user_id=id1)
    if request.method == 'POST':
        a.full_name = request.POST.get('fullname')
        a.phone = request.POST.get('phone')
        a.email = request.POST.get('email')
        a.address = request.POST.get('address')
        a.state = request.POST.get('state')
        a.district = request.POST.get('district')
        a.city = request.POST.get('city')
        a.zip = request.POST.get('zip')
        a.save()
        return redirect(buyer_payments)
    return render(request,'edit_buyer_address.html',{'data':a})

def details_delivery(request):
    id1 = request.session['user_id']
    u_name = request.session['username']
    med_name = []
    dosage = []
    qty = []
    price1 = []
    a = cart.objects.all()
    for i in a:
        if i.user_id == id1:
            med_name.append(i.med_name1)
            dosage.append(i.dosage1)
            qty.append(i.qty1)
            price1.append(i.price1)
    b = address_buyer.objects.all()

    price = request.session['total_price']
    address1 = []
    prod_str = ''
    prod_img = ''
    ord_date = datetime.date.today()
    est_date = ord_date+timedelta(days=7)

    for i in b:
        if i.user_id == id1:
            address1.append(i.address)
            address1.append(i.state)
            address1.append(i.district)
            address1.append(i.city)
            address1.append(i.zip)
    print(address1)
    prod_list=[]
    for i in a:
        if i.user_id == id1:
            prod_str = "med_pic:"+str(i.med_pic1).split('/')[-1]+"|Med_name:"+str(i.med_name1)+"|Dosage:"+str(i.dosage1)+"|Quantiy:"+str(i.qty1)+"|price:"+str(i.price1)
            prod_list.append(prod_str)

    prod_strlist = "+".join(prod_list)
    print(prod_strlist)
    c = final_deliver(user_id=id1,address=address1,order_date=ord_date,est_del_date=est_date,products=prod_strlist,amount=price)
    c.save()

    for i in address1:
        print(i)
    subject = f"Thank you {u_name} for ordering!"
    message = f"Order Details" \
              f"Medicine : {med_name}, Dosage: {dosage}, Quantity : {qty}, Price : {price1}" \
              f"Total Amount : {price}"


    email_from = EMAIL_HOST_USER
    send_mail(subject,message,email_from,['nivedsankarpm7@gmail.com'])
    return redirect(order_details)

def deliver_display(request):
    # print('hahah')
    id2 = request.session['user_id']
    b = reg_buyer.objects.get(id=id2)
    img = str(b.buyer_img).split('/')[-1]
    med_pic = []
    med_name = []
    dosage = []
    qty = []
    price = []
    address = []
    ord_date = []
    del_date = []
    amount = []
    user_id = []
    a = final_deliver.objects.all()
    u_name = request.session['username']


    for i in a:

        if i.user_id == id2:
            items = i.products.split("+")
            #print(items)
            #print(i.products,type(i.products), i.user_id)
            for item in items:
                # print(item)

                # Split the item into key-value pairs
                key_value_pairs = item.split('|')
                # print(key_value_pairs)
                # print(len(key_value_pairs))

                # Ensure that the product data is in the expected format
                if len(key_value_pairs) == 5:
                    med_pic.append(key_value_pairs[0].split(':')[-1])
                    med_name.append(key_value_pairs[1].split(':')[-1])
                    dosage.append(key_value_pairs[2].split(':')[-1])
                    qty.append(key_value_pairs[3].split(':')[-1])
                    price.append(key_value_pairs[4].split(':')[-1])
                else:
                    # Handle unexpected data format or log an error
                    pass
            user_id.append(i.user_id)
            address.append(i.address)
            ord_date.append(i.order_date)
            del_date.append(i.est_del_date)
            amount.append(i.amount)
    print(med_pic)
    print(med_name)
    print(dosage)
    print(qty)
    print(price)
    mylist = zip(med_pic,med_name,dosage,qty,price,address,ord_date,del_date,amount,user_id)
    # for i,j,k,l,m,n,o,p,q,r in mylist:
    return render(request,'deliver_display.html',{'data':mylist,'u_name':u_name,'id':id2,'img':img})


def buyer_product_view(request):

    id1 = request.session['user_id']
    b = reg_buyer.objects.get(id=id1)
    img = str(b.buyer_img).split('/')[-1]
    a = product_add.objects.all()
    # img = str(a.med_pic).split('/')[-1]
    id = []
    man_name = []
    med_name = []
    dosage = []
    type = []
    price = []
    qty = []
    mtf = []
    med_pic = []
    for i in a:
        id1 = i.id
        id.append(id1)

        man_name1 = i.man_name
        man_name.append(man_name1)
        med_name1 = i.med_name
        med_name.append(med_name1)
        dosage1 = i.dosage
        dosage.append(dosage1)
        type1 = i.type
        type.append(type1)
        price1 = i.price
        price.append(price1)
        qty1 = i.price
        qty.append(qty1)
        mtf1 = i.mtf
        mtf.append(mtf1)
        med_pic1 = str(i.med_pic).split('/')[-1]
        med_pic.append(med_pic1)
    mylist=zip(id,man_name,med_name,dosage,type,price,mtf,med_pic,qty)
    return render(request,'buyer_product_view.html',{'data':mylist,"img":img})



def order_details(request):
    id2 = request.session['user_id']
    u_name = request.session['username']
    amount = request.session['total_price']
    med_pic = []
    med_name = []
    dosage = []
    qty = []
    price = []
    ord_date = []
    del_date = []
    a = cart.objects.all()
    for i in a:
        if i.user_id == id2:
            med_pic.append(str(i.med_pic1).split('/')[-1])
            med_name.append(i.med_name1)
            dosage.append(i.dosage1)
            qty.append(i.qty1)
            price.append(i.price1)
            # ord_date.append(i.order_date)
            # del_date.append(i.est_del_date)
    print(med_pic)
    print(med_name)

    mylist = zip(med_pic,med_name,dosage,qty,price)
    d = cart.objects.all()
    d.delete()
    return render(request,'ordered_products.html',{'data':mylist,'amount':amount,'u_name':u_name})

# def user_delivery_details(request):
#     id2 = request.session['user_id']
#     u_name = request.session['username']
#     amount = request.session['total_price']
#     med_name = []
#     med_pic = []
#     qty = []
#     dosage = []
#     price = []
#     address = []
#     city = []
#     district = []
#     state = []
#     zip = []
#     ord_date = datetime.date.today()
#     est_date = ord_date + timedelta(days=7)
#     a = cart.objects.all()
#     b = address_buyer.objects.all()
#     for i in a:
#         if i.user_id == id2:
#             med_name.append(i.med_name1)
#             med_pic.append(str(i.med_pic1).split('/')[-1])
#             qty.append(i.qty1)
#             dosage.append(i.dosage1)
#             price.append(i.price1)
#     for i in b:
#         if i.user_id == id2:
#             address.append(i.address)
#             city.append(i.city)
#             district.append(i.district)
#             state.append(i.state)
#             zip.append(i.zip)
#
#     c = user_deliver(user_id=id2,med_name=med_name,med_pic=med_pic,qty=qty,dosage=dosage,price=price,address=address,city=city,state=state,district=district,zip=zip,order_date=ord_date,est_del_date=est_date,amount=amount)
#     c.save()
#     subject = f"Thank you {u_name} for ordering!"
#     message = f"Order Details" \
#               f"Medicine : {med_name}, Dosage: {dosage}, Quantity : {qty}, Price : {price}" \
#               f"Total Amount : {amount}"
#
#     email_from = EMAIL_HOST_USER
#     send_mail(subject, message, email_from, ['nivedsankarpm7@gmail.com'])
#     return redirect(order_details)
def buyer_payments(request):
    amount = request.session['total_price']
    u_name = request.session['username']
    return render(request,'buyer_payments.html',{'total':amount,'u_name':u_name})

