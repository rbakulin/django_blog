import os
import django.apps
import django

from django.core.wsgi import get_wsgi_application
from rest_framework import viewsets, serializers
# from rest_framework import routers

os.environ['DJANGO_SETTINGS_MODULE'] = 'django_blog.settings'
application = get_wsgi_application()
all_models = django.apps.apps.get_models()

# for current_model in all_models:
#     class CurrentModelSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = current_model
#             fields = '__all__'
#
#     class CurrentModelView(viewsets.ModelViewSet):
#         queryset = current_model.objects.all()
#         serializer_class = CurrentModelSerializer
#
#     router = routers.DefaultRouter()
#     router.register()




# import os
# import django.apps
# import django
#
# from django.core.wsgi import get_wsgi_application
#
# os.environ['DJANGO_SETTINGS_MODULE'] = 'django_blog.settings'
# application = get_wsgi_application()
# all_models = django.apps.apps.get_models()
# for model in all_models:
#     print(model)
