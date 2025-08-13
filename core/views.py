from django.shortcuts import render


# vista de función (def) - Vista de Inicio de nuestro página/blog
def HomeView(request):
    context = {}
    return render(request, "index.html", context)


# ------------------------------------------------------------------------------

