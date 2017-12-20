from django.core.management.base import BaseCommand
from dyluna.dyluna_app.models.models import *


class Command(BaseCommand):
    args = 'Nothin yet'
    help = 'Helper function to populate db with some values'

    def _create_user_roles(self):
        mod_role = User_Role(role_name='moderator')
        attendee_role = User_Role(role_name='attendee')

        mod_role.save()
        attendee_role.save()

    def _create_diets(self):
        vege = Diet(name='vege', description='brak produktow odzwiezecych')
        ichtiovege = Diet(name='ichtiovege', description='bez odzwiezecych, ale ryby ok')

        vege.save()
        ichtiovege.save()

    def _create_users(self):
        user1 = User(
            name = "Stanislas",
            last_name='Baguette',
            diet_id = 1,  # foreign key
            user_role_id=1
        )

        user2 = User(
            name = "Tester",
            last_name='Testowy',
            diet_id = 2,  # foreign key
            user_role_id=2
        )

        user1.save()
        user2.save()


    def _create_workshop_types(self):
        manual_wk = Type( name = "manualne/majsterkowe", description='Zwiazane z nauka robienia czegos i robieniem tego w praktyce')
        theory_wk = Type(name = "teoretyczne", description='Takie, na których lepiej wziąć notatnik, niż rękawice robocze')

    def _create_equipment(self):
        pass

    def _create_workshops(self):
        wk1 = Workshop(
            name = "szydełkowanie",
            user_id = 1,
            type_id = 1,
            description = 'Nauczymy sie szydełkować, zrobimy szalik!'
        )
        wk2 = Workshop(
            name = "Całki",
            user_id = 2,
            type_id = 2,
            description = 'Pochodne, całki i różniczki. Wszystko co najlepsze!'
        )


    def _create_places(self):
        pass

    def _create_workshop_schedule(self):
        pass

    def _create_equipment(self):
        pass

    def _create_meal(self):
        pass

    def _create_meal_time(self):
        pass

    def _create_preferences(self):
        pass

    def handle(self, *args, **options):
        self._create_user_roles()
        self._create_diets()
        self._create_users()
        self._create_workshop_types()
        self._create_workshops()
        self._create_places()
        self._create_workshop_schedule()
        self._create_equipment()
        self._create_meal()
        self._create_meal_time()
        self._create_preferences()