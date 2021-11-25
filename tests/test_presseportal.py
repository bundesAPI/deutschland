from deutschland.presseportal import Company, Entity, PresseportalApi, Story

presseportal = PresseportalApi("YOUR_KEY_HERE")

try:
    stories = presseportal.get_stories()
except Exception as e:
    print(str(e))
    assert str(e) == "The API returned error code 101 (authentification failed)."
