from django.db import models
from django.utils.text import slugify

class Reporter(models.Model):
    name = models.CharField(max_length=100)
    outlet = models.CharField(max_length=50, null=True, blank=True)
    statecode = models.CharField(max_length=2)
    email = models.EmailField(max_length=254, null=True, blank=True)
    def __str__(self):
        return self.name

class ModelSuggestion(models.Model):
    model_name = models.CharField(max_length=200)
    source_link = models.URLField(max_length=200)
    model_source = models.CharField(max_length=200)
    model_text = models.TextField()
    your_name = models.CharField(max_length=200)
    your_email = models.EmailField(max_length=100)

#This is a model containing details on the model, as pulled from
#https://statehouses-api.gannettdigital.com/api/v1.0/GetTableRecords?output_format=csv&table_name=lid.model_text
class ModelText(models.Model):
    keywords = models.CharField(max_length=500, null=True, blank=True)
    model_source = models.CharField(max_length=500, null=True, blank=True)
    model_text = models.TextField(null=True, blank=True)
    model_name = models.CharField(max_length=500, null=True, blank=True)
    model_id = models.IntegerField()
    source_link = models.URLField(max_length=500, null=True, blank=True)

class Match(models.Model):
    enabled = models.IntegerField()
    simtype = models.IntegerField()
    actualleg = models.CharField(max_length=3, null=True, blank=True)
    modelid = models.IntegerField()
    simid = models.IntegerField()
    view = models.TextField(null=True, blank=True)
    maxwordscore = models.IntegerField()
    fiveplusscore = models.IntegerField()
    tenplusscore = models.IntegerField()
    lidscore = models.IntegerField()
    maxwords = models.IntegerField()
    fiveplus = models.IntegerField()
    tenplus = models.IntegerField()
    fifteenplus = models.IntegerField()
    exactmatch = models.IntegerField()
    modelwords = models.CharField(max_length=20, null=True, blank=True)
    number = models.CharField(max_length=20, null=True, blank=True)
    modeltext = models.TextField(null=True, blank=True)
    modelname = models.TextField(null=True, blank=True)
    modeltype = models.TextField(null=True, blank=True)
    modelcat = models.TextField(null=True, blank=True)
    modelsubject = models.TextField(null=True, blank=True)
    modeldesc = models.TextField(null=True, blank=True)
    year1 = models.CharField(max_length=4, null=True, blank=True)
#    year2 = models.CharField(max_length=4, null=True, blank=True)
    state = models.TextField(null=True, blank=True)
    billno = models.SlugField(max_length=100, null=True, blank=True)
    party = models.CharField(max_length=100, null=True, blank=True)
    statusdate = models.CharField(max_length=75, null=True, blank=True)
    status = models.CharField(max_length=75, null=True, blank=True)
#    statusdate2 = models.CharField(max_length=15, null=True, blank=True)
    noideawhathisis = models.CharField(max_length=100, null=True, blank=True)
    primarysponsors = models.TextField(null=True, blank=True)
    cosponsors = models.TextField(null=True, blank=True)
    othersponsors = models.TextField(null=True, blank=True)
    billtext = models.TextField(null=True, blank=True)
    billtitle = models.TextField(null=True, blank=True)
    billid = models.TextField(null=True, blank=True)
    textid = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(null=True, blank=True)

#    def save(self, *args, **kwargs):
#        self.slug = slugify(self.hospital)
#        super().save(*args, **kwargs)

#    def get_absolute_url(self):
#        return "/deadly-deliveries/%s/" % self.slug
