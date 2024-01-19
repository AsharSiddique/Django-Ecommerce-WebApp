# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Administrators(models.Model):
    adminid = models.AutoField(db_column='AdminID', primary_key=True)  # Field name made lowercase.
    aname = models.CharField(db_column='AName', max_length=60, blank=True, null=True)  # Field name made lowercase.
    aemail = models.CharField(db_column='AEmail', unique=True, max_length=40, blank=True, null=True)  # Field name made lowercase.
    apassword = models.CharField(db_column='APassword', max_length=20, blank=True, null=True)  # Field name made lowercase.
    passcode = models.ForeignKey('Job', models.DO_NOTHING, db_column='PassCode', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'administrators'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cartcontainers(models.Model):
    cartid = models.OneToOneField('Shoppingcarts', on_delete=models.CASCADE, db_column='CartID', primary_key=True)  # Field name made lowercase. The composite primary key (CartID, ProdID) found, that is not supported. The first column is selected.
    prodid = models.ForeignKey('Products', on_delete=models.CASCADE, db_column='ProdID')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cartcontainers'
        unique_together = (('cartid', 'prodid'),)


class Contact(models.Model):
    custid = models.OneToOneField('Customers', models.DO_NOTHING, db_column='CustID', primary_key=True)  # Field name made lowercase. The composite primary key (CustID, ContactID) found, that is not supported. The first column is selected.
    contactid = models.IntegerField(db_column='ContactID')  # Field name made lowercase.
    contype = models.CharField(db_column='ConType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ccontactnumber = models.IntegerField(db_column='CContactNumber', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contact'
        unique_together = (('custid', 'contactid'),)


class Custcompany(models.Model):
    custid = models.OneToOneField('Customers', models.DO_NOTHING, db_column='CustID', primary_key=True)  # Field name made lowercase.
    ntn = models.IntegerField(db_column='NTN', blank=True, null=True)  # Field name made lowercase.
    creditlimit = models.DecimalField(db_column='CreditLimit', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'custcompany'


class Customers(models.Model):
    custid = models.AutoField(db_column='CustID', primary_key=True)  # Field name made lowercase.
    cname = models.CharField(db_column='CName', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cemail = models.CharField(db_column='CEmail', unique=True, max_length=40, blank=True, null=True)  # Field name made lowercase.
    cpassword = models.CharField(db_column='CPassword', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ccountry = models.CharField(db_column='CCountry', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ccity = models.CharField(db_column='CCity', max_length=20, blank=True, null=True)  # Field name made lowercase.
    caddress = models.CharField(db_column='CAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    last_login = models.DateTimeField(null=True, blank=True)
    

    class Meta:
        managed = True
        db_table = 'customers'


class Custperson(models.Model):
    custid = models.OneToOneField(Customers, models.DO_NOTHING, db_column='CustID', primary_key=True)  # Field name made lowercase.
    nic = models.IntegerField(db_column='NIC', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'custperson'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Electronics(models.Model):
    prodid = models.OneToOneField('Products', models.DO_NOTHING, db_column='ProdID', primary_key=True)  # Field name made lowercase.
    company = models.CharField(db_column='Company', max_length=60, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'electronics'


class Garments(models.Model):
    prodid = models.OneToOneField('Products', models.DO_NOTHING, db_column='ProdID', primary_key=True)  # Field name made lowercase.
    brand = models.CharField(db_column='Brand', max_length=60, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'garments'


class Groceries(models.Model):
    prodid = models.OneToOneField('Products', models.DO_NOTHING, db_column='ProdID', primary_key=True)  # Field name made lowercase.
    expirydate = models.DateField(db_column='ExpiryDate', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'groceries'


class Job(models.Model):
    passcode = models.AutoField(db_column='PassCode', primary_key=True)  # Field name made lowercase.
    jobtype = models.CharField(db_column='JobType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    salary = models.DecimalField(db_column='Salary', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'job'


class Management(models.Model):
    adminid = models.OneToOneField(Administrators, models.DO_NOTHING, db_column='AdminID', primary_key=True)  # Field name made lowercase.
    manager = models.IntegerField(db_column='Manager', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'management'


class Orders(models.Model):
    orderid = models.AutoField(db_column='OrderID', primary_key=True)  # Field name made lowercase.
    custid = models.ForeignKey(Customers, models.DO_NOTHING, db_column='CustID', blank=True, null=True)  # Field name made lowercase.
    prodid = models.ForeignKey('Products', models.DO_NOTHING, db_column='ProdID', blank=True, null=True)  # Field name made lowercase.
    orderquantity = models.IntegerField(db_column='OrderQuantity', blank=True, null=True)  # Field name made lowercase.
    orderdate = models.DateField(db_column='OrderDate', blank=True, null=True)  # Field name made lowercase.
    ordertime = models.TimeField(db_column='OrderTime', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orders'


class Products(models.Model):
    prodid = models.AutoField(db_column='ProdID', primary_key=True)  # Field name made lowercase.
    pname = models.CharField(db_column='PName', max_length=60, blank=True, null=True)  # Field name made lowercase.
    pprice = models.DecimalField(db_column='PPrice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pquantity = models.IntegerField(db_column='PQuantity', blank=True, null=True)  # Field name made lowercase.
    pspecs = models.TextField(db_column='PSpecs', blank=True, null=True)  # Field name made lowercase.
    pimage = models.ImageField(db_column='PImage', max_length=200, blank=True, null=True, upload_to='product_image')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    rating = models.DecimalField(blank=True, null=True, max_digits=2, decimal_places=1)
    persons_rated = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'products'


class Productstock(models.Model):
    adminid = models.OneToOneField(Administrators, models.DO_NOTHING, db_column='AdminID', primary_key=True)  # Field name made lowercase. The composite primary key (AdminID, ProdID, StockDate) found, that is not supported. The first column is selected.
    prodid = models.ForeignKey(Products, models.DO_NOTHING, db_column='ProdID')  # Field name made lowercase.
    stockdate = models.DateField(db_column='StockDate')  # Field name made lowercase.
    stocktime = models.TimeField(db_column='StockTime', blank=True, null=True)  # Field name made lowercase.
    stockquantity = models.IntegerField(db_column='StockQuantity', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productstock'
        unique_together = (('adminid', 'prodid', 'stockdate'),)


class Productsupply(models.Model):
    vendorid = models.OneToOneField('Vendors', models.DO_NOTHING, db_column='VendorID', primary_key=True)  # Field name made lowercase. The composite primary key (VendorID, ProdID, SupplyDate) found, that is not supported. The first column is selected.
    prodid = models.ForeignKey(Products, models.DO_NOTHING, db_column='ProdID')  # Field name made lowercase.
    supplydate = models.DateField(db_column='SupplyDate')  # Field name made lowercase.
    supplytime = models.TimeField(db_column='SupplyTime', blank=True, null=True)  # Field name made lowercase.
    supplyquantity = models.IntegerField(db_column='SupplyQuantity', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productsupply'
        unique_together = (('vendorid', 'prodid', 'supplydate'),)


class Shoppingcarts(models.Model):
    cartid = models.AutoField(db_column='CartID', primary_key=True)  # Field name made lowercase.
    custid = models.ForeignKey(Customers, on_delete=models.CASCADE, db_column='CustID', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'shoppingcarts'


class Supervision(models.Model):
    adminid = models.ForeignKey(Administrators, models.DO_NOTHING, db_column='AdminID', blank=True, null=True)  # Field name made lowercase.
    custid = models.OneToOneField(Customers, models.DO_NOTHING, db_column='CustID', primary_key=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'supervision'


class Vencompany(models.Model):
    vendorid = models.OneToOneField('Vendors', models.DO_NOTHING, db_column='VendorID', primary_key=True)  # Field name made lowercase.
    ntn = models.IntegerField(db_column='NTN', blank=True, null=True)  # Field name made lowercase.
    creditlimit = models.DecimalField(db_column='CreditLimit', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vencompany'


class Vendors(models.Model):
    vendorid = models.AutoField(db_column='VendorID', primary_key=True)  # Field name made lowercase.
    vname = models.CharField(db_column='VName', max_length=60, blank=True, null=True)  # Field name made lowercase.
    vcountry = models.CharField(db_column='VCountry', max_length=20, blank=True, null=True)  # Field name made lowercase.
    vcity = models.CharField(db_column='VCity', max_length=20, blank=True, null=True)  # Field name made lowercase.
    vaddress = models.CharField(db_column='VAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vendors'


class Venperson(models.Model):
    vendorid = models.OneToOneField(Vendors, models.DO_NOTHING, db_column='VendorID', primary_key=True)  # Field name made lowercase.
    nic = models.IntegerField(db_column='NIC', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'venperson'
