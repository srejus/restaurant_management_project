from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework import status

# Create your views here.
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            # Delete the user's token
            request.user.auth_token.delete()
        except (AttributeError, Token.DoesNotExist):
            pass  # Token may already be deleted

        return Response({"detail": "Logged out successfully."}, status=status.HTTP_200_OK)