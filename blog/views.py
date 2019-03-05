from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone
from django.core.paginator import Paginator 

def home(request):
    blogs = Blog.objects # 쿼리셋 # 메소드

    # 블로그 모든 글을 대상으로
    blog_list = Blog.objects.all()
    # 블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(blog_list, 3)
    # request된 페이지가 뭔지 알아내고 (request 페이지를 변수에 담아내고)
    page = request.GET.get('page')
    # request된 페이지를 얻어온 뒤 return 해준다
    posts = paginator.get_page(page)

    return render(request, 'home.html', {'blogs': blogs, 'posts': posts})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'blog': blog_detail})

def new(request):
    return render(request, 'new.html')

def create(request): # 입력받은 데이터를 데이터베이스에 넣어주는 함수
    blog = Blog()
    blog.title = request.GET['title'] # wordcount때 배웠음
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now() # 현재시간!! import 해줘야하는 것이 있음
    blog.save() # 객체.delete() : 지우기
    return redirect('/blog/' + str(blog.id)) # 이 url로 넘기세요 (render와 다름) # id는 int니까 str로 형변환