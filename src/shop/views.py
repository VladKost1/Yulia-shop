import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import DetailView, ListView
from accounts.models import Customer
from shop.models import Order, Category, Product, OrderItem


class IndexView(ListView):
    template_name = "index.html"
    queryset = Product.objects.all()
    context_object_name = "all_products"
    paginate_by = 3


class ProductDetailView(DetailView):
    template_name = "product_details.html"
    model = Product

    def get_object(self, queryset=None):
        return Product.objects.get(uuid=self.kwargs.get("uuid"))


class CategoryView(ListView):
    model = Category
    template_name = "category.html"
    context_object_name = 'all_categories'


class CategorySelectView(ListView):
    model = Product
    template_name = "category_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategorySelectView, self).get_context_data(**kwargs)
        filtered_products = Product.objects.filter(category__slug=self.kwargs['cat_slug'])
        context.update({'all_products': filtered_products})
        return context


class AccountView(ListView):
    template_name = "account.html"
    model = Customer


def location(request):
    return render(request, 'location.html')


def cart(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = ['get_cart_item']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'cart.html', context)


# def updateItem(request):
#     data = json.loads(request.body)
#     productId = data['productId']
#     action = data['action']
#     print(type(productId))
#     print(productId)
#     print('Action:', action)
#     print('Product:', productId)
#
#     customer = request.user.customer
#     product = Product.objects.get(id=productId)
#     order, created = Order.objects.get_or_create(customer=customer, complete=False)
#
#     orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
#
#     if action == 'add':
#         orderItem.quantity = (orderItem.quantity + 1)
#     elif action == 'remove':
#         orderItem.quantity = (orderItem.quantity - 1)
#
#     orderItem.save()
#
#     if orderItem.quantity <= 0:
#         orderItem.delete()
#
#     return JsonResponse('Item was added', safe=False)

