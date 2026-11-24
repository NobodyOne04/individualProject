from django.shortcuts import redirect, render
from django.views import View

from morphology.adapters.inbound.web.forms import InflectForm, OperationForm, TextForm
from morphology.composition import morphology_service


class IndexView(View):
    def get(self, request):
        return render(request, "morphology/index.html", {"form": OperationForm()})

    def post(self, request):
        form = OperationForm(request.POST)
        if form.is_valid():
            return redirect(form.cleaned_data["operation"])
        return render(request, "morphology/index.html", {"form": form})


class _TextOperationView(View):
    """GET shows the form; a valid POST shows the results under it."""

    template = ""
    form_class = TextForm

    def run(self, data):
        raise NotImplementedError

    def get(self, request):
        return render(request, self.template, {"form": self.form_class()})

    def post(self, request):
        form = self.form_class(request.POST)
        results = self.run(form.cleaned_data) if form.is_valid() else None
        return render(request, self.template, {"form": form, "results": results})


class NormalView(_TextOperationView):
    template = "morphology/normal.html"

    def run(self, data):
        return morphology_service().normal_forms(data["text"])


class GrammarView(_TextOperationView):
    template = "morphology/grammar.html"

    def run(self, data):
        return morphology_service().grammar(data["text"])


class InflectView(_TextOperationView):
    template = "morphology/inflect.html"
    form_class = InflectForm

    def run(self, data):
        return morphology_service().inflect(data["text"], data["case"], data["number"])
