from django.db import models

# Create your models here.
class Player(models.Model):
    player_id = models.AutoField(primary_key=True)
    player_nickname = models.CharField(max_length=128, unique=True)
    player_name = models.CharField(max_length=150, blank=False)
    player_email = models.CharField(max_length=250, blank=False)
    player_phone_number = models.CharField(max_length=11, blank=True, default='')
    player_age = models.IntegerField(blank=False)

    def __str__(self):
        return f'Id: {self.player_id} | Nickname: {self.player_nickname} | E-mail: {self.player_email}'

class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    team_name = models.CharField(max_length=255, unique=True, blank=False)
    team_game = models.CharField(max_length=255, unique=True, blank=False)
    team_quantity_members = models.IntegerField(blank=False)

    def __str__(self):
        return f'Id: {self.team_id} | Team Name: {self.team_name} | Team Game: {self.team_game}'