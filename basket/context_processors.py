from .basket import Basket


def basket(request):
    basket = Basket(request)
    length = basket.__len__()

    return {'basket_total': length}


    