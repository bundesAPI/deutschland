from deutschland.presseportal import PresseportalApi
from deutschland.presseportal import Company, Entity, Story

presseportal = PresseportalApi("YOUR_KEY_HERE")

try:
    stories = presseportal.get_stories()
except Exception as e:
    print(str(e))
    assert str(e) == "The API returned error code 101 (authentification failed)."
