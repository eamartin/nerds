from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import RegForm, ScheduleForm, LoginForm, UserSelectForm
from models import Class

def home(request):
	return render_to_response('home.html', {'user': request.user})

def reg(request):
	form = RegForm()
	if request.method == 'POST':
		form = RegForm(request.POST)
		if form.is_valid():
			print 'form is valid'
			cd = form.cleaned_data
			u = User.objects.create_user(cd['username'], cd['email'], cd['pw'])
			u.first_name = cd['first_name']
			u.last_name = cd['last_name']
			u.save()
			u = authenticate(username=cd['username'], password=cd['pw'])
			login(request,u)
			return HttpResponseRedirect(reverse('home'))
	return render_to_response('registration.html', {'reg_form': form, 'login_form': LoginForm()}, context_instance=RequestContext(request))
	
def login_view(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = User.objects.get(email=cd['email'])
			user = authenticate(username=user.username, password=cd['password'])
			if user:
				login(request, user)
				return HttpResponseRedirect(reverse('home'))
	return HttpResponseRedirect(reverse('classic_reg'))
	
def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse('home'))
	
def overview(request):
	if 'user_select' in request.GET:
		return HttpResponseRedirect(reverse('view_sched', kwargs={'user_id': request.GET['user_select']}))
	else:
		return render_to_response('overview.html', {'user': request.user, 'form': UserSelectForm()})
	
@login_required
def edit_schedule(request):
	form = ScheduleForm()
	if request.method == 'POST':
		form = ScheduleForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			request.user.classes = []
			if cd.get('new_classes'):
				for cls_num in cd['new_classes']:
					request.user.classes.create(period=cd['p_'+str(cls_num)], teacher=cd['teacher_'+str(cls_num)], 
												dif=cd['dif_'+str(cls_num)], subject=cd['subject_'+str(cls_num)])
			if cd.get('old_classes'):
				for cls_num in cd['old_classes']:
					request.user.classes.add(cd['class_'+str(cls_num)])
			return HttpResponseRedirect(reverse('home'))
	return render_to_response('edit_sched.html', {'form': form}, context_instance=RequestContext(request))
	
def view_sched(request, user_id=''):
	if not user_id:
		return HttpResponseNotFound()
	else:
		student = User.objects.get(id=user_id)
	return render_to_response('view_sched.html', {'student': student, 'user': request.user})
