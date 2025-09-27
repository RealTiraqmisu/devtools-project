from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Booking(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = "Pending", "รอการอนุมัติ"
        CONFIRM = "Confirm", "ยืนยัน"
        COMPLETED = "Completed", "เสร็จสิ้น"
    customer = models.ForeignKey(User, on_delete=models.SET_NULL)
    sitter = models.ForeignKey(User, on_delete=models.SET_NULL)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=15, choices=StatusChoices.choices)

    def __str__(self):
        return f"Customer : {self.customer} | Sitter : {self.sitter} | Service : {self.service} | {self.statusChoicesThai()} {self.start_date.strftime("%B %d, %Y")}-{self.end_date.strftime("%B %d, %Y")}"
        
    def statusChoices(self):
        status = {"Pending": 0, "Confirm": 1, "Completed": 2}
        return status[self.status]
    
    def statusChoicesThai(self):
        status = {"Pending": "รอการอนุมัติ", "Confirm": "ยืนยัน", "Completed": "เสร็จสิ้น"}
        return status[self.status]