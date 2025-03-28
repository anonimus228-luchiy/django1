from django.contrib import admin
from django.urls import path
from posts.views import (
    test_view,
    post_list_view,
    post_create_view,
    post_detail_view,
    home_page_view,
    post_update_view,
    TestView,
    PostListView2,
    PostCreateView2
)
from users.views import (
    register_view,
    login_view,
    logout_view,
    profile_view


)
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('posts/create2/', PostCreateView2.as_view()),
    path('test2/', TestView.as_view()),
    path('posts2/', PostListView2.as_view()),
    path('admin/', admin.site.urls),
    path('test/', test_view),
    path('', home_page_view),
    path('posts/', post_list_view),
    path('posts/create/', post_create_view),
    path('posts/<int:post_id>/', post_detail_view),
    path('register/', register_view),
    path('login/', login_view,name="login"),
    path('logout/', logout_view,name="logout"),
    path('posts/<int:post_id>/update/', post_update_view),
    path('profile/', profile_view),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
