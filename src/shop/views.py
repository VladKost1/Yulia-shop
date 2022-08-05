from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView

from shop.models import Category, Order, OrderItem, Product
from shop.forms import CheckoutForm


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
    context_object_name = "all_categories"


class CategorySelectView(ListView):
    model = Product
    template_name = "category_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategorySelectView, self).get_context_data(**kwargs)
        filtered_products = Product.objects.filter(category__slug=self.kwargs["cat_slug"])
        context.update({"all_products": filtered_products})
        return context


def location(request):
    return render(request, "location.html")


def cart(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        if request.method == 'POST':
            product = Product.objects.filter(uuid=request.POST.get("product")).first()
            OrderItem.objects.create(product=product, quantity=1, order=order)
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0}
        cartItems = ["get_cart_item"]

    context = {"items": items, "order": order, "cartItems": cartItems}
    return render(request, "cart.html", context)


def add_cart(request, product):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        if request.method == 'POST':
            product = Product.objects.filter(uuid=product).first()
            if not order.orderitem_set.filter(product=product).exists():
                OrderItem.objects.create(product=product, quantity=1, order=order)
            else:
                order_item = order.orderitem_set.filter(product=product).first()
                order_item.quantity += 1
                order_item.save()
    return redirect("shop:cart")


def delete_cart(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        if request.method == 'POST':
            OrderItem.objects.filter(order=order).delete()
    return render(request, "cart.html")


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        if request.method == 'POST':
            form = CheckoutForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Your order has been successfully completed")
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0}
        cartItems = ["get_cart_item"]

    form = CheckoutForm()
    context = {"form": form, "items": items, "order": order, "cartItems": cartItems}
    return render(request, "checkout.html", context)

