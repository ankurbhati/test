from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


class UserActivation(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.OneToOneField(User, db_column='user_id')
    activation_key = models.CharField(max_length=30)
    role_id = models.ForeignKey(Group, db_column='role_id')
    created = models.DateTimeField(auto_now=False)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.user_id.email

    class Meta:
        db_table = 'user_activation'


class Country(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=False)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'country'


class State(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    country_id = models.ForeignKey(Country, db_column='country')
    created = models.DateTimeField(auto_now=False)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'state'


class City(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    state_id = models.ForeignKey(State, db_column='state_id')
    country_id = models.ForeignKey(Country, db_column='county_id')
    created = models.DateTimeField(auto_now=False)
    updated = models.DateTimeField(auto_now=False)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'city'


class UserDetail(models.Model):
    gender_choices = ((1, 'Male'),
                      (2, 'Female'))
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, db_column='user_id')
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city_id = models.ForeignKey(City, db_column='city_id')
    state_id = models.ForeignKey(State, db_column='state_id')
    country_id = models.ForeignKey(Country, db_column='country_id')
    pin_code = models.CharField(max_length=10)
    telephone = models.CharField(max_length=15)
    gender = models.IntegerField(max_length=1, choices=gender_choices)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    def __unicode__(self):
        return self.first_name

    class Meta:
        db_table = 'user_detail'


class Rent(models.Model):
    status_choices = ((0, 'Inactive'),
                      (1, 'Active'))
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=200)
    status = models.IntegerField(max_length=1, choices=status_choices)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        db_table = 'rent'


class CustomerRequest(models.Model):
    status_choices = ((0, 'Inactive'),
                      (1, 'Active'))
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, db_column='user_id')
    title = models.CharField(max_length=200)
    description = models.TextField()
    min_budget = models.IntegerField()
    max_budget = models.IntegerField()
    status = models.IntegerField(max_length=1, choices=status_choices)
    rent_id = models.ForeignKey(Rent, db_column='rent_id')
    city_id = models.ForeignKey(City, db_column='city_id')
    state_id = models.ForeignKey(State, db_column='state_id')
    country_id = models.ForeignKey(Country, db_column='country_id')
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        db_table = 'customer_request'


class SupplierOffer(models.Model):
    status_choices = ((0, 'Inactive'), (1, 'Active'))
    id = models.AutoField()
    user_id = models.ForeignKey(User, db_column='user_id')
    title = models.CharField(max_length=200)
    description = models.TextField()
    min_budget = models.IntegerField()
    max_budget = models.IntegerField()
    status = models.IntegerField(max_length=1, choices=status_choices)
    rent_id = models.ForeignKey(Rent, db_column='rent_id')
    city_id = models.ForeignKey(City, db_coulmn='city_id')
    state_id = models.ForeignKey(State, db_column='state_id')
    country_id = models.ForeignKey(Country, db_column='country_id')
    num_of_visiters = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        db_table = 'supplier_offer'


class ProductDetails(models.Model):
    status_choices = ((0, 'Inactive'), (1, 'Activate'))
    slider_choices = ((0, 'Inactive'), (1, 'Activate'))
    id = models.AutoField(primary_key=True)
    supplier_id = models.ForeignKey(User, db_column='supplier_id')
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    pincode = models.IntegerField()
    min_budget = models.IntegerField()
    max_budget = models.IntegerField()
    status = models.IntegerField(max_length=1, choices=status_choices)
    latitude = models.DecimalField(max_length=20, decimal_places=10)
    longitude = models.DecimalField(max_length=20, decimal_places=10)
    description = models.TextField()
    num_of_visiters = models.IntegerField()
    city_id = models.ForeignKey(City, db_column='city_id')
    state_id = models.ForeignKey(State, db_column='state_id')
    country_id = models.ForeignKey(Country, db_column='country_id')
    slider = models.IntegerField(max_length=1, choices=slider_choices)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        db_table = 'product_details'


class ProductTelephones(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(ProductDetails, db_column='product_id')
    telephone = models.CharField(max_length=12)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        db_table='product_telephones'


class ProductImages(models.Model):
    id, product_id, images_name, image_oldname, status,     order_byproduct, created, updated
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(ProductDetails, db_column='product_id')
    image_name = models.CharField(max_length=200)
    image_old_name = models.CharField(max_length=200)

