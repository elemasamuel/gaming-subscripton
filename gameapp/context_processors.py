from .models import Category
from .forms import GameSearchForm


def category_links(request):
    category = Category.objects.all()
    return {'categories': category}


def game_search(request):
    search_form = GameSearchForm
    if request.method == 'POST':
        search_form = GameSearchForm(request.POST)
        if search_form.is_valid():
            search_form.save()
    return{'search_form': search_form}

