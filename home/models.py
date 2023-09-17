from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    author = models.CharField(max_length=250, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    author_image = models.ImageField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Multimedia(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    content = models.CharField(max_length=250, null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


galerie_choice = {
    ('RENCONTRES', 'RENCONTRES'),
    ('EVENEMENTS', 'EVENEMENTS'),
    ('REALISATIONS', 'REALISATIONS'),
    ('PROJETS', 'PROJETS')
}

class Galerie(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    categorie = models.CharField(max_length=250, blank=True, null=True, choices=galerie_choice)
    image = models.ImageField(null=True, blank=True)
    content = models.FileField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Evenement(models.Model):
    entete = models.CharField(max_length=250, null=True, blank=True)
    title = models.CharField(max_length=250, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    localisation = models.CharField(max_length=250,null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Solutions(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    author_image = models.ImageField(null=True, blank=True)
    author = models.CharField(max_length=250,null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    content = models.FileField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class AboutGalerie(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Slides(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

