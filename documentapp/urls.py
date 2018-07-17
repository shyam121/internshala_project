from django.urls import path

from documentapp.views import *
from django.conf.urls import url
from db_file_storage.compat import url, reverse_lazy
app_name='documentapp'

urlpatterns = [

    path('home/',Mainpage,name="mainpage"),
    path('signup/', SignupView.as_view(), name="sign_up"),
    path('login/', LoginView.as_view(), name="loginpage"),
    path('logout/', logout_user, name="logoutpage"),

#for single doc
    path('singledoclists/', SingledocListsView.as_view(), name="singledoc.list"),
    path('singledoclists/<int:pk>',GetUniqueDataView.as_view(),name="uniquedoc"),
    path('singledoclists/add', add_SingleSocDetails.as_view(), name="singledoc.add"),
    path('singledoclists/edit/<int:pk>', edit_SingleDocDetails.as_view(), name="singledoc.edit"),
    path('singledoclists/delete/<int:pk>', delete_SingleDocDetails.as_view(), name="singledoc.delete"),


    path('users/',UserDetailsView.as_view(),name="userspage"),

    path('users/profile/<int:pk>',show_profile.as_view(),name="userprofile"),

    path('users/profile/add',add_profile.as_view(),name="profilepage"),
    path('users/profile/edit/<int:pk>',edit_profile.as_view(),name="profilepage.edit"),

    # path('student/', details_list.as_view(), name="details.list"),
    # path('student/add', add_details.as_view(), name="details.add"),
    # path('student/edit/<int:pk>', edit_details.as_view(), name="details.edit"),
    # path('student/delete/<int:pk>', delete_Details.as_view(), name="details.delete"),

]
