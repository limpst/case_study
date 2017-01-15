from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

from django.core.urlresolvers import reverse

# Create your models here.
class Deal(models.Model):
    name = models.CharField(max_length=200)
    currency = models.CharField(max_length=15)
    fund = models.CharField(max_length=200) 
    
    def __unicode__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('deal_edit', kwargs={'pk':self.pk})
        
        
class Cashflows(models.Model):
    CF_CHOICES = ( 
        (u'Equity','Equity'), 
        (u'Proceeds', 'Proceeds'), 
        ) 
            
    did = models.ForeignKey('Deal', verbose_name="Deal_Name")
    valuedate = models.DateField("Value_Date") 
    cftype = models.CharField("CF_Type", max_length=200, choices = CF_CHOICES) 
    cashflows = models.IntegerField()
