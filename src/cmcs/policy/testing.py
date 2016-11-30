# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import cmcs.policy


class CmcsPolicyLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=cmcs.policy)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'cmcs.policy:default')


CMCS_POLICY_FIXTURE = CmcsPolicyLayer()


CMCS_POLICY_INTEGRATION_TESTING = IntegrationTesting(
    bases=(CMCS_POLICY_FIXTURE,),
    name='CmcsPolicyLayer:IntegrationTesting'
)


CMCS_POLICY_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(CMCS_POLICY_FIXTURE,),
    name='CmcsPolicyLayer:FunctionalTesting'
)


CMCS_POLICY_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        CMCS_POLICY_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CmcsPolicyLayer:AcceptanceTesting'
)
