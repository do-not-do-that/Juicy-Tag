from django.db import models

# Create your models here.

class JuicyBoard(models.Model):
    no = models.AutoField(db_column='NO', primary_key=True)  # Field name made lowercase.
    pcode = models.CharField(db_column='PCODE', max_length=4)  # Field name made lowercase.
    user_id = models.CharField(db_column='USER_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    is_complete = models.IntegerField(db_column='IS_COMPLETE', blank=True, null=True)  # Field name made lowercase.
    priority = models.IntegerField(db_column='PRIORITY', blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateField(db_column='CREATED_AT', blank=True, null=True)  # Field name made lowercase.

    def juicy_save(self):
        self.save()
    
    class Meta:
        managed = False
        db_table = 'juicy_board'
        
        
class TagCode(models.Model):
    tcode = models.CharField(db_column='TCODE', primary_key=True, max_length=4)  # Field name made lowercase.
    tname = models.CharField(db_column='TNAME', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TAG_CODE'