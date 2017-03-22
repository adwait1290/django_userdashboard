from django.shortcuts import render, HttpResponse, redirect
from .models import User, Friend,UserManager
from django.core.urlresolvers import reverse
# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    context = {
        'type' : True
    }
    print context['type']
    return render(request, 'reg.html', context)

def signin(request):
    context = {
        'type' : False
    }
    print context['type']
    return render(request, 'reg.html', context)

def create(request):
    results = User.userManager.register(request.POST['first_name'], request.POST['last_name'], request.POST['email'], request.POST['password'], request.POST['password_confirmation'], request.POST['user_level'])
    if not results[0]:
        print results[1]
        return HttpResponse('errors')
    else:
        print results[1]
        context = {
            'users' : User.objects.all()
        }
        return redirect('/signin')

def create_new(request):
    results = User.userManager.register(request.POST['first_name'], request.POST['last_name'], request.POST['email'], request.POST['password'], request.POST['password_confirmation'], request.POST['user_level'])
    if not results[0]:
        print results[1]
        return HttpResponse('errors')
    else:
        print results[1]
        context = {
            'users' : User.objects.all()
        }
        return redirect('/dashboard/admin')

def login(request):
    results = User.userManager.login(request.POST['email'], request.POST['password'])
    if not results[0]:
        return HttpResponse('failed')
    else:
        request.session['id'] = results[1].id
        if (results[1].user_level >= 9):
            return redirect('/dashboard/admin')
        else:
            return redirect('/dashboard')

def logoff(request):
    request.session['id'] = 0;
    return redirect('/')
def friends(request):
    me = User.objects.get(id=request.session['id'])
    try:
        users = User.objects.all()
        others = []
        for other_user in users:
            if (other_user.id != request.session['id']):
                others.append(other_user)
    except:
        users = None

    try:
        friends = Friend.objects.filter(user_friend=me)
        real_friends = []
        for each_friend in friends:
            real_friends.append(each_friend.second_friend)
        real_others = []
        for other_user in others:
            if (other_user not in real_friends):
                real_others.append(other_user)
    except:
        friends = None

    context = {
        'me' : me,
        'users' : real_others,
        'friends' : real_friends
    }
    print context
    return render(request, 'friends.html', context)

def profile(request, id):
	try:
		users = User.objects.all()
		others = []
		for other_user in users:
			if (other_user.id != request.session['id']):
				others.append(other_user)
	except:
		users = None

	try:
		friends = Friend.objects.filter(user_friend=me)
		real_friends = []
		for each_friend in friends:
			real_friends.append(each_friend.second_friend)
		real_others = []
		for other_user in others:
			if (other_user not in real_friends):
				real_others.append(other_user)
	except:
		friends = None
	profile = User.objects.get(id=id)
	context = {
        'user' : profile,
        'userss' : real_others,
        'friends' : friends
	}
	print userss

	return render(request, 'profile.html', context)

def add_friend(request, id):
    User.userManager.addFriend(request.session['id'], id)
    return redirect(request, 'profile.html',id)
def remove_friend(request, id):
    User.userManager.removeFriend(request.session['id'], id)
    return redirect('/friends')
