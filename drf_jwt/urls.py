from django.contrib import admin
from django.urls import path , include
from home import views
from rest_framework.routers import DefaultRouter
from rest_framework import urls
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


router = DefaultRouter()

router.register('studentapi' , views.studentViewSet , basename="student")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include(router.urls)),
    path('gettoken/' , TokenObtainPairView.as_view() , name = "tokenobtainpair"),
    path('refreshtoken/' , TokenRefreshView.as_view() , name = "tokenrefresh"),
    path('verifytoken/' , TokenVerifyView.as_view() , name = "tokenverify"),
    ]

# get token 
#  http POST  http://127.0.0.1:8000/gettoken/ username="admin" password="9084470790" 

# verify token

# PS F:\projects\django\rest api>  http POST  http://127.0.0.1:8000/verifytoken/ token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA2NDM2Njc0LCJpYXQiOjE3MDY0MzYzNzQsImp0aSI6ImQ1Mjc1MTc4NWY2NTQ5YjBiY2Q5NmZjNDFmZmQwOWVkIiwidXNlcl9pZCI6M30.chQpJkpu8FF9kccsWEeTt5j7pjJpOXioVxygwa36VYI"

# refresh token
#  http POST  http://127.0.0.1:8000/refreshtoken/ refresh="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwNjUyMjc3NCwiaWF0IjoxNzA2NDM2Mzc0LCJqdGkiOiIxMjQxMzFhOWU3NmY0ZThhOWJjYTQ0YTJlNDIzZTMzNCIsInVzZXJfaWQiOjN9.vFFaSfsm8LvQMAeaCdYjMBx93XQHQcVlpzFYTMjh1Aw"

# acces api using token 

# http http://127.0.0.1:8000/studentapi/ 'Authorization:Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA2NDQwMzIwLCJpYXQiOjE3MDY0MzYzNzQsImp0aSI6IjZmZTYwMzQ1MDhkYjQzYmM4YTRiOThhNzJmZmZiZGUyIiwidXNlcl9pZCI6M30._U_scChGI-x09Xpwj6kyZg8rtY92NwVhnIftgeUTM6I'

# post data in api
# http -f POST http://127.0.0.1:8000/studentapi/ username=arvind bio=dm 'Authorization:Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA2NDQwNjQ3LCJpYXQiOjE3MDY0MzYzNzQsImp0aSI6IjY2MjRjZjI1MWM2YjQ4MGM5NTk2MThhN2Q1ODllNDQ2IiwidXNlcl9pZCI6M30.l4qQs_NVWXiNtiGqOgG4Ef_iDTrP5Yew_gvN0a7crOM