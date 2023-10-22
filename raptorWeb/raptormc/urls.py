from django.urls import URLPattern, path, re_path

from raptorWeb.raptormc import views
from raptorWeb.raptormc.exchange import current_urlpatterns

app_name: str = "raptormc"

urlpatterns: list[URLPattern] = [

    path('raptormc/api/html/home', views.HomeServers.as_view(), name="home"),
    # Information
    path('raptormc/api/html/announcements', views.Announcements.as_view(), name="announcements"),
    path('raptormc/api/html/rules', views.Rules.as_view(), name="rules"),
    path('raptormc/api/html/banneditems', views.BannedItems.as_view(), name="banneditems"),
    path('raptormc/api/html/voting', views.Voting.as_view(), name="voting"),
    path('raptormc/api/html/howtojoin', views.HowToJoin.as_view(), name="howtojoin"),
    path('raptormc/api/html/applications', views.StaffApps.as_view(), name="applications"),
    # Created Pages
    path('raptormc/api/html/pages/<str:page_name>', views.PageView.as_view(), name="pages"),
    # Users
    path('raptormc/api/html/user', views.SiteMembers.as_view(), name='user'),
    path('raptormc/api/html/user/<str:profile_name>', views.User_Page.as_view(), name="user_page"),
    path('raptormc/api/html/user/reset/<str:profile_name>/<str:user_reset_token>', views.User_Pass_Reset.as_view(), name="user_reset_pass"),
    # Admin Panel
    path('panel/', views.Admin_Panel.as_view(), name='admin_panel_base'),
    # 404
    path('404', views.View_404.as_view(), name='404_view'),
    # API
    path('raptormc/api/action/session/headerbox/update', views.Update_Headerbox_State.as_view(), name='update_headerbox_state'),
    # Base View
    path('rules', views.BaseView.as_view(), name="base"),
    re_path(r'\S*', views.BaseView.as_view(), name="base")

]

current_urlpatterns.append(urlpatterns)
