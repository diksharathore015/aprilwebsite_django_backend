import django_filters
from .models import Course

class CourseFilter(django_filters.FilterSet):
    slug = django_filters.CharFilter(lookup_expr='exact')  # or 'icontains' for partial match

    class Meta:
        model = Course
        fields = ['slug']
