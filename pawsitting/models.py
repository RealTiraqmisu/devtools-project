from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.TextField()
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True, blank=True)

class Booking(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = "Pending", "รอการอนุมัติ"
        CONFIRM = "Confirm", "ยืนยัน"
        COMPLETED = "Completed", "เสร็จสิ้น"
    customer = models.ForeignKey(User, on_delete= models.CASCADE, related_name='cus')
    sitter = models.ForeignKey(User, on_delete= models.CASCADE, related_name='sit')
    service = models.ForeignKey(Service, on_delete= models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=15, choices=StatusChoices.choices)

    def __str__(self):
        return f"Customer : {self.customer} | Sitter : {self.sitter} | Service : {self.service} | {self.get_status_display()} {self.start_date.strftime("%B %d, %Y")}-{self.end_date.strftime("%B %d, %Y")}"
    

class SitterProfile(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    service = models.ManyToManyField(Service, blank=True)
    cert_image = models.ImageField(upload_to='image/', null=True, blank=True)

class Review(models.Model):
    booking = models.OneToOneField(Booking, on_delete= models.CASCADE)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)