from django.db import models


class UserSocialAuthManager(models.Manager):
    """Manager for the UserSocialAuth django model."""

    def get_social_auth(self, provider, uid, private_portal=None):
        try:
            return self.select_related('user').get(provider=provider,
                                                   uid=uid,
                                                   private_portal=private_portal)
        except self.model.DoesNotExist:
            return None
