from django.contrib import admin
from .models import Sport, Choice

# Register your models here.

# Create a bunch of choice when you create a Question object

admin.site.site_header = "Sports Predictor ⚽🏀🏈"


class MyAdminSite(admin.AdminSite):
    site_header = "Sports Predictor ⚽🏀🏈"


# Attach CSS to ALL admin pages
class AdminCss(admin.ModelAdmin):
    class Media:
        css = {"all": ("admin/admin_override.css",)}


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


# Make the poll app modifiable in the admin
class SportAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["sport_text"]}),
        ("Date information", {
            "fields": ["pub_date"],
            "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]

    list_display = ["sport_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["sport_text"]


admin.site.register(Sport, SportAdmin)
admin.site.register(Choice)
