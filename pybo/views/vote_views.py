from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from ..models import Question, Answer, Comment


@login_required(login_url='common:login')
def vote_question(request, question_id):
    """
    pybo 질문추천등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.author:
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다')
    else:
        question.voter.add(request.user)
    return redirect('pybo:detail', question_id=question.id)


@login_required(login_url='common:login')
def vote_question_delete(request, question_id):
    """
    pybo 질문추천취소
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user in question.voter.all():
        question.voter.remove(request.user)
    else:
        messages.error(request, '본인이 추천한 글만 추천을 취소할 수 있습니다.')
    return redirect('pybo:detail', question_id=question.id)


@login_required(login_url='common:login')
def vote_answer(request, answer_id):
    """
    pybo 답글추천등록
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user == answer.author:
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다')
    else:
        answer.voter.add(request.user)
    return redirect('pybo:detail', question_id=answer.question.id)


@login_required(login_url='common:login')
def vote_answer_delete(request, answer_id):
    """
    pybo 답글추천취소
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user in answer.voter.all():
        answer.voter.remove(request.user)
    else:
        messages.error(request, '본인이 추천한 글만 추천을 취소할 수 있습니다.')
    return redirect('pybo:detail', question_id=answer.question.id)


@login_required(login_url='common:login')
def vote_create_comment(request, comment_id):
    """
    pybo 댓글 추천등록
    """
    comment_type = request.GET.get('type')
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.user == comment.author:
        messages.error(request, '본인이 작성한 댓글은 추천할 수 없습니다')
    else:
        comment.voter.add(request.user)

    if comment_type == "question":
        return redirect('pybo:detail', question_id=comment.question.id)
    else:
        answer = get_object_or_404(Answer, pk=comment.answer.id)
        return redirect('pybo:detail', question_id=answer.question.id)


@login_required(login_url='common:login')
def vote_delete_comment(request, comment_id):
    """
    pybo 댓글 추천취소
    """
    comment_type = request.GET.get('type')
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user in comment.voter.all():
        comment.voter.remove(request.user)
    else:
        messages.error(request, '본인이 추천한 댓글만 추천을 취소할 수 있습니다.')

    if comment_type == "question":
        return redirect('pybo:detail', question_id=comment.question.id)
    else:
        answer = get_object_or_404(Answer, pk=comment.answer.id)
        return redirect('pybo:detail', question_id=answer.question.id)
