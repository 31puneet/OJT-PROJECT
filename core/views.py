from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Page, PageVersion
from .forms import PageForm
import diff_match_patch as dmp_module

# Helper function
def save_version(page, user):
    PageVersion.objects.create(
        page=page,
        content=page.content,
        cover_image=page.cover_image,
        category=page.category,
        status=page.status,
        created_by=user
    )

@login_required
def dashboard(request):
    all_pages = Page.objects.all().order_by('-last_updated')
    return render(request, 'dashboard.html', {'pages': all_pages})

@login_required
def create_page(request):
    if request.method == 'POST':
        form = PageForm(request.POST, request.FILES)
        if form.is_valid():
            page = form.save(commit=False)
            page.created_by = request.user
            page.save()
            save_version(page, request.user)
            return redirect('dashboard')
    else:
        form = PageForm()
    return render(request, 'editor.html', {'form': form, 'title': 'Create New Page'})

@login_required
def edit_page(request, page_id):
    page = get_object_or_404(Page, id=page_id)
    if request.method == 'POST':
        form = PageForm(request.POST, request.FILES, instance=page)
        if form.is_valid():
            page = form.save()
            save_version(page, request.user)
            return redirect('dashboard')
    else:
        form = PageForm(instance=page)
    return render(request, 'editor.html', {'form': form, 'title': f'Edit: {page.title}'})

@login_required
def delete_page(request, page_id):
    page = get_object_or_404(Page, id=page_id)
    page.delete()
    return redirect('dashboard')

def history_list(request, page_id):
    page = get_object_or_404(Page, id=page_id)
    versions = page.versions.all().order_by('-created_at')
    return render(request, 'history.html', {'page': page, 'versions': versions})

# === THIS IS THE CRITICAL FUNCTION ===
def compare_view(request):
    # Get IDs from URL (e.g. ?ids=1,2,3)
    ids_param = request.GET.get('ids', '')
    if not ids_param:
        return redirect('dashboard')
    
    try:
        id_list = [int(x) for x in ids_param.split(',')]
    except ValueError:
        return redirect('dashboard')

    versions = PageVersion.objects.filter(id__in=id_list).order_by('created_at')
    
    if not versions:
        return redirect('dashboard')

    columns = []
    dmp = dmp_module.diff_match_patch()
    previous_content = None

    for v in versions:
        diff_html = ""
        if previous_content is not None:
            diffs = dmp.diff_main(previous_content, v.content)
            dmp.diff_cleanupSemantic(diffs)
            diff_html = dmp.diff_prettyHtml(diffs)
        else:
            diff_html = v.content

        columns.append({
            'version': v,
            'raw_content': v.content,
            'diff_html': diff_html,
            'has_diff': (previous_content is not None)
        })
        previous_content = v.content

    return render(request, 'compare.html', {'columns': columns})

def restore_version(request, version_id):
    old = get_object_or_404(PageVersion, id=version_id)
    curr = old.page
    curr.content = old.content
    curr.cover_image = old.cover_image
    curr.category = old.category
    curr.status = old.status
    curr.save()
    save_version(curr, request.user)
    return redirect('history', page_id=curr.id)