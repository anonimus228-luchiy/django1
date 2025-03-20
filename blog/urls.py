from django.contrib import admin
from django.urls import path
from posts.views import (test_view,
                         post_list_view,
                         post_create_view,
                         post_detail_view,
                         home_page_view)
from users.views import (
    register_view,
    login_view,
    logout_view
)
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', test_view),
    path('', home_page_view),
    path('posts/', post_list_view),
    path('posts/create/', post_create_view),
    path('posts/<int:post_id>/', post_detail_view),
    path('register/', register_view),
    path('login/', login_view,name="login"),
    path('logout/', logout_view,name="logout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
