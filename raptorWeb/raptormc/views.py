from django.views.generic import TemplateView
from os.path import join
from logging import getLogger

from raptorWeb import settings
from raptormc.util import viewContext

TEMPLATE_DIR_RAPTORMC = join(settings.TEMPLATE_DIR, "raptormc")

LOGGER = getLogger('raptormc.views')

class ShadowRaptor():
    """
    Object containing different categories of views that are used
    across the website/application.
    """
    class Info():
        """
        Views that act as static pages of information
        """
        class HomeServers(TemplateView):
            """
            Homepage with general information
            """
            template_name = join(TEMPLATE_DIR_RAPTORMC, 'home.html')

            def get_context_data(self, **kwargs): 
                context = super().get_context_data(**kwargs)
                return viewContext.update_context(context = context, informative_text_names = ["Homepage Information"], announcements=True)

        class Announcements(TemplateView):
            """
            Page containing the last 30 announcements from Discord
            """
            template_name = join(TEMPLATE_DIR_RAPTORMC, 'announcements.html')

            def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                return viewContext.update_context(context = context, informative_text_names = ["Announcements Information"], announcements=True)

        class Rules(TemplateView):
            """
            Rules page containing general and server-specific rules
            """
            template_name = join(TEMPLATE_DIR_RAPTORMC, 'rules.html')

            def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                return viewContext.update_context(context = context, informative_text_names = [
                    "Rules Information",
                    "Network Rules"])

        class BannedItems(TemplateView):
            """
            Contains lists of items that are banned on each server
            """
            template_name = join(TEMPLATE_DIR_RAPTORMC, 'banneditems.html')

            def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                return viewContext.update_context(context = context, informative_text_names = ["Banned Items Information"])

        class Voting(TemplateView):
            """
            Contains lists links for each server's voting sites
            """
            template_name = join(TEMPLATE_DIR_RAPTORMC, 'voting.html')

            def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                return viewContext.update_context(context = context, informative_text_names = ["Voting Information"])

        class HowToJoin(TemplateView):
            """
            Contains guides for downloading modpacks and joining servers.
            """
            template_name = join(TEMPLATE_DIR_RAPTORMC, 'joining.html')

            def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                return viewContext.update_context(context = context, informative_text_names = [
                    "Joining Information",
                    "Using the CurseForge Launcher",
                    "Using the FTB Launcher",
                    "Using the Technic Launcher"])

        class StaffApps(TemplateView):
            """
            Provide links to each staff application
            """
            template_name = join(settings.APPLICATIONS_DIR, 'staffapps.html')

            def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                return viewContext.update_context(context = context, informative_text_names = ["Staff App Information"])

    class User_Views():
        """
        Views related to Users
        """
        class SiteMembers(TemplateView):
            """
            Provide links to each Site Member's profile
            """
            template_name = join(TEMPLATE_DIR_RAPTORMC, 'sitemembers.html')

            def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                return viewContext.update_context(context = context)

        class User_Page(TemplateView):
            """
            Info about a User
            """
            template_name = join(TEMPLATE_DIR_RAPTORMC, 'user.html')

            def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                return viewContext.update_context(context = context)

        class User_Edit_Page(TemplateView):
            """
            Edit a User's Info
            """
            template_name = join(TEMPLATE_DIR_RAPTORMC, 'user_edit.html')

            def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                return viewContext.update_context(context = context)
