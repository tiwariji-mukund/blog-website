from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponse


# def index(request):
# 	return render(request, 'index.html', {})

class Home(ListView):
	model = Post
	template_name = 'index.html'
	# ordering = ['-created_on']
	ordering = ['-id']

	def get_context_data(self, *args,**kwargs):
		catg_menu = Category.objects.all()
		context = super(Home, self).get_context_data(*args, **kwargs)
		context["catg_menu"] = catg_menu
		return context


def CategoryView(request, catg):
	category_posts = Post.objects.filter(category=catg)
	ordering = ['-created_on']
	return render(request, 'category.html', {'catg': catg.title().replace('-', ' '), 'category_posts': category_posts})

	
class BlogDetail(DetailView):
	model = Post
	template_name = 'blog_detail.html'

	def get_context_data(self, *args,**kwargs):
		catg_menu = Category.objects.all()
		context = super(BlogDetail, self).get_context_data(*args, **kwargs)
		stuff = get_object_or_404(Post, id=self.kwargs['pk'])

		total_likes = stuff.total_likes()
		liked = False
		if stuff.likes.filter(id=self.request.user.id).exists():
			liked = True

		context["catg_menu"] = catg_menu
		context["total_likes"] = total_likes
		context["liked"] = liked
		return context

class AddPost(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'add_blogs.html'
	# fields = '__all__'
	# fields = ['title', 'title_tag', 'author', 'content']

class AddComment(CreateView):
	model = Comment
	form_class = CommentForm
	template_name = 'add_comment.html'
	# fields = '__all__'
	ordering = ['-date_added']


	def form_valid(self, form):
		form.instance.post_id = self.kwargs['pk']
		return super().form_valid(form)

	success_url = reverse_lazy('home')
	
	

class UpdatePost(UpdateView):
	model = Post
	template_name = 'edit.html'
	form_class = EditForm
	# fields = ['title', 'title_tag', 'content']

class DeletePost(DeleteView):
	model = Post
	template_name = 'delete.html'
	success_url = reverse_lazy('home')

class AddCategory(CreateView):
	model = Category
	# form_class = PostForm
	template_name = 'add_category.html'
	fields = '__all__'

def CategoryList(request):
	category_menu = Category.objects.all()
	ordering = ['-created_on']
	return render(request, 'category_list.html', {'category_menu': category_menu})

def LikesOnPost(request, pk):
	post = get_object_or_404(Post, id=request.POST.get('post_id'))
	liked = False
	if post.likes.filter(id=request.user.id).exists():
		post.likes.remove(request.user)
		liked = False
	else:
		post.likes.add(request.user)
		liked = True
	
	return HttpResponseRedirect(reverse('article', args=[str(pk)]))

