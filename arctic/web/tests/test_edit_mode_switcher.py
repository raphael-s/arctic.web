from ftw.builder import Builder
from ftw.builder import create
from ftw.testbrowser import browsing
from arctic.web.tests import FunctionalTestCase


class TestEditModeSwitcher(FunctionalTestCase):

    def setUp(self):
        super(TestEditModeSwitcher, self).setUp()
        self.grant('Manager')

    def document_is_editable(self, browser):
        return len(browser.css('.documentEditable')) > 0

    @browsing
    def test_edit_mode_is_enabled_by_default(self, browser):
        """
        This test makes sure that the edit mode is enabled by default, e.g.
        the users don't have to toggle the edit mode before the editing
        tools and actions appear.
        """
        page = create(Builder('sl content page'))
        browser.login().visit(page)
        self.assertTrue(self.document_is_editable(browser),
                        'Edit mode should be enabled by default.')

    @browsing
    def test_edit_mode_toggle_works(self, browser):
        """
        This test makes sure that the user is able to toggle the edit mode.
        """
        page = create(Builder('sl content page'))
        browser.login().visit(page)

        # Make sure the user can disable the edit mode.
        browser.find('Disable edit mode').click()
        self.assertFalse(self.document_is_editable(browser),
                         'The document must editable now.')

        # Make sure the user can enable the edit mode again.
        browser.find('Enable edit mode').click()
        self.assertTrue(self.document_is_editable(browser),
                        'The document must no longer be editable.')

    @browsing
    def test_byline_not_visible_when_edit_mode_disabled(self, browser):
        page = create(Builder('sl content page'))

        browser.login().visit(page)
        self.assertTrue(browser.css('#plone-document-byline'),
                        'Byline should be visible by default.')

        browser.find('Disable edit mode').click()
        self.assertFalse(browser.css('#plone-document-byline'),
                         'Byline should be hidden when disabling edit mode.')
