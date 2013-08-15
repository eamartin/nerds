from django.contrib.auth.models import User
from django.db import models

class Class(models.Model):
	DIF_CHOICES = (
		('L', 'Level'),
		('H', 'Honors'),
		('P', 'Pre-AP'),
		('A', 'AP'),
		('D', 'Dual Credit'),
		('N', 'Not Applicable'),
	)
	
	PERIOD_CHOICES = (
		(1, '1st'),
		(2, '2nd'),
		(3, '3rd'),
		(4, '4th'),
		(5, '5th'),
		(6, '6th'),
		(7, '7th')
	)
		
	dif = models.CharField(max_length=1, choices=DIF_CHOICES, blank=True)
	teacher = models.CharField(max_length=20)
	subject = models.CharField(max_length=30)
	period = models.PositiveSmallIntegerField(choices=PERIOD_CHOICES)
	students = models.ManyToManyField(User, related_name='classes')

	class Meta(object):
		ordering = ('period',)
		unique_together = ('teacher', 'subject', 'period')
		
	def __unicode__(self):
		if self.dif != 'N':
			return self.teacher + ' - ' + self.get_dif_display() + ' ' + self.subject
		return self.teacher + ' - ' + self.subject
		
class MyUser(User):
	class Meta(object):
		proxy = True
		ordering = ['first_name', 'last_name']
		
	def __unicode__(self):
		return self.get_full_name()
