# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from cmcs.policy.testing import CMCS_POLICY_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that cmcs.policy is properly installed."""

    layer = CMCS_POLICY_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if cmcs.policy is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'cmcs.policy'))

    def test_browserlayer(self):
        """Test that ICmcsPolicyLayer is registered."""
        from cmcs.policy.interfaces import (
            ICmcsPolicyLayer)
        from plone.browserlayer import utils
        self.assertIn(ICmcsPolicyLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = CMCS_POLICY_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['cmcs.policy'])

    def test_product_uninstalled(self):
        """Test if cmcs.policy is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'cmcs.policy'))

    def test_browserlayer_removed(self):
        """Test that ICmcsPolicyLayer is removed."""
        from cmcs.policy.interfaces import ICmcsPolicyLayer
        from plone.browserlayer import utils
        self.assertNotIn(ICmcsPolicyLayer, utils.registered_layers())
