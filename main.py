from fastapi import FastAPI, Depends
from fastapi.security import OpenIdConnect

app = FastAPI()


oidc = OpenIdConnect(
    openIdConnectUrl="http://localhost:3001/oidc/.well-known/openid-configuration"
)


@app.get("/foo")
async def bar(token=Depends(oidc)):
    return token
