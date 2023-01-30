from django.contrib.auth.views import LogoutView, LoginView
from django.views.generic import CreateView,DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from custom_user.models import UserProfile
from blog.models import Post

User = get_user_model()


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'custom_user/user_create.html'
    success_url = reverse_lazy('blog:post_list')



class UserLoginView(LoginView):
    template_name ='custom_user/user_login.html'
    success_url = reverse_lazy('blog:post_list')


class UserProfileDetailView(DetailView):
    model = UserProfile
    template_name = 'custom_user/user_profile.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
       extra_context = super().get_context_data(**kwargs)
       extra_context['own_post']=Post.objects.filter(author_id=self.request.user.id)
       return extra_context