from datetime import datetime

from django.db import models


class Poll(models.Model):
    question = models.TextField()
    additionalnotes = models.TextField(default="")
    dt = models.DateTimeField(auto_now_add=True,null=True)
    option_one = models.CharField(max_length=60, default="")
    option_two = models.CharField(max_length=60, default="")
    option_three = models.CharField(max_length=60, default="")
    option_four = models.CharField(max_length=60, default="")
    option_five = models.CharField(max_length=60, default="")
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)
    option_four_count = models.IntegerField(default=0)
    option_five_count = models.IntegerField(default=0)




    def total(self):
        return self.option_one_count + self.option_two_count + self.option_three_count + self.option_four_count + self.option_five_count

    def percent1(self):
        initial = self.option_one_count / (
                self.option_one_count + self.option_two_count + self.option_three_count + self.option_four_count + self.option_five_count)
        initial2 = initial * 100
        initial3 = round(initial2, 3)
        return initial3

    def percent2(self):
        initial = self.option_two_count / (
                self.option_one_count + self.option_two_count + self.option_three_count + self.option_four_count + self.option_five_count)
        initial2 = initial * 100
        initial3 = round(initial2, 3)
        return initial3

    def percent3(self):
        initial = self.option_three_count / (
                self.option_one_count + self.option_two_count + self.option_three_count + self.option_four_count + self.option_five_count)
        initial2 = initial * 100
        initial3 = round(initial2, 3)
        return initial3

    def percent4(self):
        initial = self.option_four_count / (
                self.option_one_count + self.option_two_count + self.option_three_count + self.option_four_count + self.option_five_count)
        initial2 = initial * 100
        initial3 = round(initial2, 3)
        return initial3

    def percent5(self):
        initial = self.option_five_count / (
                self.option_one_count + self.option_two_count + self.option_three_count + self.option_four_count + self.option_five_count)
        initial2 = initial * 100
        initial3 = round(initial2, 3)
        return initial3

class Comment(models.Model):
    poll=models.ForeignKey(Poll,related_name='comments',on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    AreYouVoting=models.CharField(max_length=255,default="")
    email=models.EmailField()
    note=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)