import pytest

from content_settings.models import ContentSetting
from content_settings.models import ContentSetting

pytestmark = [pytest.mark.django_db(transaction=True)]


def test_admin(webtest_admin):
    cs = ContentSetting.objects.get(name="RATINGS")
    resp = webtest_admin.get(f"/admin/content_settings/contentsetting/{cs.id}/change/")
    assert resp.status_int == 200

    resp.forms["contentsetting_form"]["value"] = "New Title"
    resp = resp.forms["contentsetting_form"].submit()
    assert resp.status_int == 302

    cs.refresh_from_db()
    assert cs.value == "New Title"
