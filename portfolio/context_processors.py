from blog.models import Post

def top_posts(request):
    """
    Context processor that provides 4 latest blog posts
    """
    return {'top_posts': Post.objects.all()[:4]}