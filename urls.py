from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views import generic

import mezzanine
from mezzanine.conf import settings

admin.autodiscover()

urlpatterns = [
    url(
        r'^contacts/',
        generic.TemplateView.as_view(template_name='contact_form.html')
    ),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^blog/', include('blog.urls')),
    url(r'^sample_1/', include('sample_1.urls')),
    url(r'^sample_2/', include('sample_2.urls')),
    url(r'^sample_3/', include('sample_3.urls')),
    url(r'^$', mezzanine.pages.views.page, {'slug': '/'}, name='home'),
    url('^', include('mezzanine.urls')),
]

if settings.TEMPLATE_DEBUG:
    urlpatterns += [
        url(
            r'^404.html$',
            generic.TemplateView.as_view(template_name='404.html')
        ),
        url(
            r'^500.html$',
            generic.TemplateView.as_view(template_name='500.html')
        ),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "mezzanine.core.views.page_not_found"
handler500 = "mezzanine.core.views.server_error"
