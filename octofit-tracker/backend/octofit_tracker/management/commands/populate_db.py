from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create users
        users = [
            User(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User(name='Batman', email='batman@dc.com', team=dc),
        ]
        for user in users:
            user.save()

        # Create activities
        Activity.objects.create(user=users[0], type='Swing', duration=30, date=timezone.now().date())
        Activity.objects.create(user=users[1], type='Fly', duration=45, date=timezone.now().date())
        Activity.objects.create(user=users[2], type='Fight', duration=60, date=timezone.now().date())
        Activity.objects.create(user=users[3], type='Detective Work', duration=50, date=timezone.now().date())

        # Create workouts
        workout1 = Workout.objects.create(name='Web Swing', description='Swinging through the city')
        workout2 = Workout.objects.create(name='Armor Training', description='Suit up and train')
        workout3 = Workout.objects.create(name='Amazon Training', description='Warrior training')
        workout4 = Workout.objects.create(name='Bat Training', description='Stealth and combat')
        workout1.suggested_for.set([users[0]])
        workout2.suggested_for.set([users[1]])
        workout3.suggested_for.set([users[2]])
        workout4.suggested_for.set([users[3]])

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
