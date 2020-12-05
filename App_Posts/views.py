from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from App_Login.models import UserProfile, Follow
from App_Posts.models import Posts, Liked
from django.contrib.auth.models import User


# Create your views here.
@login_required
def home(request):
    following_list=Follow.objects.filter(follower=request.user)
    posts = Posts.objects.filter(author__in=following_list.values_list('following'))
    post_liked = Liked.objects.filter(user=request.user)
    liked_post_list = post_liked.values_list('post', flat=True)
    print(liked_post_list)
    if request.method == 'GET':
        search = request.GET.get('search', '') #the name of search section for get the keyword that was searched
        result = User.objects.filter(username__icontains=search)
    return render(request, 'App_Posts/home.html', context={'title':'homepage', 'search': search, 'result':result, 'posts':posts, 'liked_post_list':liked_post_list})


@login_required
def like(request, pk):
    post = Posts.objects.get(pk=pk)
    already_liked = Liked.objects.filter(post=post, user=request.user)
    if not already_liked:
        post_liked = Liked(post=post, user=request.user)
        post_liked.save()
        return HttpResponseRedirect(reverse('home'))


@login_required
def unlike(request, pk):
    post = Posts.objects.get(pk=pk)
    already_liked = Liked.objects.filter(post=post, user=request.user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('home'))
