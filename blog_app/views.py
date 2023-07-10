from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone

# Create your views here.

#전체 게시글 페이지
def index(request):
    if Post.objects is not None:
        content=Post.objects
        return render(request,'temp/index.html',{'check':content})
    else:
        return render(request,'temp/index.html')

#게시글작성페이지
def create(request):
    return render(request,'temp/create.html')

#게시글작성 후 저장 -> 메인페이지
def storage(request):
    post_save=Post()
    post_save.selectType=request.GET.get('seltype','')
    post_save.subject=request.GET['subject01']
    post_save.memo=request.GET['memo01']
    post_save.created_date=timezone.datetime.now()

    

    post_save.save()
    #return redirect('../index')
    return redirect('/')

#작성된 글 세부내용 표시(글의 아이디를 찾아 특정 글의 세부내용을 본다.)
def specific(request,id):
    
    content=get_object_or_404(Post,pk=id)
    
    return render(request,'temp/specific.html',{'check':content})

#세부내용의 글을 삭제한다.
def delete(request,id):
    content=get_object_or_404(Post,pk=id)
    content.delete()
    return redirect('/')

#세부내용의 글을 수정하는 페이지로 이동한다.    
def update(request,id):
    content=get_object_or_404(Post,pk=id)
    return render(request,'temp/update.html',{'check':content})

#세부내용의 글을 수정한다.
def doupdate(request,id):
    content=get_object_or_404(Post,pk=id)
    content.selectType=request.GET.get('seltype','')
    content.subject=request.GET['subject02']
    content.memo=request.GET['memo02']
    content.created_date=timezone.datetime.now()
    content.save()
    return redirect('/'+str(id))