from django.db import models

class QueryResult(models.Model):
    submitted_text = models.TextField()
    search_city    = models.CharField(max_length=3,blank=True)
    results        = models.TextField()
    http_post_data = models.TextField()
    metadata       = models.TextField()
    date_created   = models.DateTimeField(auto_now_add=True)

    
    

