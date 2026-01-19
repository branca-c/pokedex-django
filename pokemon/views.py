#from django.shortcuts import render

# Create your views here.

import json
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from .models import Pokemon


@require_http_methods(["GET"])
def pokemon_list(request):
    pokemons = Pokemon.objects.all().order_by("id")

    data = [
        {
            "id": p.id,
            "name": p.name,
            "type1": p.type1,
            "type2": p.type2,
            "level": p.level,
            "hp": p.hp,
        }
        for p in pokemons
    ]

    return JsonResponse(data, safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def pokemon_create(request):
    try:
        payload = json.loads(request.body.decode("utf-8"))
    except json.JSONDecodeError:
        return JsonResponse({"error": "JSON non valido"}, status=400)

    # campi obbligatori
    if not payload.get("name") or not payload.get("type1"):
        return JsonResponse({"error": "name e type1 sono obbligatori"}, status=400)

    p = Pokemon.objects.create(
        name=payload["name"],
        type1=payload["type1"],
        type2=payload.get("type2"),
        level=payload.get("level", 1),
        hp=payload.get("hp", 10),
    )

    return JsonResponse(
        {
            "message": "Pokemon creato",
            "pokemon": {
                "id": p.id,
                "name": p.name,
                "type1": p.type1,
                "type2": p.type2,
                "level": p.level,
                "hp": p.hp,
            },
        },
        status=201,
    )


@csrf_exempt
@require_http_methods(["POST", "DELETE"])
def pokemon_delete(request):
    """
    Tranello: per cancellare devi indicare l'ID.
    Riceviamo {"id": 3} nel body.
    """
    try:
        payload = json.loads(request.body.decode("utf-8")) if request.body else {}
    except json.JSONDecodeError:
        return JsonResponse({"error": "JSON non valido"}, status=400)

    pokemon_id = payload.get("id")
    if not pokemon_id:
        return JsonResponse({"error": "Devi passare l'id del Pokemon"}, status=400)

    deleted_count, _ = Pokemon.objects.filter(id=pokemon_id).delete()

    if deleted_count == 0:
        return JsonResponse({"error": f"Nessun Pokemon con id={pokemon_id}"}, status=404)

    return JsonResponse({"message": f"Pokemon id={pokemon_id} cancellato"})
