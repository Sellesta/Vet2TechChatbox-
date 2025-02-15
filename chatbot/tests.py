from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Subject, Question, UserPerformance, EntranceExam, CourseCompletion

class SubjectModelTest(TestCase):
    def test_create_subject(self):
        subject = Subject.objects.create(name="Math")
        self.assertEqual(str(subject), "Math")

class QuestionModelTest(TestCase):
    def setUp(self):
        self.subject = Subject.objects.create(name="Science")

    def test_create_question(self):
        question = Question.objects.create(
            subject=self.subject,
            question_text="What is the atomic number of Oxygen?",
            option_a="6",
            option_b="7",
            option_c="8",
            option_d="9",
            correct_option="C",
            difficulty=2
        )
        self.assertEqual(str(question), "What is the atomic number of Oxygen?")
        self.assertEqual(question.correct_option, "C")

class UserPerformanceTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser")
        self.subject = Subject.objects.create(name="History")

    def test_user_performance(self):
        performance = UserPerformance.objects.create(
            user=self.user,
            subject=self.subject,
            total_attempts=10,
            correct_attempts=7
        )
        self.assertAlmostEqual(performance.accuracy(), 0.7)

class EntranceExamTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="examuser")

    def test_entrance_exam_score(self):
        exam = EntranceExam.objects.create(user=self.user, score=85)
        self.assertEqual(exam.score, 85)

class CourseCompletionTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="courseuser")

    def test_course_completion(self):
        course = CourseCompletion.objects.create(user=self.user, completed=True)
        self.assertTrue(course.completed)
