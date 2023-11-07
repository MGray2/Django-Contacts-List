from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=15)
    is_favorite = models.BooleanField()

    def create_contact(name, email, phone, is_favorite):
        new_contact = Contact(name, email, phone, is_favorite)
        new_contact.save()

    def all_contacts(Contact):
        Contact.objects.all()

    def find_contact_by_name(name):
        Contact.objects.filter(name=name)

    def favorite_contacts(Contact):
        Contact.objects.filter(is_favorite=True)

    def update_contact_email(name, new_email):
        for person in Contact:
            if person.name == name:
                person.email = new_email

    def delete_contact(name):
        to_remove = Contact.objects.get(name=name)
        to_remove.delete()
