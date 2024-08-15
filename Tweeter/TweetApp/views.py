from django.shortcuts import render
from .models import Tweet
from .forms import TweetFrom,UserRegistrationForm
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth import logout
from .forms import SearchForm
from django.template.loader import render_to_string
from django.http import JsonResponse


# Create your views here.
def index(request):
    return render(request,'index.html')

def tweet_list(request):
    tweets=Tweet.objects.all().order_by('created_at')
    return render(request,'tweet_list.html',{'tweets':tweets})

@login_required
def tweet_create(request):
    if request.method=="POST":
        form=TweetFrom(request.POST,request.FILES)
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user=request.user
            tweet.save()
            redirect('tweet_list')
    else:
        form=TweetFrom()
    return render(request,'tweet_form.html',{'form':form})

@login_required
def tweet_edit(request,tweet_id):
    tweet=get_object_or_404(Tweet,pk=tweet_id,user= request.user)
    if request.method=="POST":
        form=TweetFrom(request.POST,request.FILES,instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list') 
    else:
        form = TweetFrom(instance=tweet)
    return render(request,'tweet_form.html',{'form':form})

@login_required
def tweet_delete(request,tweet_id):
    tweet=get_object_or_404(Tweet,pk=tweet_id,user=request.user)
    if request.method=="POST":
        tweet.delete()
        return redirect('tweet_list')
    return render(request,'tweet_confirm_delete.html',{'tweet':tweet})

def register(request):
    if request.method=="POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('tweet_list')
    else:
        form = UserRegistrationForm()
    return render(request,'registration/register.html',{'form':form})


def logout_view(request, tweet_id):
    logout(request)
    return redirect('tweet_list')

def tweet_search(request):
    form = SearchForm(request.GET or None)
    tweets = Tweet.objects.all()
    
    if form.is_valid():
        query = form.cleaned_data['query']
        if query:
            tweets = tweets.filter(text__icontains=query)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        results_html = render_to_string('tweet_search_results.html', {'tweets': tweets})
        return JsonResponse({'results': results_html})

    return render(request, 'tweet_list.html', {'form': form, 'tweets': tweets})

def like_tweet(request, tweet_id):
    if request.method == 'POST':
        tweet = get_object_or_404(Tweet, id=tweet_id)
        user = request.user
        if user in tweet.likes.all():
            tweet.likes.remove(user)
            liked = False
        else:
            tweet.likes.add(user)
            liked = True

        return JsonResponse({
            'success': True,
            'like_count': tweet.like_count(),
            'liked': liked
        })
    return JsonResponse({'success': False}, status=400)