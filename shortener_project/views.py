from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.views.decorators.cache import never_cache
from .models import ShortURL
from .forms import URLForm

@login_required
def dashboard_view(request):
    urls = ShortURL.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'urls': urls})

@login_required
def create_short_url(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            short_url = form.save(commit=False)
            short_url.user = request.user
            short_url.save()
            return redirect('dashboard')
    else:
        form = URLForm()
    return render(request, 'create_short_url.html', {'form': form})

def redirect_short_url(request, code):
    url = get_object_or_404(ShortURL, short_code=code)
    url.click_count += 1
    url.save()
    return redirect(url.original_url)

@login_required
def delete_short_url(request, id):
    url = get_object_or_404(ShortURL, id=id, user=request.user)
    url.delete()
    return redirect('dashboard')

@login_required
@require_GET
@never_cache
def clicks_snapshot(request):
    """Return current click counts for the logged-in user's URLs.
    Response format: {"clicks": [{"id": <int>, "click_count": <int>}, ...]}
    """
    qs = ShortURL.objects.filter(user=request.user).values('id', 'click_count')
    return JsonResponse({"clicks": list(qs)})
