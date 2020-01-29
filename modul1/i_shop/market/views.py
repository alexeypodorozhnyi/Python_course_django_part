from django.shortcuts import render

# Create your views here.

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Item, ShoppingEvent, ReversalEvent, Profile
from .forms import ShoppingEventForm, ItemForm, ReversalForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from .utils import check_shopping_event_time


class ItemList(ListView):
    model = Item
    template_name = 'index.html'
    paginate_by = 10
    ordering = ['name']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context.update({
            'shopping_event_form': ShoppingEventForm
        })
        return context


class ShoppingEventCreate(LoginRequiredMixin, CreateView):
    model = ShoppingEvent
    http_method_names = ['post']
    success_url = '/'
    form_class = ShoppingEventForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        profile = Profile.objects.get(user=self.request.user)
        self.object.profile = profile
        item = Item.objects.get(pk=self.request.POST.get("item", ""))
        self.object.item = item
        if not ShoppingEvent.check_count_of_items(self.object):
            messages.warning(self.request, "We have less items that you want. Please contact with our manager.")
            return HttpResponseRedirect('/')
        if not ShoppingEvent.check_sum_in_profile_wallet(self.object):
            messages.warning(self.request, "The sum of your order less that you have")
            return HttpResponseRedirect('/')
        self.object.order_sum = item.price * self.object.count_of_items
        profile.reduce_wallet_sum(self.object.order_sum)
        item.reduce_item_count(self.object.count_of_items)
        self.object.save()
        return super().form_valid(form)


class ReversalList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = ReversalEvent
    template_name = 'reversals.html'
    paginate_by = 10
    permission_required = 'ReversalEvent.can_view'

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            queryset = queryset.filter(is_confirmed=False)
        return queryset


class BoughtItemList(LoginRequiredMixin, ListView):
    model = ShoppingEvent
    template_name = 'bought.html'
    paginate_by = 100

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            queryset = queryset.filter(profile=Profile.objects.get(user=self.request.user))
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context.update({
            'reversal_create_form': ReversalForm
        })
        return context


class ItemCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Item
    success_url = '/'
    form_class = ItemForm
    template_name = 'item_create.html'
    permission_required = 'Item.can_create'


class ItemUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Item
    success_url = '/'
    form_class = ItemForm
    template_name = 'item_update.html'
    permission_required = 'Item.can_change'


class ReversalCreate(LoginRequiredMixin, CreateView):
    model = ReversalEvent
    success_url = '/'
    form_class = ReversalForm
    template_name = 'reversal_create.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        shopping_event = ShoppingEvent.objects.get(pk=self.request.POST.get("shopping_event", ""))
        self.object.shopping_event = shopping_event
        if not check_shopping_event_time(shopping_event.event_date_time):
            messages.warning(self.request, "You cant return item. Time is up")
            return HttpResponseRedirect('/')
        try:
            preveous_shop_event = ReversalEvent.objects.get(shopping_event=self.request.POST.get("shopping_event", ""))
        except ReversalEvent.DoesNotExist:
            preveous_shop_event = None
        if preveous_shop_event:
            messages.warning(self.request,
                                 "You have already Sent a request for return money. Please wait for admin "
                                 "approve")
            return HttpResponseRedirect('/')
        self.object.save()
        return super().form_valid(form)


class ReversalConfirm(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = ReversalEvent
    success_url = '/'
    form_class = ReversalForm
    permission_required = 'ReversalEvent.can_change'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        if self.request.POST.get('decision') == 'Submit':
            self.object.is_confirmed = True
            self.object.save()
            shopping_event = ShoppingEvent.objects.get(pk=self.request.POST.get("shopping_event", ""))
            shopping_event.profile.add_wallet_sum(shopping_event.order_sum)
            shopping_event.item.add_item_count(shopping_event.count_of_items)
        return super().form_valid(form)


class ReversalDecline(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = ReversalEvent
    success_url = '/'
    permission_required = 'ReversalEvent.can_delete'
