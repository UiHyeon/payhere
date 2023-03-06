from .models import Board
from .serializers import BoardSerializer
from rest_framework import generics

#ListCreateAPIView - 목록, 생성
class BoardAPI(generics.ListCreateAPIView):
    serializer_class = BoardSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    #로그인한 사용자의 가계부 리스트를 볼 수 있도록 조회.
    def get_queryset(self):
        return Board.objects.filter(author=self.request.user)

#RetrieveUpdateDestroyAPIView - 조회, 수정, 삭제
class BoardDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    #로그인한 사용자의 가계부 상세정보를 볼 수 있도록 조회.
    def get_queryset(self):
        return Board.objects.filter(author=self.request.user)
    

# 가계부의 세부 내역을 복제할 수 있습니다. -> 조건 미구현.
class BoardCopyAPI(generics.CreateAPIView):
    serializer_class = BoardSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        serializer.save(memo=self.request.user)
        serializer.save(price=self.request.user)

    #로그인한 사용자의 가계부 리스트를 볼 수 있도록 조회.
    def get_queryset(self):
        return Board.objects.filter(author=self.request.user, id = self.request.user)