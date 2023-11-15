from django.shortcuts import render
def page_not_found_view(request, *args, **kwargs):
    return render(request, 'error_404.html')


def server_error_view(request, *args, **kwargs):
    return render(request, 'error_500.html')

