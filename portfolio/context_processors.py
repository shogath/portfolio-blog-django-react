from blog.models import Post

def top_posts(request):
    return {'top_posts': Post.objects.all()[:4]}