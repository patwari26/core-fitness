from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import Person

class LatestEntriesFeed(Feed):
    title = "Eat Healthy Live Healthy"
    link = "feed/"
    description = "recent users"

    def items(self):
        return Person.objects.order_by('user')[:5]

    def item_height(self, item):
        return item.height

    def item_weight(self, item):
        return item.weight

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse('feedlink')