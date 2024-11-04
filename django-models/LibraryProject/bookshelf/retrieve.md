### Retrieve

```PY
from bookshelf.models import Book
book = Book.objects.get(id=1)
print(book)
# Expected output: <Book: 1984>
```