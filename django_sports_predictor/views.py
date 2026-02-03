from django.db.models import F
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Sport, Choice


# Create your views here.
class IndexView(generic.ListView):
    # Sort questions by the latest five ordered by published date
    template_name = "polls/index.html"
    context_object_name = "sorted_sport_arr"

    def get_queryset(self):
        """
        Return the last five published questions
        (not including those set to be published in the future
        """
        return Sport.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by("-pub_date")


# Displays a question text, with no results but with a form to vote
class DetailView(generic.DetailView):
    model = Sport

    template_name = "polls/detail.html"

    def get_queryset(self):
        return Sport.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Sport

    template_name = "polls/results.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sport = self.object

        choices = list(sport.choice_set.all())
        total = sum(c.votes for c in choices)
        # Attach a percentage to each choice
        for c in choices:
            c.percent = (c.votes / total * 100) if total else 0

        context["choices"] = choices
        context["total_votes"] = total
        return context


def vote(request, sport_id):
    sport = get_object_or_404(Sport, pk=sport_id)

    try:
        selected_choice = sport.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the sport voting form
        return render(request,
                      template_name="polls/detail.html",
                      context={
                          "sport": sport,
                          "error_message": "You didn't select a choice."
                      })
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse(
            "polls:results",
            args=[sport_id]
        ))
