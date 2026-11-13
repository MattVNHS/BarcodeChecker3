SHIRE_DB = "Shire_Data"
READ_ONLY_APPS = {"account"}
READ_WRITE_APPS = {"shire"}
SHIRE_APPS = READ_ONLY_APPS | READ_WRITE_APPS

class ShireRouter:

    def db_for_read(self, model, **hints):
        if model._meta.app_label in SHIRE_APPS:
            return SHIRE_DB

    def db_for_write(self, model, **hints):
        if model._meta.app_label in READ_ONLY_APPS:
            raise PermissionError(f"{model.__name__} is read-only (Shire database)")
        if model._meta.app_label in READ_WRITE_APPS:
            return SHIRE_DB
        return None

    def allow_relation(self, obj1, obj2, **hints):
        in_shire_1 = obj1._meta.app_label in SHIRE_APPS
        in_shire_2 = obj2._meta.app_label in SHIRE_APPS
        if in_shire_1 or in_shire_2:
            return in_shire_1 and in_shire_2
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in SHIRE_APPS:
            return False
        if db == SHIRE_DB:
            return False
        return None