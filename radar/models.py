from django.db import models
from django.contrib.auth.models import User


class Tech(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()

    def __unicode__(self):
        return unicode(self.name)


class TechPerson(models.Model):
    COMPETENCY_LEVELS = [(0, 'Ignoramus'),
                         (100, 'Aware'),
                         (200, 'Noob'),
                         (200, 'Working knowledge'),
                         (300, 'Competent'),
                         (400, 'Capable'),
                         (500, 'Experienced'),
                         (1000, 'Expert'),
                         (2000, 'Guru'),
                         (1000000, 'Omniscient'),
    ]
    tech = models.ForeignKey(Tech)
    person = models.ForeignKey(User)
    competence = models.IntegerField(choices=COMPETENCY_LEVELS, default=0)
    rating = models.IntegerField()  # 0 - Want it erased from history, 100 - want it's children
    notes = models.TextField(blank=True)

    def __unicode__(self):
        return "%s: %s at %s" % (unicode(self.person), unicode(self.get_competence_display()), unicode(self.tech))