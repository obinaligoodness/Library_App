from django.urls import path, include
from rest_framework_nested import routers

from . import views

#
# urlpatterns = [
#     # path('welcome/', views.welcome),
#     path('book/', views.book_list),
#     path('book/<int:pk>', views.book_detail),
#     path('author', views.author_list),
#     path('author<int:pk>', views.author_list, name="author-detail"),
# ]

router = routers.DefaultRouter()
router.register('books', views.BookViewSet)
router.register('authors', views.AuthorViewSet)
router.register('reviews', views.ReviewViewSet)

urlpatterns = router.urls
books_router = routers.NestedDefaultRouter(router, 'books', lookup='book')
router.register('reviews',views.ReviewViewSet,basename='book-reviews')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(books_router.urls)),
    path('bookinstance/', views.BookInstanceAPIView.as_view()),
]
