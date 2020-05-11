from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from form_app.models import Post


# Create your views here.
def index(request):
    new_post = Post(post_title='First Post', post_content = 'First post content!!')
    new_post.save()

    demo = {
        'new_post': new_post,
    }
    return render(request, 'form_app/index.html', context=demo)
