from django.shortcuts import render, get_object_or_404
from .models import Pet

def pets_list(request):
    pets = Pet.objects.filter(is_active=True).order_by("-created_at").prefetch_related('images')
    return render(request, "pet/page-index.html", {
        "title": "Питомцы",
        "meta_text": "Этот раздел посвящен питомцам, которым требуется ваша помощь и забота. Здесь вы найдете истории животных, оказавшихся в сложной ситуации, а также информацию о том, как вы можете помочь каждому из них: от временной опеки до пожертвований или поиска постоянного дома. Присоединяйтесь к спасению жизней и дарите шанс на лучшее будущее нашим четвероногим друзьям.",
        "meta_keywords": "помощь животным, животные в беде, питомцы, нуждающиеся в помощи, спасение животных, приюты, временная опека, найти дом животным, помощь бездомным животным",
        "pets": pets
    })

def pet_detail(request, slug):
    pet = get_object_or_404(Pet, slug=slug, is_active=True)
    return render(request, "pet/page-detail.html", {
        'pet': pet,
        'title': pet.meta_title,
        'meta_text': pet.meta_text,
        'meta_keywords': pet.meta_keywords
    })