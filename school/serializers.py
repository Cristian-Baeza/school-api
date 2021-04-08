from builtins import object

class StudentSerializer(object):
    def __init__(self, body):
        self.body = body

    @property
    def all_students(self):
        output = {'students': []}

        for each in self.body:
            student_details = {
                'id': each.id,
                'first_name': each.first_name,
                'last_name': each.last_name,
                'age': each.age
            }
            output['students'].append(student_details)

        return output
    
    @property
    def student_detail(self):
        return {
            'id': self.body.id,
            'first_name': self.body.first_name,
            'last_name': self.body.last_name,
            'age': self.body.age
        }