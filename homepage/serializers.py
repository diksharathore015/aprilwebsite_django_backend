from rest_framework import serializers
from .models import *
from media.serializers import *
# class BannerSerializer(serializers.ModelSerializer):

#     image_id = serializers.PrimaryKeyRelatedField(
#         queryset=Media.objects.all(),
#         source='image',  
#         many=True,
#         write_only=True
#     )
#     image =MediaSerializer(many=True, read_only=True)
    
#     class Meta:
#         model = Banners
#         fields = ['id','title','image_id' ,'image']    


class BannerSerializer(serializers.ModelSerializer):
    image_id = serializers.PrimaryKeyRelatedField(
        queryset=Media.objects.all(),
        source='image',  
        many=True,
        write_only=True
    )
    image = MediaSerializer(many=True, read_only=True)
    
    class Meta:
        model = Banners
        fields = ['id', 'title', 'image_id', 'image']

    def create(self, validated_data):
        # Extract image data
        image_data = validated_data.pop('image', [])
        
        # Check if a Banner with the same image IDs already exists
        existing_banners = Banners.objects.filter(image__in=image_data).distinct()
        if existing_banners.exists():
            # Delete the existing banners if required
            existing_banners.delete()

        # Create the new Banner
        banner = Banners.objects.create(**validated_data)
        banner.image.set(image_data)  # Set the many-to-many relationship
        return banner

class SeoSerializer(serializers.ModelSerializer):
       image_id = serializers.PrimaryKeyRelatedField(
        queryset=Media.objects.all(),
        source='logo',  
        many=True,
        write_only=True
    )
       logo = MediaSerializer(many=True, read_only=True)

       class Meta:
        model = SEO
        fields = [
            'id', 'title',  'logo' ,"image_id" ,'description','keywords','canonical_url','address','contact_number' ,'whatsapp_number','youtube_link','facebook_link','instagram_link','scripts', ]


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id',  'course' ,'question', 'answer']



class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = ['id', 'title', 'description', 'image']
     
class home_page_dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = home_page_data
        fields = ['id', 'title', 'description', ]
        

      
       
    