from turtle import title
from django.shortcuts import render, redirect  
from insert.models import Products, Title 
import os

def index(request):  
    return render(request,'index.html')  

def img(request):
    if request.method == "POST":
        pname = request.POST['pname']
        pprice = request.POST['pprice']
        pquantity = request.POST['pquantity']
        # image = request.FILES['image']
        if request.FILES.get('image') is not None:
            image= request.FILES['image']
        else:
            image= "/static/image/shoe.png"
            
        # try:
        #     image = request.FILES['image']
        # except:
        #     image = 'images/shoe.png'
        prd = Products(productname=pname,productprice=pprice,productquantity=pquantity,productimage=image)
        print("Data Saved...")
        prd.save()
        return redirect('/show')
    else:
        return render('index.html')
    
def img(request):
    if request.method == "POST":
        pname = request.POST['pname']
        pprice = request.POST['pprice']
        pquantity = request.POST['pquantity']
        if request.FILES.getlist('image') is not None:
            image= request.FILES['image']
        else:
            image= "/static/image/shoe.png"
            
        # try:
        #     image = request.FILES['image']
        # except:
        #     image = 'images/shoe.png'
        prd = Products(productname=pname,productprice=pprice,productquantity=pquantity,productimage=image)
        print("Data Saved...")
        prd.save()
        return redirect('/show')
    else:
        return render('index.html')

     
def show(request):  
    prdcts = Products.objects.all()  
    return render(request,'show.html',{'prdcts':prdcts})  

def edit(request, id):  
    product = Products.objects.get(id=id)  
    return render(request,'edit.html', {'product':product})  

def update_data(request, id):
    if request.method == "POST":
        updateproduct = Products.objects.get(id=id) 
        updateproduct.productname = request.POST.get('upname')
        updateproduct.productprice = request.POST.get('upprice')
        updateproduct.productquantity = request.POST.get('upquantity')
        if request.FILES.get('upimage') is not None:
            if not updateproduct.productimage == "/static/image/shoe.png":
                os.remove(updateproduct.productimage.path)
                updateproduct.productimage = request.FILES['upimage']
            else:
                updateproduct.productimage = request.FILES['upimage']
        else:
            os.remove(updateproduct.productimage.path)
            updateproduct.productimage = "/static/image/shoe.png"
        updateproduct.save()
        return redirect('/show')
    return render(request, 'edit.html')

# def update(request, id):  
#     product = Products.objects.get(id=id)  
#     form = Products(request.POST, instance = product)  
#     if form.is_valid():  
#         form.save()  
#         return redirect('show')  
#     return render(request, 'edit.html', {'product': product})  

def destroy(request, id):  
    delproduct = Products.objects.get(id=id)  
    if delproduct.productimage is not None:
        if not delproduct.productimage == "/static/image/shoe.png":
            os.remove(delproduct.productimage.path)
        else:
            pass
    delproduct.delete()
    # product.delete()  
    return redirect('/show')  


def item(request):
    return render(request, 'item.html')
def add_image(request, id):
    if request.method == "POST":
        images= request.FILES.getlist('images')
        titls = title.objects.get(id)
        for img in images:
            imagesave = Title(title=titls, image=img)
            imagesave.save()
            print("save")
        return redirect('pro_home')
    return render(request, 'item.html')
            