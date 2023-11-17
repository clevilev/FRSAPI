from django.contrib.auth.models import Group


class AuthChecker:
    def __int__(self, auth_status, user_id):
        self.user_id = user_id
        self.auth_status = auth_status

    def check_group_id(self):
        instance = Group.objects.get(field_name=self.auth_status)
        id_of_auth_status = instance.id
