from django.conf.urls import url, include
from . import views as hubviews



urlpatterns = [
	url(r'^$', hubviews.homepage, name='homepage'),
	url(r'^our_organization$/', hubviews.our_organization, name='our_organization'),
	url(r'^why_orphan_education/$', hubviews.why_orphan_education, name='why_orphan_education'),
	url(r'^get_involved/$', hubviews.get_involved, name='get_involved'),
	url(r'^our_impact/$', hubviews.our_impact, name='our_impact'),
	url(r'^sign_in/$', hubviews.sign_in, name='sign_in'),
	url(r'^sign_out/$', hubviews.sign_out, name='sign_out'),


]
