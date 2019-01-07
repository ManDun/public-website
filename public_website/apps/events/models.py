from django.utils.timezone import now
from django.db import models

from django.db import models

from member.models import Person
# Create your models here.


class Events(models.Model):
	name = models.CharField(max_length=200, blank=True, default='Unnamed Event')
	day = models.DateTimeField(default=now, blank=True )
	description = models.CharField(max_length=1500, blank=True, null=True)

	attendees = models.ManyToManyField(Person, related_name='attendees', default='None', blank=True)
	organisor = models.ForeignKey(Person, on_delete=models.CASCADE, related_name = 'organisor', null=True)
	address = models.CharField(max_length=250, blank=False, default='', null=True)
#	position = GeopositionField()

	class Meta:
		verbose_name_plural = 'events'

	def __str__(self):
		return '{}'.format(self.name)