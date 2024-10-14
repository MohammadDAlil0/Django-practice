from django.shortcuts import render
from django.http import JsonResponse
from .models import Inventory
from django.views.decorators.csrf import csrf_exempt
import json

def hello_world_view(request):
    return JsonResponse({
        "message": 'Hello world'
    })

def get_books(request):
    result = []
    books = Inventory.objects.all()
    for book in books: 
        data={
            "title": book.title,
            "price": book.price,
            "author": book.author
        }
        result.append(data)
    
    return JsonResponse({
        "books": result
    })

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Inventory  # Adjust this import based on your project structure

@csrf_exempt
def add_book(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            # Validate required fields
            required_fields = ["title", "isbn_id", "price", "publisher", "quantity", "author"]
            for field in required_fields:
                if field not in data:
                    return JsonResponse({
                        "error": f"Missing field: {field}"
                    }, status=400)

            # Create the book
            book = Inventory.objects.create(
                title=data["title"],
                isbn_id=data["isbn_id"],
                price=data["price"],
                publisher=data["publisher"],
                quantity=data["quantity"],
                author=data["author"]
            )

            print(book)

            # Serialize the book to a dictionary
            book_data = {
                "id": book.id,
                "title": book.title,
                "isbn_id": book.isbn_id,
                "price": book.price,
                "publisher": book.publisher,
                "quantity": book.quantity,
                "author": book.author,
            }

            return JsonResponse({
                "status": 'success',
                "data": book_data
            })

        except json.JSONDecodeError:
            return JsonResponse({
                "error": "Invalid JSON"
            }, status=400)
        except Exception as e:
            return JsonResponse({
                "error": str(e)
            }, status=500)

    else:
        return JsonResponse({
            "error": "Only POST method is allowed"
        }, status=405)
