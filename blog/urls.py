from . import views
from django.urls import path

app_name = "blog"
urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>', views.detail, name='detail'),
    path('category/<int:category_id>', views.category, name='category'),
    path('tag/<int:tag_id>', views.tag, name='tag'),
    path('top', views.top, name='top'),
    path('page/<int:current_page>', views.page, name='page'),
    path('category_page/<int:category_id>/<int:current_page>', views.category_page, name='category_page'),
    path('tag_page/<int:tag_id>/<int:current_page>', views.tag_page, name='tag_page'),
    path('top_page/<int:current_page>', views.top_page, name='top_page'),
]
