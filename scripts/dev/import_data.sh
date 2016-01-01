#!/bin/bash
# Call this from root directory of repo

python manage.py migrate

# import from ORC
python scripts/importers/import_orc_courses.py

# import course pages
python scripts/importers/import_course_pages.py

# import term data
python scripts/importers/import_term.py 16W data/terms/201601_courses.json

# import medians
python scripts/importers/import_medians.py

# import reviews
python scripts/importers/import_layups_as_reviews.py
python scripts/importers/import_reviews.py

# compute the initial scorings
python scripts/compute/compute_initial_scores.py
