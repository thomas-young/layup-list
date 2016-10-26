from dal import autocomplete
from web.models import Course


class CourseAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Course.objects.all()

        if self.q:
            if len(self.q) <= 4:
                qs = qs.filter(department__istartswith=self.q[:3])
            elif 4 < len(self.q) <= 8 and self.q[4] == " ":
                qs = qs.filter(department__istartswith=self.q[:3])\
                    .filter(number__startswith=self.q[5:])
            elif 4 < len(self.q) <= 8 and self.q[4].isdigit():
                qs = qs.filter(department__istartswith=self.q[:3])\
                    .filter(number__startswith=self.q[4:])
            else:
                qs = qs.filter(title__icontains=self.q)

        return qs
