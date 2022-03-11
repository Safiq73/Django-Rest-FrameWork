from rest_framework import serializers
from .models import Song, Singer

class SongSerializer(serializers.ModelSerializer):
# class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Song
        fields=['id', 'title', 'duration', 'singer']
        

class SingerSerializer(serializers.ModelSerializer):
    # song=serializers.StringRelatedField(many=True, read_only=True)
    # By mentioning line 11, .StringRelatedField(many=True, read_only=True) we will be seeing the song name instead of the song id
    
    # song=serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # will show the primary key
        
    # song=serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='song-detail')
    # Will form a link link like this "http://127.0.0.1:8000/serializer_relations/song/1/", 
    
    # song=serializers.SlugRelatedField(many=True, read_only=True, slug_field='duration')
    # will show whatever field we mention in slug_field
    
    # song=serializers.HyperlinkedIdentityField(view_name='song-detail')
    # Will form a hyper link like this "song": "http://127.0.0.1:8000/serializer_relations/song/1/"
    
    
    songby=SongSerializer(many=True, read_only=True)
    class Meta:
        model=Singer
        # fields=['id', 'name', 'gender', 'song']
        fields=['id', 'name', 'gender', 'songby']
        # Here we are able to mention the field song, as we mentionede in models.py related_name='song' in the Song class, and in the get request you will be able to see the songs id which sang by respective singer        
        