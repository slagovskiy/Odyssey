from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from apps.blog.models import Tag


def index(request):
    content = {
    }
    return render(request, 'oadmin/index.html', content)


def tag(request):
    content = {
    }
    return render(request, 'oadmin/tag.html', content)


def tag_all(request):
    data = serializers.serialize('json', Tag.objects.all())
    return JsonResponse(data, safe=False)


def tag_edit(request, id):
    data = serializers.serialize('json', Tag.objects.all().filter(id=id))
    return JsonResponse(data, safe=False)


def tag_save(request):
    try:
        id = int(request.POST['id'])
        slug = str(request.POST['txtSlug'])
        name = str(request.POST['txtName'])
        deleted = False
        if request.POST['deleted'] == 'true':
            deleted = True
        if id == -1:
            tag = Tag.objects.create(
                slug=slug,
                name=name,
                deleted=deleted
            )
            tag.save()
            return HttpResponse('ok')
        else:
            tag = Tag.objects.get(id=id)
            if tag:
                tag.slug = slug
                tag.name = name
                tag.deleted = deleted
                tag.save()
                return HttpResponse('ok')
            else:
                return HttpResponse('error get object')
    except Exception as ex:
        return HttpResponse(ex)
