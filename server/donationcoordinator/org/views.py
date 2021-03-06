from pprint import pprint

from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError, PermissionDenied
from django.http import *
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView, UpdateView

from donationcoordinator.views import CreateOrUpdateView
from donator.libs import OrgItemList
from donator.models import User, Home
from donator.views import ItemsUpdate
from org.forms import OrgForm, HomeSearchForm, OrgItemsForm
from org.models import Org, OrgItems


# Create your views here.

def index(request: HttpRequest):
    template_name = 'org/index.html'
    context = {}
    return render(request, template_name, context)


@login_required
def my_org(request: HttpRequest, context={}):
    template_name = 'org/org_detail.html'
    user: User = request.user
    org: Org = user.org

    if org is not None:
        return render(request, OrgDetail.template_name, {'org': org, 'can_edit_org': True})
    else:
        return HttpResponseRedirect(reverse('org:org_list'))


def org_list(request: HttpRequest, context={}):
    template_name = "org/org_list.html"

    orgs = Org.objects.filter()

    context['orgs_list'] = orgs

    return render(request, template_name, context)


class OrgCreateOrUpdate(CreateOrUpdateView):
    model = Org
    template_name = 'org/org_edit.html'
    form_class = OrgForm

    @login_required
    def form_valid(self, form):
        user = User.objects.get(username=self.request.user.username)

        # print("user:")
        # print(user)
        # print("user's org:")
        # print(user.org)

        # print("Current Org being edited:")
        # print(form.instance)

        if user.org.pk != form.instance.pk:
            raise ValidationError("You do not own this Org and cannot edit it!")

        return super(OrgCreateOrUpdate, self).form_valid(form)

    @login_required
    def get_success_url(self):
        return reverse('org:org_detail', kwargs={'pk': self.object.id})


class OrgDetail(DetailView):
    model = Org
    template_name = 'org/org_detail.html'


class OrgCreate(OrgCreateOrUpdate):
    def form_valid(self, form: OrgForm):
        user: User = self.request.user
        org: Org = user.org_or_none()

        if org is not None:
            raise ValidationError('You already have an Org, you cannot make multiple ones!')

        form.save()

        User.objects.filter(pk=user.pk).update(org=form.instance)

        return super(OrgCreateOrUpdate, self).form_valid(form)


class OrgItemsUpdate(ItemsUpdate, UpdateView):
    model = OrgItems
    template_name = 'org/items.html'
    form_class = OrgItemsForm
    illegal_keys = [  # keys we do NOT want in our form
        'csrfmiddlewaretoken'
    ]

    def get_object(self, queryset=None):
        return self.request.user.org

    def get_context_data(self, **kwargs):
        context = super(OrgItemsUpdate, self).get_context_data(**kwargs)

        context['org'] = self.request.user.org
        context['priority_descriptions'] = OrgItemList().generate_priority_descriptions()

        return context

    def form_valid(self, form):
        user = self.request.user

        self.org = self.get_object()

        if not self.org.user == user:  # make sure they own the Org
            raise PermissionDenied

        return True

    def clean_form(self) -> dict:
        """Remove anything that isn't an {'item':number} value in
        this form's POST data."""
        d = {}

        for key, val in self.request.POST.items():
            if key not in self.illegal_keys:
                try:
                    key = key.replace(OrgItemList.space_replacer, ' ')
                    val = int(val)

                    d[key] = val
                except:
                    pass

        return d

    def post(self, request: HttpRequest, *args, **kwargs):

        if self.form_valid(request):
            il = OrgItemList()
            formDict = self.clean_form()

            pprint(formDict)

            il.apply_flat_dict(formDict)

            self.org.items.data = il.data
            self.org.items.save()

            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponse("ur items ar bad :(")
        pass


def searchHomeList(request: HttpRequest):
    template_name = 'org/home_list.html'
    context = {}

    form = HomeSearchForm(request.GET or None)  # create form from GET data

    context['form'] = form

    if not form.is_valid():  # if not valid, stop.
        return render(request, template_name, context)

    miles = HomeSearchForm.Meta.default_miles
    if 'miles' in form.data:
        miles = form.data['miles'] or HomeSearchForm.Meta.default_miles

    org: Org = request.user.org_or_none()

    if org is None:
        return render(request, 'index.html', 'You need an Org to view a list of homes!')

    homesResults = Home.get_homes_locations_near(
        radius=miles,
        lat=org.location.lat(),
        lng=org.location.lng(),
    )
    homesResults = sorted(homesResults, key=lambda d: d['distance'])  # sort by closest

    context['homes_results'] = homesResults

    if len(request.GET.keys()) == 0:  # they did not give us any arguments
        context['message'] = 'hi org! You didn\'t give this view any arguments! Here\'s a default view!'
    elif 'miles' in request.GET:
        context['message'] = 'OH SO U WANT ' + str(request.GET['miles'] + "MILES DO U??")

    return render(request, template_name, context)
