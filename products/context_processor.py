from products.models import Category


def categories(request):
    """
    context processor for make category root in navbar
    :param request:
    :return:
    """
    queryset = Category.objects.filter(parent=None)
    return {
        'cat_root': queryset
    }