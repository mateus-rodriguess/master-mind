from apps.bot.models import DoneList, Ranking


def add_bonus(profile):
    """
    add bonus the ranking
    """
    done_list = DoneList.objects.filter(id_user=profile.pk).last()
    ranking = Ranking.objects.filter(id_user=profile.pk).last()
    try:
        if done_list.streak_count == 7:
            ranking.points = ranking.points + 10
            ranking.save()
        else:
            if done_list.streak_count == 30:
                ranking.points = ranking.points + 50
                ranking.save()
        return True
    except Exception as e:
        print(f"Erro add_bonus: {e}")
        return False
