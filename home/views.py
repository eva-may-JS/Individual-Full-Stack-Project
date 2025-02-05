from django.shortcuts import render


def HomePage(request):
    """
    Renders the home page

    **Template:**

    :template:`home/index.html`
    """
    return render(request, 'home/index.html')
