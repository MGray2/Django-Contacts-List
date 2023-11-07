from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=15)
    is_favorite = models.BooleanField()

    def create_contact(self, name, email, phone, is_favorite):
        self.name = name
        self.email = email
        self.phone = phone
        self.is_favorite = is_favorite

    def all_contacts(Contact):
        for person in Contact:
            print(
                f"{number}. {person.name}, {person.email}, {person.phone}, {person.is_favorite}"
            )

    def find_contact_by_name(name):
        for person in Contact:
            if person.name == name:
                print(
                    f"{number}. {person.name}, {person.email}, {person.phone}, {person.is_favorite}"
                )

    def favorite_contacts(Contact):
        for person in Contact:
            if person.is_favorite == True:
                print(
                    f"{number}. {person.name}, {person.email}, {person.phone}, {person.is_favorite}"
                )

    def update_contact_email(name, new_email):
        for person in Contact:
            if person.name == name:
                person.email = new_email

    def delete_contact(name):
        to_remove = Contact.objects.get(name=name)
        to_remove.delete()
