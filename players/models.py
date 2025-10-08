from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg

class Player(models.Model):
    """Brighton player with stats"""
    POSITIONS = [
        ('GK', 'Goalkeeper'),
        ('DEF', 'Defender'),
        ('MID', 'Midfielder'),
        ('FWD', 'Forward'),
    ]
    
    # Basic Info
    api_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=200)
    photo_url = models.URLField(blank=True)
    position = models.CharField(max_length=3, choices=POSITIONS)
    nationality = models.CharField(max_length=100)
    age = models.IntegerField()
    height = models.CharField(max_length=20, blank=True)
    weight = models.CharField(max_length=20, blank=True)
    
    # Season Stats
    appearances = models.IntegerField(default=0)
    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    minutes_played = models.IntegerField(default=0)
    official_avg_rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    
    # Meta
    is_active = models.BooleanField(default=True)
    last_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name} ({self.position})"
    
    def get_fan_rating(self):
        """Calculate average fan rating"""
        avg = self.userreview_set.aggregate(Avg('overall_rating'))['overall_rating__avg']
        return round(avg, 1) if avg else None
    
    def get_recent_form(self):
        """Get average rating from last 5 matches"""
        recent = self.matchperformance_set.order_by('-match_date')[:5]
        if recent:
            avg = sum(m.rating for m in recent) / len(recent)
            return round(avg, 2)
        return None
    
    