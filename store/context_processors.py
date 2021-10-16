from .models import Category, ServiceCategory


def categories(request):
    return {
        'categories': Category.objects.all(),
        'service_categories': ServiceCategory.objects.all()
    }