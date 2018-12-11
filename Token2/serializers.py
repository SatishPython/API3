from rest_framework import serializers
from .models import Products
class ProductSeralizer(serializers.ModelSerializer):
    class meta:
        model = Products
        fields = ('pid','pname','pcost','pmfdt','pexpdt')