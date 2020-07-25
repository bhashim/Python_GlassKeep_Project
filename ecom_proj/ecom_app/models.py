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
        if "subject" not in post_data:
            errors["field_missing"] = "Subject does not exist."
        elif len(post_data["subject"]) == 0:
            errors["subject"] = "Include a subject."
        elif len(post_data["subject"]) < 2:
            errors["subject"] = "Subject must be more than 2 characters."
        if "purchase_message" not in post_data:
            errors["field_missing"] = "Message does not exist."
        elif len(post_data["purchase_message"]) == 0:
            errors["purchase_message"] = "Include a message."
        elif len(post_data["purchase_message"]) < 3:
            errors["purchase_message"] = "Message must be more than 3 characters."
        if "quantity" not in post_data:
            errors["field_missing"] = "Quantity does not exist."
        elif len(post_data["quantity"]) == 0 or int(post_data["quantity"]) < 1:
            errors["quantity"] = "Quantity must be greater than 0."
        if "shipping_address" not in post_data:
            errors["field_missing"] = "Shipping Address does not exist."
        elif len(post_data["shipping_address"]) == 0:
            errors["shipping_address"] = "Include a shipping address."
        elif len(post_data["shipping_address"]) < 3:
            errors["shipping_address"] = "Shipping Address must be at least 3 characters."
        if "city" not in post_data:
            errors["field_missing"] = "City does not exist."
        elif len(post_data["city"]) == 0:
            errors["city"] = "Include a city."
        elif len(post_data["city"]) < 2:
            errors["city"] = "City must be more than 2 characters."
        if "state" not in post_data:
            errors["field_missing"] = "State does not exist."
        elif len(post_data["state"]) == 0:
            errors["state"] = "Include a state."
        if "zip_code" not in post_data:
            errors["field_missing"] = "Zip Code does not exist."
        elif len(post_data["zip_code"]) == 0:
            errors["zip_code"] = "Include a zip code."
        elif len(post_data["zip_code"]) < 3:
            errors["zip_code"] = "Zip Code must be more than 3 characters." 
        if len(post_data["credit_card_number"]) == 0:
            errors["credit_card_number"] = "Include a credit card number."
        elif len(post_data["credit_card_number"]) < 4:
            errors["credit_card_number"] = "Credit card number must be more than 4 numbers."
        if len(post_data["security_code"]) == 0:
            errors["security_code"] = "Include a security code."
        elif len(post_data["security_code"]) < 3:
            errors["security_code"] = "Security must be 3 characters."
        if len(post_data["card_type"]) == 0:
            errors["card_type"] = "Include the card used."
        elif len(post_data["card_type"]) < 4:
            errors["card_type"] = "Card used must be longer than 4 characters."
            
        return errors


class Purchase(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=60)
    message = models.TextField(max_length=100)
    quantity = models.IntegerField(default=1)
    shipping_address = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=60)
    credit_card_number = models.CharField(max_length=100)
    security_code = models.CharField(max_length=3)
    card_type = models.CharField(max_length=60)
    expiration_date = models.CharField(max_length=8)
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
