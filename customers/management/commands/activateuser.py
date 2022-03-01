from ._usercommand import Command as BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        super().handle(*args, **options)
        if self.user.is_active == False:
            self.user.is_active = True
            self.user.save()
        print(self.style.SUCCESS('Done!'))
