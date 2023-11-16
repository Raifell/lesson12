from django.shortcuts import render, redirect
from shop_side.models import Product, Category


def product_create_view(request):
    context = {'category_list': Category.objects.all()}

    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        category = request.POST.get('category')

        product = Product()
        product.name = name
        product.price = price
        product.quantity = quantity
        product.category = Category.objects.get(
            pk=category
        )

        product.save()

        return redirect('product_list')

    return render(request,
                  'shop_side/product_create.html',
                  context)


def product_delete_view(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    product.delete()

    return redirect('product_list')


def product_update_view(request, product_slug):
    product = Product.objects.get(slug=product_slug)

    if request.method == "POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        category = request.POST.get('category')

        product.name = name
        product.price = price
        product.quantity = quantity
        product.category = Category.objects.get(
            pk=category
        )

        product.save()

        return redirect('product_list')

    context = {
        'product': product,
        'category_list': Category.objects.all()
    }
    return render(request,
                  'shop_side/product_update.html',
                  context)









