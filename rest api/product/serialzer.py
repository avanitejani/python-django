from rest_framework import serializers
from .models import *

# સીરીયલાઇઝર્સનો ઉપયોગ જટિલ ડેટા પ્રકારો, જેમ કે જેંગો મોડેલ ઇન્સ્ટન્સ, પાયથોન ડેટા પ્રકારોમાં રૂપાંતરિત કરવા માટે થાય છે જે સરળતાથી JSON, XML અથવા અન્ય સામગ્રી પ્રકારોમાં રેન્ડર કરી શકાય છે.


# 3anev table na badha data mali rahe te mate nu serializers banayvu

# class AuthorSerializer(serializers.Serializer):
    # class Meta:
    #     model=Author
    #     filds='__all__'

# class PublicationSerializer(serializers.Serializer):
    # class Meta:
    #     models=Publication
    #     fields='__all__'

# class BookSerializer(serializers.Serializer):
    # class Meta:
    #     models=Book
    #     fields='__all__'



    # to representation  lakhvathi jason ma je data male tema thi foreign key ni badhi value malse 

    # without aana vgr khali id j malse biji koi information malse nahi 
    # def to_representation(self, instance):
    #     resp = super().to_representation(instance)
    #     resp['author'] = AuthorSerializer(instance.author).data
    #     resp['publication'] = PublicationSerializer(instance.publication).data
    #     return resp