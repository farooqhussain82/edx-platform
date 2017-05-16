
from django.dispatch import receiver, Signal

# Signal that indicates that a course grading policy has been updated.
# This signal is generated when a grading policy change occurs within
# modulestore for either course or subsection changes.
GRADING_POLICY_CHANGED = Signal(
    providing_args=[
        'user_id',  # Integer User ID
        'course_id',  # Unicode string representing the course
    ]
)
