from django.conf.urls.defaults import *

urlpatterns = patterns('',
	url(r'^$', 'matches.views.home', name='home'),
	url(r'^register/$', 'matches.views.reg', name='classic_reg'),
	url(r'^edit_schedule/$', 'matches.views.edit_schedule', name='edit_sched'),
	url(r'^schedule/(?P<user_id>\d{,5})', 'matches.views.view_sched', name='view_sched'),
	url(r'^login/$', 'matches.views.login_view', name='login'),
	url(r'^logout/$', 'matches.views.logout_view', name='logout'),
	url(r'^overview/$', 'matches.views.overview', name='overview'),
)
