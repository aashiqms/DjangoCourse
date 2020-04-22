from django.shortcuts import render
from django.views.generic import TemplateView


class HomepageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['my_statement'] = 'nice'
        context = {
            "my_statement": 'Nice to see you!',
            "my_statement_2": 'welcome',
            "my_statement_3": 'See you again'
        }
        return context

    def say_bye(self):
        return 'Goodbye'

# We created python class called HomepageView
# This class HomepageView inherits from TemplateView(subclassed)
# Associated the index.html template with the class

