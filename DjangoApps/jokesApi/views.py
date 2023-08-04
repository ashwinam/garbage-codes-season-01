from django.shortcuts import render, HttpResponse

# Create your views here.


def Index(request):
    return HttpResponse('Welcome to the jokes party.')


# TODO 1:
'''
Joke Sharing API:
Develop an API that allows users to post jokes and retrieve random jokes from the collection. Users can submit jokes with categories or tags, and the API should have endpoints to filter jokes based on these categories. Each joke should have a text and a category. This project will give you experience in creating APIs that support both reading and writing operations.

Keep in mind that the complexity of the projects can vary depending on your familiarity with Django Rest Framework and web development in general. These ideas should be simple enough to complete within a day, but feel free to modify or expand them to suit your interests and learning goals. Happy coding!
'''
