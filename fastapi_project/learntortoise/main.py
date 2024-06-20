# Import necessary modules
from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.fastapi import register_tortoise
from fastapi import FastAPI

# Define your Tortoise ORM model
class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50, unique=True)
    password_hash = fields.CharField(max_length=128)

    def __str__(self):
        return self.username

# Configure FastAPI app
app = FastAPI()

# Register Tortoise ORM
register_tortoise(
    app,
    db_url='postgres://postgres:password123#@localhost:5432/tortoisedata',  # Replace with your PostgreSQL connection string
    modules={'models': ['User']},  # Module path where models are defined
    generate_schemas=True  # Automatically generate database schemas
)

# Example usage in FastAPI route handler
@app.post("/users/")
async def create_user(username: str, password: str):
    # Create a new user in the database
    new_user = await User.create(username=username, password_hash=hash_password(password))
    return {"id": new_user.id, "username": new_user.username}
