from django.urls import path, include
from . import views
from django.contrib import admin


# CHANGING DJANGO HEADER WITHOUT OVERRIDING TEMPLATES
admin.site.site_header = "Sports Predictor ⚽️🏀🏈"
admin.site.site_title = "SportsPredictor"
admin.site.index_title = "Welcome to SP Predictions 🎲"

app_name = "polls"

urlpatterns = [
    # /polls/
    path("", views.IndexView.as_view(), name="index"),
    # /admin/
    path("admin/", admin.site.urls),

    # /polls/{question id}/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # /polls/{question id}/results/
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    # /polls/{question id}/vote/
    path("<int:sport_id>/vote/", views.vote, name="vote"),
    # EXTRA DJANGO REST FRAMEWORK
    path('api-auth/', include('rest_framework.urls')),

]
