from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404

from items.models import Item

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, product_id):
    """ Add a quantity of the specified product to the shopping bag """

    item = get_object_or_404(Item, pk=product_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if product_id in list(bag.keys()):
        bag[product_id] += quantity
        
    else:
        bag[product_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)
