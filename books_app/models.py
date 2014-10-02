
from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50)
    website = models.URLField(blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['country', 'city', 'name']


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    # email = models.EmailField(blank=True, verbose_name='e-mail')
    email = models.EmailField('e-mail', blank=True)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    class Meta:
        ordering = ['first_name', 'last_name']


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, blank=True)
    publication_date = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return u'%s by %s (%s, %s)' % (self.title, u", ".join([unicode(a) for a in self.authors.all()]),
                                        #u", ".join([u"%s %s" % (a.first_name, a.last_name) for a in self.authors.all()]))
                                        self.publisher.name, self.publication_date)


    class Meta:
        ordering = ['title']
