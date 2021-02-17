from .import bp as blog_bp

@blog_bp.route('/')
def home():
    return 'It works'