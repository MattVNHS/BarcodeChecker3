class AccountRouter:
# We only allow read access for models with the app_label 'account'
# all other database operations from other apps are performed on the default database

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'account':
            return 'Shire_Data'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'account':
            return False
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
                obj1._meta.app_label == 'account'
                or obj2._meta.app_label == 'account'
        ):
            return False
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'account':
            return False
        return None