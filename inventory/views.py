from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    """
    ViewSet yang menyediakan aksi CRUD lengkap untuk model Item.
    - POST /items/ -> Tambah item baru
    - GET /items/ -> List seluruh item
    - GET /items/<id>/ -> Detail item berdasarkan ID
    - PUT /items/<id>/ -> Update data/stat item secara penuh berdasarkan ID
    - PATCH /items/<id>/ -> Update sebagian data/stat item berdasarkan ID
    - DELETE /items/<id>/ -> Hapus item berdasarkan ID
    """
    queryset = Item.objects.all().order_by('-created_at')
    serializer_class = ItemSerializer
