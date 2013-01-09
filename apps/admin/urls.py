from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'apps.admin.views.index'),
    url(r'^ad/$', 'apps.admin.views.ad'),
    url(r'^login/$', 'apps.admin.views.login_action'),
    url(r'^logout/$', 'apps.admin.views.logout_action'),
    url(r'^login_check/$', 'apps.admin.views.login_check'),

    url(r'^blog/category/getall/', 'apps.admin.views.blog_category_getall'),
    url(r'^blog/category/save/', 'apps.admin.views.blog_category_save'),
    url(r'^blog/category/edit/(?P<id>[-\w]+)/', 'apps.admin.views.blog_category_edit'),
    url(r'^blog/category/', 'apps.admin.views.blog_category'),

    url(r'^blog/tag/getall/', 'apps.admin.views.blog_tag_getall'),
    url(r'^blog/tag/save/', 'apps.admin.views.blog_tag_save'),
    url(r'^blog/tag/edit/(?P<id>[-\w]+)/', 'apps.admin.views.blog_tag_edit'),
    url(r'^blog/tag/moveup/(?P<id>[-\w]+)/', 'apps.admin.views.blog_tag_moveup'),
    url(r'^blog/tag/movedown/(?P<id>[-\w]+)/', 'apps.admin.views.blog_tag_movedown'),
    url(r'^blog/tag/', 'apps.admin.views.blog_tag'),

    #url(r'^blog/post/getall/', 'apps.admin.views.blog_post_getall'),
    #url(r'^blog/post/save/', 'apps.admin.views.blog_post_save'),
    url(r'^blog/post/edit/(?P<id>[-\w]+)/', 'apps.admin.views.blog_post_edit'),
    #url(r'^blog/post/', 'apps.admin.views.blog_post'),

)


