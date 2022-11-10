from django.urls import path
from . import views
from .views import Home, BlogDetail, AddPost, UpdatePost, DeletePost, AddCategory, CategoryView, CategoryList, LikesOnPost, AddComment

urlpatterns = [
    # path('', views.index, name="home"),
    path('', Home.as_view(), name="home"),
    path('article/<int:pk>', BlogDetail.as_view(), name="article"),
    path('add_blogs/', AddPost.as_view(), name="add_blogs"),
    path('add_category/', AddCategory.as_view(), name="add_category"),
    path('article/edit/<int:pk>', UpdatePost.as_view(), name="Edit-Blogs"),
    path('article/<int:pk>/remove', DeletePost.as_view(), name="delete"),
    path('category/<str:catg>/', CategoryView, name="category"),
    path('category-list/', CategoryList, name="category-list"),
    path('like/<int:pk>', LikesOnPost, name="like_post"),
    path('article/<int:pk>/comment/', AddComment.as_view(), name="add_comment"),


]
# video no. 25