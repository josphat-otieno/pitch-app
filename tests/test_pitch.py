import unittest
from app.models import Pitch, User

class PitchTest(unittest.TestCase):
    def setUp(self):
        self.user_jose=User(username='oti', password='josephat', email='josiah@gmail.com')
        self.new_pitch=Pitch(title='jose', description='race with time', category='business', user=self.user_jose)

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEqual(self.new_pitch.title, 'jose')
        self.assertEqual(self.new_pitch.description, 'race with time')
        self.assertEqual(self.new_pitch.category, 'business')
        self.assertEqual(self.new_pitch.user, self.user_jose)
        
    def test_get_pitches_by_category(self):
        self.new_pitch.save_pitch()
        got_pitches=Pitch.get_pitches('busiess')
        self.assertTrue(len(got_pitches)>0)

    def test_save_pitches(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)