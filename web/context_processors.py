from web.models.forms import SearchForm, SimpleSearchForm


def search_form(request):
    return {
        'search_form': SearchForm(),
        'simple_search_form': SimpleSearchForm()
    }
