import unittest
from app.models import Comments, User
from app import db

class CommentsTest(unittest.TestCase):
    def setUp(self):
        self.user_jose=User(username='kevin', password='josephat', email = 'kevin@gmail.com')

        self.new_comment=Comments( pitch_id=1, comment='realy', user=self.user_jose)

    def tearDown(self):
        User.query.delete()
        Comments.query.delete()

    def check_instance_variables(self): 
        # self.assertEqual(self.new_pitch.title, 'jose')
        # self.assertEqual(self.new_pitch.description, 'race with time')
        # self.assertEqual(self.new_pitch.category, 'business')
        self.assertEqual(self.new_comment.comment, 'realy')
        # self.assertEqual(self.new_pitch.user, self.user_jose)
        self.assertEqual(self.new_comment.pitch_id, 1)
        

    def test_save_comments(self):
        self.new_comment.save_comments()
        self.assertTrue(len(Comments.query.all())>0)

    def test_get_comments(self):
        self.new_comment.save_comments()
        got_comments= Comments.get_comments(1)
        self.assertTrue(len(got_comments)>0)