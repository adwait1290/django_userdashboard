from django.shortcuts import render, HttpResponse, redirect
from .models import User, Message, Comment, Friend, UserManager
# Create your views here.
def remove(request, id):
    User.userManager.get(id=id).delete()
    return redirect('/dashboard/admin')

def edit(request):
    return render(request, 'edit.html')

def editAdmin(request, id):
    context = {
        'user_id' : id
    }
    return render(request, 'editAdmin.html', context)

def editInfo(request):
    user_id = request.session['id']
    user = User.objects.get(id=user_id)
    user.email = request.POST['email']
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.save()
    return redirect('/dashboard')

def editPassword(request):
    user_id = request.session['id']
    if (not User.userManager.updatePassword(request.POST['password'], request.POST['password_confirmation'], user_id)):
        return redirect('/dashboard')
    else:
        return HttpResponse('errors')

def editDescription(request):
    user_id = request.session['id']
    user = User.objects.get(id=user_id)
    user.description = request.POST['description']
    user.save()
    return redirect('/dashboard')

def new_user(request):
    return render(request, 'new_user.html')

def specificEditInfo(request, id):
    user = User.objects.get(id=id)
    user.email = request.POST['email']
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.user_level = request.POST['user_level']
    user.save()
    return redirect('/dashboard/admin')

def specificEditPassword(request, id):
    if (not User.userManager.updatePassword(request.POST['password'], request.POST['password_confirmation'], id)):
        return redirect('/dashboard/admin')
    else:
        return HttpResponse('errors')

def profile(request, id):
	user = User.objects.get(id=id)
	try:
		users = User.objects.all()
		others = []
		for other_user in users:
			if (other_user.id != request.session['id']):
				others.append(other_user)
	except:
		users = None
	try:
		real_friends = []
		real_others = []
		friends = Friend.objects.filter(user_friend=me)
		for each_friend in friends:
			real_friends.append(each_friend.second_friend)
		for other_user in others:
			if (other_user not in real_friends):
				real_others.append(other_user)
	except:
		friends = None
	try:
		messages = Message.objects.filter(user_id=user)
		comments = Comment.objects.all()
	except:
		messages = None
	context = {
	'user' : user,
	'messages' : messages,
	'comments' : comments,
	'users' : others,
	'friends' : real_friends,
	}
	print context
	return render(request, 'show.html', context)

def post_message(request, id):
    Message.messageManager.addUser(request.POST['message'], id, request.session['id'])
    return redirect('/dashboard')

def post_comment(request, id, id2):
    Comment.commentManager.addComment(request.POST['comment'], id, id2)
    return redirect('/dashboard')
def add_friend(request, id):
    User.userManager.addFriend(request.session['id'], id)
    return redirect('/friends')

def remove_friend(request, id):
    User.userManager.removeFriend(request.session['id'], id)
    return redirect('/friends')

