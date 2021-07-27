from django.apps import AppConfig


class SearchConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'search'

    # def ready(self):
    #     logging.info("generating fake data!")
    #     fake = Faker()
    #     keywords = ['help', 'ticket', 'support', 'data', 'tech', 'computer', 'hardware', 'software', 'dashboard',
    #                 'rating',
    #                 'install', 'working', 'admin', 'IT', 'supervisor', 'manager', 'error', 'missing', 'not installed',
    #                 'not starting', 'failure', 'boot']
    #     for _ in range(100):
    #         title = fake.sentence(ext_word_list=keywords)
    #         details = fake.sentence(ext_word_list=keywords)
    #         owner = fake.name()
    #         hd = HelpdeskModel(title=title.rstrip('.'), details=details, owner=owner)
    #         hd.save()
