from django.db import models

from datetime import datetime

# Create your models here.
class Society(models.Model):
    class Meta:
        verbose_name= 'Society'
        verbose_name_plural = 'Societies'

    society_name = models.CharField(max_length=1024, unique=True)
    president = models.CharField(max_length=1024)
    address = models.CharField(max_length=1024)
    date_of_creation = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.society_name

class Member(models.Model):
    society = models.ForeignKey(Society, related_name='society', on_delete=models.CASCADE)
    name = models.CharField(max_length=1024)
    starting_share = models.IntegerField(blank=False, null=False)
    starting_loan = models.IntegerField(blank=False, null=False)
    date_of_creation = models.DateTimeField(default=datetime.now)
    month_of_creation = models.IntegerField(default=0)

    def fill_month(self):
        if self.date_of_creation:
            self.month_of_creation = self.date_of_creation.month


    def __str__(self):
        return self.name

class MonthlyRecord(models.Model):
    member = models.ForeignKey(Member, related_name='members', on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now)
    month = models.IntegerField(blank=True, null=True, default=0)
    year = models.IntegerField(blank=True, null=True)
    previous_share = models.IntegerField(blank=True, null=True)
    previous_loan = models.IntegerField(blank=True, null=True)
    share = models.IntegerField(blank=True, null=True)
    total_share = models.IntegerField(blank=True, null=True)
    installment = models.IntegerField(blank=True, null=True)
    balance_loan = models.IntegerField(blank=True, null=True)
    interest = models.IntegerField(blank=True, null=True)
    late_fees = models.IntegerField(default=0, blank=True, null=True)
    total_amount = models.IntegerField(blank=True, null=True, default=10)
    remarks = models.CharField(max_length=30, blank=True, null=True)


    def fill_month(self):
        cur_date = self.date
        month = cur_date.month
        return month
        # print(cur_month, cur_year)

    def fill_year(self):
        cur_date = self.date
        print(cur_date.month, " THERE ")
        year = cur_date.year
        return year


    def fill_share(self):
        share = 200
        return share

    def fill_total_share(self, previous_share, share):
        total_share = previous_share + share
        return total_share

    def fill_installment(self, installment):
        # installment = 5000
        return installment

    def fill_balance_loan(self, previous_loan, installment):
        balance_loan = previous_loan - installment
        return balance_loan

    def fill_interest(self, previous_loan):
        interest = 0.1 * previous_loan
        return interest

    def fill_total_amount(self):
        total_amount = 1000 #self.share + self.installment + self.interest
        return total_amount

    def __str__(self):
        return self.member.name
