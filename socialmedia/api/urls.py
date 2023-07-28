from rest_framework.routers import DefaultRouter
from users.views import UserViewSet
from user_profile.views import ProfileViewSet
from posts.views import PostViewSet
from comments.views import CommentViewSet
from likes.views import LikeViewSet
from searchs.views import SearchViewSet

router=DefaultRouter()

router.register(r'user',UserViewSet,basename='user')
router.register(r'profiles',ProfileViewSet,basename='profiles')
router.register(r'posts',PostViewSet, basename='posts')
router.register(r'comments',CommentViewSet, basename='comments')
router.register(r'likes',LikeViewSet,basename='likes')
router.register(r'search_user',SearchViewSet,basename='searchs')

urlpatterns=router.urls
