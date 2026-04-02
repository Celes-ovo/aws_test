from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
# our modules
from .models import MyModel
from rest_framework import generics


# def test_view(request):
#     my_model = MyModel()
#     return my_model.get_dict()

# def test_view(request):
#     my_model = MyModel()
#     context = my_model.get_dict()

#     return render(request=request, template_name='dict_model/test.html', context=context)


"""
Django의 render 함수와 JsonResponse는 목적이 서로 다르기 때문에 JsonResponse(context)를 context 인자로 직접 전달하지
  않았습니다.

   1. render 함수의 context 인자: Django 템플릿 엔진은 context로 일반 파이썬 딕셔너리(dict)를 기대합니다. 템플릿 파일(.html)
      내에서 {{ Landmark }}와 같이 변수를 사용할 때, 템플릿 엔진은 전달받은 딕셔너리에서 해당 키를 찾아 값을 출력합니다.
   2. JsonResponse의 역할: JsonResponse는 데이터(딕셔너리 등)를 JSON 형식으로 직렬화하여 HTTP 응답 객체(Response Object)로
      만드는 도구입니다. 주로 웹 브라우저에 HTML이 아닌 JSON 데이터를 직접 반환할 때(API 서버 등) 사용합니다.
   3. 오류 발생 원인: 만약 context=JsonResponse(context)라고 작성하면, 템플릿 엔진은 실제 데이터가 들어있는 딕셔너리가
      아니라 '응답 객체' 자체를 받게 됩니다. 이 경우 템플릿 내부에서 {{ Landmark }}를 호출해도 값을 찾을 수 없어 화면에
      아무것도 출력되지 않거나 오류가 발생할 수 있습니다.
      (context must be a dict rather than JsonResponse.)

  따라서 템플릿을 통해 HTML을 렌더링할 때는 MyModel().get_dict()가 반환하는 순수 딕셔너리 객체를 그대로 전달하는 것이 올바른
  방법입니다.
"""
class TestView(generics.GenericAPIView):
    def get(self, request):
      my_model = MyModel()
      context = my_model.get_dict()

      # 디버깅용 출력
      print("context:", context)

      # 받은 context를 템플릿에 전달하여 렌더링
      return render(request=request, template_name='dict_model/test.html', context=context)
