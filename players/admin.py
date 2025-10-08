from django.contrib import admin
from .models import Player, MatchPerformance, UserReview, PlayerAISummary, UserProfile

# Register your models here.

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'nationality', 'appearances', 'goals', 'is_active']
    list_filter = ['position', 'is_active']
    search_fields = ['name']

@admin.register(UserReview)
class UserReviewAdmin(admin.ModelAdmin):
    list_display = ['player', 'user', 'overall_rating', 'created_at']
    list_filter = ['created_at']

@admin.register(MatchPerformance)
class MatchPerformanceAdmin(admin.ModelAdmin):
    list_display = ['player', 'opponent', 'match_date', 'rating', 'goals']
    list_filter = ['match_date']

admin.site.register(PlayerAISummary)
admin.site.register(UserProfile)