# -*- coding: utf-8 -*-
from plone.app.testing import TEST_USER_ID
from zope.component import queryUtility
from zope.component import createObject
from plone.app.testing import setRoles
from plone.dexterity.interfaces import IDexterityFTI
from plone import api

from cmcs.policy.testing import CMCS_POLICY_INTEGRATION_TESTING  # noqa
from cmcs.policy.interfaces import IWriting

import unittest2 as unittest


class WritingIntegrationTest(unittest.TestCase):

    layer = CMCS_POLICY_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='Writing')
        schema = fti.lookupSchema()
        self.assertEqual(IWriting, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='Writing')
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='Writing')
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(IWriting.providedBy(obj))

    def test_adding(self):
        self.portal.invokeFactory('Writing', 'Writing')
        self.assertTrue(
            IWriting.providedBy(self.portal['Writing'])
        )
