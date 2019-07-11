from .forms import LoginForm

def add_variable_to_context(request):
    form = LoginForm()
    return {
        'form': form
    }