from django import template
from django.db.models import Avg
from library.models import Review

register = template.Library()

@register.filter
def average_rating(book):
    return book.reviews.aggregate(Avg('rating'))['rating__avg'] or 0
