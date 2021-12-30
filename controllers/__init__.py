import random, string

from fastapi.responses import ORJSONResponse

from data import User, Token
from utils import get_password_hash

def random_string():

    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))

def parse(request):

  if request.method == "GET":
    args = request.path_params

  if request.method == "POST":
    args = request.json()

  return args


def create_response_ok(message, item=None):

  data = {}  
  data['message'] = message
  data['item'] = item
  data['status'] = 200
  return ORJSONResponse(content=data)


def create_response_bad(message, status=400,  item=None):

  data = {}  
  data['message'] = message
  data['item'] = item
  data['status'] = status
  return ORJSONResponse(content=data)


async def create_bulk_users(users, session):

  for _ in range(users):

    args = {}
    args['email'] = "{}@{}".format(random_string(), random_string())
    args['username'] = random_string()
    args['hashed_pass'] = get_password_hash(random_string())
    password = random_string()

    await User.AddNew(session, args)
    
  return True

