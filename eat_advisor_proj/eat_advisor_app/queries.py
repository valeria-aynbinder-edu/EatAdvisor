from eat_advisor_proj.eat_advisor_app.models import Review
from django.db.models import Avg, Max, Min, Count, Q

# from django.db.models import Count
# result = (Members.objects
#           .values('designation')
#           .annotate(dcount=Count('designation'))
#           .order_by()
#           )
#
# # Rating.objects.filter(attribute__in=attributes) \
# #     .values('location') \
# #     .annotate(score = Sum('score')) \
# #     .order_by('-score')
#
# Review.objects.values('restaurant').annotate(avg_stars=Avg('stars'), reviews_cnt=Count('id'))
#
# # OR query
# Review.objects.filter(Q(stars__gte=3) | Q(name__contains='bla'))