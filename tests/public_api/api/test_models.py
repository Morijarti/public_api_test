# pylint: disable=invalid-name, unused-argument
from opt_out.public_api.api.models import URL, Submission


def create_submission():
    first = Submission()
    first.identity = "female"
    first.age = 20
    first.interaction = "A little"

    second = Submission()
    second.identity = "trans"
    second.age = 95
    second.interaction = "A lot"

    return first, second


def test_save_identity(db):
    first, second = create_submission()
    first.save()

    second.save()

    submissions = Submission.objects.all()
    assert submissions.count() == 2

    assert submissions[0].identity == "female"
    assert submissions[1].identity == "trans"


def test_save_age(db):
    first, second = create_submission()
    first.save()

    second.save()

    submissions = Submission.objects.all()
    assert submissions[0].age == "20"
    assert submissions[1].age == "95"


def test_save_interaction(db):
    first, second = create_submission()
    first.save()

    second.save()

    submissions = Submission.objects.all()
    assert submissions[0].interaction == "A little"
    assert submissions[1].interaction == "A lot"


def test_save_selfsubmission(db):
    first = Submission()
    first.save()

    second = Submission()
    second.self_submission = False
    second.save()

    submissions = Submission.objects.all()
    assert submissions.count() == 2

    assert submissions[0].self_submission
    assert not submissions[1].self_submission


def create_url():
    submission = Submission()
    submission.save()

    first = URL()
    first.url = "https://test1.url"
    first.submission = submission

    second = URL()
    second.url = "https://test2.url"
    second.submission = submission

    return first, second


def test_save_id(db):
    first, second = create_url()
    first.save()
    second.save()

    retrieved_comments = URL.objects.all()

    assert retrieved_comments[0].id == 1
    assert retrieved_comments[1].id == 2


def test_save_urls(db):
    first, second = create_url()
    first.save()
    second.save()

    retrieved_comments = URL.objects.all()
    assert retrieved_comments.count() == 2

    assert retrieved_comments[0].url == "https://test1.url"
    assert retrieved_comments[1].url == "https://test2.url"
