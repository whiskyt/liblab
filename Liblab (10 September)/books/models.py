from django.db import models

# Create your models here.


class Books(models.Model):

    in_library = True
    out_library = False

    book_status = (

            (in_library,'IN'),
            (out_library,'OUT'),
    )

    name        =models.CharField(max_length=250)
    author      =models.CharField(max_length=250)
    genre       =models.CharField(max_length=250)
    summary     =models.TextField()
    category    =models.CharField(null=True, max_length=250)
    thumbnail   =models.CharField(max_length=250, default='Thumbnail')
    time        =models.DateTimeField(auto_now=True)
    in_lib      =models.BooleanField(default=True,choices=book_status)

    def __str__(self):
        return self.name