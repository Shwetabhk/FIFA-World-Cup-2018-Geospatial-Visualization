from Home.models import Team


class OptionCreator:
    def create():
        teams=Team.objects.all()
        options=([(i.name,i.name) for i in teams])
        return options