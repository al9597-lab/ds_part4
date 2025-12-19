from app.db import get_session
from sqlalchemy import text

session = get_session()

try:
    result = session.execute(text("SELECT 1;"))
    print("DB Connection OK")
    print("Result:", list(result))
except Exception as e:
    print("DB Connection FAILED")
    print(e)
finally:
    session.close()
