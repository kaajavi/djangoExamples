# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.core.mail import send_mail

#notify = False

class Post(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    CATEGORIAS = (
        ("0", 'Linux'),
        ("1", 'dJango'),        
        ("2", 'Tutos'),
    )
    categorias = models.CharField(max_length=6,
                                      choices=CATEGORIAS,
                                      default="0")
    
    def __unicode__(self):
        return self.title





### Admin

class PostAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    display_fields = ["title", "created","categorias"]
    
#NO IMPLEMENTADO    
'''class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=60)
    body = models.TextField()
    post = models.ForeignKey(Post)

    def __unicode__(self):
        return unicode("%s: %s" % (self.post, self.body[:60]))

    
    
    
    #ESTO ES PARA ENVIAR UN MAIL CADA VEZ QUE ALQUIEN COMENTA
    #TODO: NO ESTÁ IMPLEMENTADO
    def save(self, *args, **kwargs):
        """Email when a comment is added."""
        if "notify" in kwargs and kwargs["notify"] == True:
            message = "Se realizo un comentario en el post '%s', por el usuario '%s': \n\n%s" % (self.post, self.author,
                                                                         self.body)
            from_addr = "no-reply@mydomain.com"
            recipient_list = ["myemail@mydomain.com"]
            send_mail("New comment added", message, from_addr, recipient_list)

        if "notify" in kwargs: del kwargs["notify"]
        super(Comment, self).save(*args, **kwargs)

class CommentAdmin(admin.ModelAdmin):
    display_fields = ["post", "author", "created"]
    '''