from profiles.models import Profile


def get_profile() -> Profile:
    return Profile.objects.first()