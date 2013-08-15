from django import forms
from django.contrib.auth.models import User
from django.db.models import Count
from models import Class, MyUser

class RegForm(forms.Form):
	first_name = forms.CharField()
	last_name = forms.CharField()
	email = forms.EmailField()
	pw = forms.CharField(widget=forms.PasswordInput, label='Password')
	pw_again = forms.CharField(widget=forms.PasswordInput, label='Password Again')
	
	def clean(self):
		cd = self.cleaned_data
		if len(cd['first_name'] + cd['last_name']) < 3:
			raise forms.ValidationError('This name is too short')
		n = 1
		cd['username'] = cd['first_name'] + '.' + cd['last_name']
		while User.objects.filter(username=cd['username']).exists():
			cd['username'] += str(n)
			n += 1
		return cd
		
	def clean_first_name(self):
		cd = self.cleaned_data		
		cd['first_name'] = cd['first_name'].title()
		return cd['first_name']
		
	def clean_last_name(self):
		cd = self.cleaned_data
		cd['last_name'] = cd['last_name'].title()
		return cd['last_name']
		
	def clean_email(self):
		if User.objects.filter(email=self.cleaned_data['email']).exists():
			raise forms.ValidationError('Someone has already registered with that email')
		else:
			return self.cleaned_data['email']
		
	def clean_pw_again(self):
		cd = self.cleaned_data
		if cd['pw'] != cd['pw_again']:
			raise forms.ValidationError('Passwords do not match')
		else:
			return cd['pw_again']
			
class LoginForm(forms.Form):
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput)
	
class UserSelectForm(forms.Form):
	user_select = forms.ModelChoiceField(queryset= MyUser.objects.annotate(num_classes=Count('classes')).filter(num_classes__gt=0))

'''def fix(cls):
	for k in xrange(1,8):
		print 'class_'+str(k) + ' = ' + 'forms.ModelChoiceField(queryset= Class.objects.filter(period='+str(k)+'), required=False)'
		print 'p_'+str(k) + ' = ' + 'forms.IntegerField(widget=forms.HiddenInput, initial='+str(k)+', required=False)'
		print 'teacher_'+str(k) + ' = ' +  'forms.CharField(max_length=20, required=False)'
		print 'dif_'+str(k) + ' = ' +  'forms.ChoiceField(required=False, choices=Class.DIF_CHOICES)'
		print 'subject_'+str(k) + ' = ' + 'forms.CharField(max_length=30, required=False)'  
		
		def clean(self):
			new_classes = []
			old_classes = []
			for k in xrange(1,8):
				if not getattr(self, 'class_'+str(k), False):
					new_classes.append(k)
				else:
					old_classes.append(k)
			self.cleaned_data['new_classes'] = new_classes
			self.cleaned_data['old_classes'] = old_classes
			return self.cleaned_data
			
		setattr(cls, 'clean', clean)
	return cls'''
	
class ScheduleForm(forms.Form):
	class_1 = forms.ModelChoiceField(queryset= Class.objects.filter(period=1).order_by('teacher'), required=False)
	p_1 = forms.IntegerField(widget=forms.HiddenInput, initial=1, required=False)
	teacher_1 = forms.CharField(max_length=20, required=False)
	dif_1 = forms.ChoiceField(required=False, choices=Class.DIF_CHOICES)
	subject_1 = forms.CharField(max_length=30, required=False)
	class_2 = forms.ModelChoiceField(queryset= Class.objects.filter(period=2).order_by('teacher'), required=False)
	p_2 = forms.IntegerField(widget=forms.HiddenInput, initial=2, required=False)
	teacher_2 = forms.CharField(max_length=20, required=False)
	dif_2 = forms.ChoiceField(required=False, choices=Class.DIF_CHOICES)
	subject_2 = forms.CharField(max_length=30, required=False)
	class_3 = forms.ModelChoiceField(queryset= Class.objects.filter(period=3).order_by('teacher'), required=False)
	p_3 = forms.IntegerField(widget=forms.HiddenInput, initial=3, required=False)
	teacher_3 = forms.CharField(max_length=20, required=False)
	dif_3 = forms.ChoiceField(required=False, choices=Class.DIF_CHOICES)
	subject_3 = forms.CharField(max_length=30, required=False)
	class_4 = forms.ModelChoiceField(queryset= Class.objects.filter(period=4).order_by('teacher'), required=False)
	p_4 = forms.IntegerField(widget=forms.HiddenInput, initial=4, required=False)
	teacher_4 = forms.CharField(max_length=20, required=False)
	dif_4 = forms.ChoiceField(required=False, choices=Class.DIF_CHOICES)
	subject_4 = forms.CharField(max_length=30, required=False)
	class_5 = forms.ModelChoiceField(queryset= Class.objects.filter(period=5).order_by('teacher'), required=False)
	p_5 = forms.IntegerField(widget=forms.HiddenInput, initial=5, required=False)
	teacher_5 = forms.CharField(max_length=20, required=False)
	dif_5 = forms.ChoiceField(required=False, choices=Class.DIF_CHOICES)
	subject_5 = forms.CharField(max_length=30, required=False)
	class_6 = forms.ModelChoiceField(queryset= Class.objects.filter(period=6).order_by('teacher'), required=False)
	p_6 = forms.IntegerField(widget=forms.HiddenInput, initial=6, required=False)
	teacher_6 = forms.CharField(max_length=20, required=False)
	dif_6 = forms.ChoiceField(required=False, choices=Class.DIF_CHOICES)
	subject_6 = forms.CharField(max_length=30, required=False)
	class_7 = forms.ModelChoiceField(queryset= Class.objects.filter(period=7).order_by('teacher'), required=False)
	p_7 = forms.IntegerField(widget=forms.HiddenInput, initial=7, required=False)
	teacher_7 = forms.CharField(max_length=20, required=False)
	dif_7 = forms.ChoiceField(required=False, choices=Class.DIF_CHOICES)
	subject_7 = forms.CharField(max_length=30, required=False)
	
	def clean(self):
		new_classes = []
		old_classes = []
		cd = self.cleaned_data
		for k in xrange(1,8):
			if not cd.get('class_'+str(k), False):
				if cd.get('teacher_'+str(k)) and cd.get('subject_'+str(k)):
					new_classes.append(k)
			else:
				old_classes.append(k)
		self.cleaned_data['new_classes'] = new_classes
		self.cleaned_data['old_classes'] = old_classes
		return self.cleaned_data

	
