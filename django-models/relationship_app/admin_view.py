from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .views import is_admin

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')
