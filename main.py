from fastapi import FastAPI, Depends, Response, status
from fastapi.security import HTTPBearer

from utils import VerifyToken



token_auth_scheme = HTTPBearer()

app = FastAPI()



@app.get("/api/public")
def public():

	result = {
		"status":"success",
		"msg": (
			"Hello from a public endpoint! You don't need to be "
                "authenticated to see this.")
	}

	return result



@app.get("/api/private")
def private(response: Response, token: str = Depends(token_auth_scheme)):
	
	result = VerifyToken(token.credentials).verify()

	if result.get("status"):
		response.status_code = status.HTTP_400_BAD_REQUEST
		return result

	return result
