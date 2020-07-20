from tethys_sdk.base import TethysAppBase, url_map_maker
from tethys_sdk.app_settings import CustomSetting


class TestApp(TethysAppBase):
    """
    Tethys app class for Test App.
    """

    name = 'Test App'
    index = 'test_app:home'
    icon = 'test_app/images/icon.gif'
    package = 'test_app'
    root_url = 'test-app'
    color = '#d35400'
    description = ''
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='test-app',
                controller='test_app.controllers.home'
            ),
        )

        return url_maps

    def custom_settings(self):
        return CustomSetting(
            name='test_setting',
            type=CustomSetting.TYPE_STRING,
            description='test_setting',
            required=False
        )
