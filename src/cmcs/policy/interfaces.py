# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from cmcs.policy import _
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from zope import schema
from zope.interface import Interface
from plone.autoform import directives
from z3c.form.browser.radio import RadioFieldWidget
from plone.namedfile.field import NamedBlobImage
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary

SeriesVocab = SimpleVocabulary(
    [SimpleTerm(value='s1', title=_(u'Statistical Series')),
     SimpleTerm(value='s2', title=_(u'Special Series')),
     SimpleTerm(value='s3', title=_(u'Miscellaneous Series')),
     SimpleTerm(value='s4', title=_(u'Service Series')),
     SimpleTerm(value='s5', title=_(u'Office Series')),
     SimpleTerm(value='s6', title=_(u'Inspectorate Series')),
     SimpleTerm(value='s7', title=_(u'Customs Publications Not Included in Any of the Foregoing Series')),
    ]
)

CtgrVocab = SimpleVocabulary(
    [SimpleTerm(value='c1', title=_(u'Chinese Maritime Custom Publications')),
     SimpleTerm(value='c2', title=_(u'China and West')),
     SimpleTerm(value='c3', title=_(u'The Directorate General of Customs')),
    ]
)

TypeVocab = SimpleVocabulary(
    [SimpleTerm(value='1st', title=_(u'Primary Materials')),
     SimpleTerm(value='2nd', title=_(u'Secondary Materials')),
    ]
)

LangVocab = SimpleVocabulary(
    [SimpleTerm(value='zh', title=_(u'Chinese')),
     SimpleTerm(value='en', title=_(u'English')),
     SimpleTerm(value='jp', title=_(u'Japanese')),
    ]
)

class ICmcsPolicyLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IWriting(Interface):

    title = schema.TextLine(
        title=_(u"Title"),
        required=True,
    )

    description = schema.Text(
        title=_(u"Description"),
        required=False,
    )

#   directives.widget(series=RadioFieldWidget)
    series = schema.Choice(
        title=_(u"Series"),
        required=False,
        vocabulary=SeriesVocab,
    )

    volume = schema.TextLine(
        title=_(u"Volume"),
        required=False,
    )

#   directives.widget(category=RadioFieldWidget)
    ctgr = schema.Choice(
        title=_(u"Category"),
        required=False,
        vocabulary=CtgrVocab,
    )

    mtrl = schema.Choice(
        title=_(u"Type"),
        required=False,
        vocabulary=TypeVocab,
    )

    lang = schema.Choice(
        title=_(u"Language"),
        required=False,
        vocabulary=LangVocab,
    )

    alo1 = schema.TextLine(
        title=_(u"Author 1 Original Last Name"),
        required=False,
    )

    afo1 = schema.TextLine(
        title=_(u"Author 1 Original First Name"),
        required=False,
    )

    alo2 = schema.TextLine(
        title=_(u"Author 2 Original Last Name"),
        required=False,
    )

    afo2 = schema.TextLine(
        title=_(u"Author 2 Original First Name"),
        required=False,
    )

    alo3 = schema.TextLine(
        title=_(u"Author 3 Original Last Name"),
        required=False,
    )

    afo3 = schema.TextLine(
        title=_(u"Author 3 Original First Name"),
        required=False,
    )

    lctn = schema.TextLine(
        title=_(u"Publishing Location"),
        required=False,
    )

    pber = schema.TextLine(
        title=_(u"Publisher"),
        required=False,
    )

    year = schema.TextLine(
        title=_(u"Publishing Year"),
        required=False,
    )

    image = NamedBlobImage(
        title=_(u"Lead Image"),
        description=_(u"Size: 800x530"),
        required=False,
    )

