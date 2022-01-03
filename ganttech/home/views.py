from django.db.models import Count
from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from home.models import Category, Brand, Color, Size, Product, Images
from comment.models import Comment, CommentForm
from order.models import ShopCart
from django.contrib import messages



def base(request):
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id=current_user.id)

    total = 0
    for rs in shopcart:
        total += rs.product.price * rs.quantity

    context = {
        'shopcart': shopcart,
        'total': total
    }

    return render(request, 'base.html', context)




def index(request):
    category = Category.objects.all()
    category_el = Category.objects.first()
    product = Product.objects.all()
    product_circle = Product.objects.order_by('?')[:6]
    category_circle = Category.objects.order_by('?')[:7]

    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id=current_user.id)

    total = 0
    for rs in shopcart:
        total += rs.product.price * rs.quantity


    context = {
        'category': category,
        'product': product,
        'product_circle': product_circle,
        'category_circle': category_circle,
        'category_el': category_el,
        'shopcart': shopcart,
        'total': total
    }

    return render(request, 'index.html', context)


def get_search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        product_search = Product.objects.filter(title__contains=searched)


        return render(request, 'search.html', {'searched': searched, 'product_search': product_search})
    else:

        return render(request, 'search.html')




def get_single(request, slug:int):
    product_single = get_object_or_404(Product, id=slug)
    category = Category.objects.all()
    images = Images.objects.filter(product_id=slug)
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id=current_user.id)

    total = 0
    for rs in shopcart:
        total += rs.product.price * rs.quantity


    product_circle = Product.objects.order_by('?')[:7]

    comments = Comment.objects.filter(product=product_single)

    if request.method == 'POST':  # check post
        form = CommentForm(request.POST)
        if form.is_valid():
            data = Comment()  # create relation with model
            data.username = form.cleaned_data['username']
            data.comment = form.cleaned_data['comment']
            data.rate = form.cleaned_data['rate']
            data.ip = request.META.get('REMOTE_ADDR')
            data.product_id = slug
            current_user = request.user
            data.user_id = current_user.id
            data.save()  # save data to table
            messages.success(request, "Your review has ben sent. Thank you for your interest.")
            return HttpResponseRedirect(reverse('single', args=[slug]))
    else:
        form = CommentForm()


    context = {
        'product_single': product_single,
        'category': category,
        'images': images,
        'product_circle': product_circle,
        'comments': comments,
        'form': form,
        'shopcart': shopcart,
        'total': total,
    }

    return render(request, 'product.html', context)


def is_valid_queryparam(param):
    return param != '' and param is not None



def get_category(request, category_id):
    category = Category.objects.get(pk=category_id)
    products = Product.objects.filter(category_id=category_id)
    categories = Category.objects.all().annotate(posts_count=Count('product'))
    brands = Brand.objects.all()
    view_count_min = request.GET.get('view_count_min')
    view_count_max = request.GET.get('view_count_max')
    brand = request.GET.get('brand')


    for cat in categories:
        print(cat.posts_count)



    if is_valid_queryparam(view_count_min):
        products = products.filter(price__gte=view_count_min)

    if is_valid_queryparam(view_count_max):
        products = products.filter(price__lt=view_count_max)

    if is_valid_queryparam(brand):
        products = products.filter(brand__name=brand)

    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id=current_user.id)

    total = 0
    for rs in shopcart:
        total += rs.product.price * rs.quantity


    context = {
        'products': products,
        'category': category,
        'brands': brands,
        'categories': categories,
        'shopcart': shopcart,
        'total': total
    }
    return render(request, 'category.html', context)


def test(request):
    return render(request, 'test.html')