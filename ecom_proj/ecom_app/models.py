from django.db import models


class PurchaseManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        print("Post data inside validator: ", post_data)
        if "purchase_name" not in post_data:
            errors["field_missing"] = "Name does not exist."
        elif len(post_data["purchase_name"]) == 0:
            errors["purchase_name"] = "Include a name."
        elif len(post_data["purchase_name"]) < 3:
            errors["purchase_name"] = "Name must be at least 3 characters."
        if "email" not in post_data:
            errors["field_missing"] = "Email does not exist."
        elif len(post_data["email"]) == 0:
            errors["email"] = "Include an email."
        elif len(post_data["email"]) < 3:
            errors["email"] = "Email must be at least 3 characters."
        if "shipping_address" not in post_data:
            errors["field_missing"] = "Shipping Address does not exist."
        elif len(post_data["shipping_address"]) == 0:
            errors["shipping_address"] = "Include a shipping address."
        elif len(post_data["shipping_address"]) < 3:
            errors["shipping_address"] = "Shipping Address must be at least 3 characters."
        if "quantity" not in post_data:
            errors["field_missing"] = "Quantity does not exist."
        elif len(post_data["quantity"]) == 0 or int(post_data["quantity"]) < 1:
            errors["quantity"] = "Quantity must be greater than 0."

        return errors


class Purchase(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=100)
    shipping_address = models.CharField(max_length=60)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id_creator = models.IntegerField(default=-1)

    objects = PurchaseManager()


class User(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Create your models here.
