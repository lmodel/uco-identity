# Auto generated from uco_identity.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-04-11T23:45:46
# Schema: uco-identity
#
# id: https://w3id.org/lmodel/uco-identity
# description:
# license: https://www.apache.org/licenses/LICENSE-2.0

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Boolean, Datetime, Decimal, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, Decimal, URIorCURIE, XSDDateTime

metamodel_version = "1.7.0"
version = "1.1.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BFO = CurieNamespace('BFO', 'http://purl.obolibrary.org/obo/BFO_')
CSO = CurieNamespace('CSO', 'https://cso.kmi.open.ac.uk/topics/')
GSSO = CurieNamespace('GSSO', 'http://purl.obolibrary.org/obo/GSSO_')
IAO = CurieNamespace('IAO', 'http://purl.obolibrary.org/obo/IAO_')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
REPR = CurieNamespace('REPR', 'https://w3id.org/reproduceme#')
SEPIO = CurieNamespace('SEPIO', 'http://purl.obolibrary.org/obo/SEPIO_')
SIO = CurieNamespace('SIO', 'http://identifiers.org/sio/')
WIKIDATA = CurieNamespace('WIKIDATA', 'http://identifiers.org/wikidata/')
CORE = CurieNamespace('core', 'https://w3id.org/lmodel/uco-core/')
CSRC = CurieNamespace('csrc', 'https://csrc.nist.gov/glossary/term/')
DCID = CurieNamespace('dcid', 'https://datacommons.org/browser/')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
GR = CurieNamespace('gr', 'http://purl.org/goodrelations/v1#')
IDENTITY = CurieNamespace('identity', 'https://w3id.org/lmodel/uco-identity/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
LM_CORE = CurieNamespace('lm_core', 'https://w3id.org/lmodel/core/')
LOCATION = CurieNamespace('location', 'https://w3id.org/lmodel/uco-location/')
OM = CurieNamespace('om', 'http://www.ontology-of-units-of-measure.org/resource/om-2/')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SCHEMA_UCO_CORE = CurieNamespace('schema_uco_core', 'https://w3id.org/lmodel/uco-core/schema/')
SCHEMA_UCO_LOCATION = CurieNamespace('schema_uco_location', 'https://w3id.org/lmodel/uco-location/schema/')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
SUMO = CurieNamespace('sumo', 'https://w3id.org/sumo/kb/')
WIKIDATA = CurieNamespace('wikidata', 'http://identifiers.org/wikidata/')
WIKIDATA_PROPERTY = CurieNamespace('wikidata_property', 'https://www.wikidata.org/wiki/Property:')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = IDENTITY


# Types
class StringType(String):
    """ A string """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "string type"
    type_model_uri = IDENTITY.StringType


class LiteralType(String):
    """ Literals are used for values such as strings, numbers, and dates. """
    type_class_uri = RDF.literal
    type_class_curie = "rdf:literal"
    type_name = "literal type"
    type_model_uri = IDENTITY.LiteralType


class NonNegativeIntegerType(Integer):
    """ real number strictly greater than zero """
    type_class_uri = XSD.nonNegativeInteger
    type_class_curie = "xsd:nonNegativeInteger"
    type_name = "non negative integer type"
    type_model_uri = IDENTITY.NonNegativeIntegerType


class StatementType(StringType):
    """ "meaningful declarative sentence that is either true or false, or that which a true or false declarative sentence asserts" """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "statement type"
    type_model_uri = IDENTITY.StatementType


class IriType(Uriorcurie):
    """ A IRI """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "iri type"
    type_model_uri = IDENTITY.IriType


class BooleanType(Boolean):
    """ A boolean value """
    type_class_uri = XSD.boolean
    type_class_curie = "xsd:boolean"
    type_name = "boolean type"
    type_model_uri = IDENTITY.BooleanType


class HexBinaryType(hex):
    """ "Represents arbitrary hex-encoded binary data" """
    type_class_uri = XSD.hexBinary
    type_class_curie = "xsd:hexBinary"
    type_name = "hex binary type"
    type_model_uri = IDENTITY.HexBinaryType


class DecimalType(Decimal):
    type_class_uri = XSD.decimal
    type_class_curie = "xsd:decimal"
    type_name = "decimal type"
    type_model_uri = IDENTITY.DecimalType


# Class references



class UcoThing(YAMLRoot):
    """
    UcoThing is the top-level class within UCO.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.UcoThing
    class_class_curie: ClassVar[str] = "core:UcoThing"
    class_name: ClassVar[str] = "UcoThing"
    class_model_uri: ClassVar[URIRef] = IDENTITY.UcoThing


class UcoInherentCharacterizationThing(UcoThing):
    """
    A UCO inherent characterization thing is a grouping of characteristics unique to a particular inherent aspect of a
    UCO domain object.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.UcoInherentCharacterizationThing
    class_class_curie: ClassVar[str] = "core:UcoInherentCharacterizationThing"
    class_name: ClassVar[str] = "UcoInherentCharacterizationThing"
    class_model_uri: ClassVar[URIRef] = IDENTITY.UcoInherentCharacterizationThing


@dataclass
class ExternalReference(UcoInherentCharacterizationThing):
    """
    Characteristics of a reference to a resource outside of the UCO.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.ExternalReference
    class_class_curie: ClassVar[str] = "core:ExternalReference"
    class_name: ClassVar[str] = "ExternalReference"
    class_model_uri: ClassVar[URIRef] = IDENTITY.ExternalReference

    referenceURL: Optional[Union[str, IriType]] = None
    definingContext: Optional[str] = None
    externalIdentifier: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.referenceURL is not None and not isinstance(self.referenceURL, IriType):
            self.referenceURL = IriType(self.referenceURL)

        if self.definingContext is not None and not isinstance(self.definingContext, str):
            self.definingContext = str(self.definingContext)

        if self.externalIdentifier is not None and not isinstance(self.externalIdentifier, str):
            self.externalIdentifier = str(self.externalIdentifier)

        super().__post_init__(**kwargs)


class Facet(UcoInherentCharacterizationThing):
    """
    A facet is a grouping of characteristics singularly unique to a particular inherent aspect of a UCO domain object.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Facet
    class_class_curie: ClassVar[str] = "core:Facet"
    class_name: ClassVar[str] = "Facet"
    class_model_uri: ClassVar[URIRef] = IDENTITY.Facet


class IdentityFacet(Facet):
    """
    An IdentityFacet is a grouping of characteristics unique to a particular aspect of an identity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IDENTITY.IdentityFacet
    class_class_curie: ClassVar[str] = "identity:IdentityFacet"
    class_name: ClassVar[str] = "IdentityFacet"
    class_model_uri: ClassVar[URIRef] = IDENTITY.IdentityFacet


@dataclass
class AddressFacet(IdentityFacet):
    """
    An Address Facet is a grouping of characteristics unique to an administrative identifier for a geolocation
    associated with a specific identity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IDENTITY.AddressFacet
    class_class_curie: ClassVar[str] = "identity:AddressFacet"
    class_name: ClassVar[str] = "AddressFacet"
    class_model_uri: ClassVar[URIRef] = IDENTITY.AddressFacet

    address: Optional[Union[dict, "Location"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.address is not None and not isinstance(self.address, Location):
            self.address = Location(**as_dict(self.address))

        super().__post_init__(**kwargs)


class AffiliationFacet(IdentityFacet):
    """
    An affiliation is a grouping of characteristics unique to the established affiliations of an entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IDENTITY.AffiliationFacet
    class_class_curie: ClassVar[str] = "identity:AffiliationFacet"
    class_name: ClassVar[str] = "AffiliationFacet"
    class_model_uri: ClassVar[URIRef] = IDENTITY.AffiliationFacet


@dataclass
class BirthInformationFacet(IdentityFacet):
    """
    Birth information is a grouping of characteristics unique to information pertaining to the birth of an entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IDENTITY.BirthInformationFacet
    class_class_curie: ClassVar[str] = "identity:BirthInformationFacet"
    class_name: ClassVar[str] = "BirthInformationFacet"
    class_model_uri: ClassVar[URIRef] = IDENTITY.BirthInformationFacet

    birthdate: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.birthdate is not None and not isinstance(self.birthdate, XSDDateTime):
            self.birthdate = XSDDateTime(self.birthdate)

        super().__post_init__(**kwargs)


class CountryOfResidenceFacet(IdentityFacet):
    """
    Country of residence is a grouping of characteristics unique to information related to the country, or countries,
    where an entity resides.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IDENTITY.CountryOfResidenceFacet
    class_class_curie: ClassVar[str] = "identity:CountryOfResidenceFacet"
    class_name: ClassVar[str] = "CountryOfResidenceFacet"
    class_model_uri: ClassVar[URIRef] = IDENTITY.CountryOfResidenceFacet


class EventsFacet(IdentityFacet):
    """
    Events is a grouping of characteristics unique to information related to specific relevant things that happen in
    the lifetime of an entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IDENTITY.EventsFacet
    class_class_curie: ClassVar[str] = "identity:EventsFacet"
    class_name: ClassVar[str] = "EventsFacet"
    class_model_uri: ClassVar[URIRef] = IDENTITY.EventsFacet


class IdentifierFacet(IdentityFacet):
    """
    Identifier is a grouping of characteristics unique to information that uniquely and specifically identities an
    entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IDENTITY.IdentifierFacet
    class_class_curie: ClassVar[str] = "identity:IdentifierFacet"
    class_name: ClassVar[str] = "IdentifierFacet"
    class_model_uri: ClassVar[URIRef] = IDENTITY.IdentifierFacet


class LanguagesFacet(IdentityFacet):
    """
    Languages is a grouping of characteristics unique to specific syntactically and grammatically standardized forms
    of communication (human or computer) in which an entity has proficiency (comprehends, speaks, reads, or writes).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IDENTITY.LanguagesFacet
    class_class_curie: ClassVar[str] = "identity:LanguagesFacet"
    class_name: ClassVar[str] = "LanguagesFacet"
    class_model_uri: ClassVar[URIRef] = IDENTITY.LanguagesFacet


class NationalityFacet(IdentityFacet):
    """
    Nationality is a grouping of characteristics unique to the condition of an entity belonging to a particular nation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IDENTITY.NationalityFacet
    class_class_curie: ClassVar[str] = "identity:NationalityFacet"
    class_name: ClassVar[str] = "NationalityFacet"
    class_model_uri: ClassVar[URIRef] = IDENTITY.NationalityFacet


class OccupationFacet(IdentityFacet):
    """
    Occupation is a grouping of characteristics unique to the job or profession of an entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IDENTITY.OccupationFacet
    class_class_curie: ClassVar[str] = "identity:OccupationFacet"
    class_name: ClassVar[str] = "OccupationFacet"
    class_model_uri: ClassVar[URIRef] = IDENTITY.OccupationFacet


class OrganizationDetailsFacet(IdentityFacet):
    """
    Organization details is a grouping of characteristics unique to an identity representing an administrative and
    functional structure.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IDENTITY.OrganizationDetailsFacet
    class_class_curie: ClassVar[str] = "identity:OrganizationDetailsFacet"
    class_name: ClassVar[str] = "OrganizationDetailsFacet"
    class_model_uri: ClassVar[URIRef] = IDENTITY.OrganizationDetailsFacet


class PersonalDetailsFacet(IdentityFacet):
    """
    Personal details is a grouping of characteristics unique to an identity representing an individual person.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IDENTITY.PersonalDetailsFacet
    class_class_curie: ClassVar[str] = "identity:PersonalDetailsFacet"
    class_name: ClassVar[str] = "PersonalDetailsFacet"
    class_model_uri: ClassVar[URIRef] = IDENTITY.PersonalDetailsFacet


class PhysicalInfoFacet(IdentityFacet):
    """
    Physical info is a grouping of characteristics unique to the outwardly observable nature of an individual person.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IDENTITY.PhysicalInfoFacet
    class_class_curie: ClassVar[str] = "identity:PhysicalInfoFacet"
    class_name: ClassVar[str] = "PhysicalInfoFacet"
    class_model_uri: ClassVar[URIRef] = IDENTITY.PhysicalInfoFacet


class QualificationFacet(IdentityFacet):
    """
    Qualification is a grouping of characteristics unique to particular skills, capabilities or their related
    achievements (educational, professional, etc.) of an entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IDENTITY.QualificationFacet
    class_class_curie: ClassVar[str] = "identity:QualificationFacet"
    class_name: ClassVar[str] = "QualificationFacet"
    class_model_uri: ClassVar[URIRef] = IDENTITY.QualificationFacet


class RelatedIdentityFacet(IdentityFacet):
    """
    <Needs fleshed out from CIQ>
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IDENTITY.RelatedIdentityFacet
    class_class_curie: ClassVar[str] = "identity:RelatedIdentityFacet"
    class_name: ClassVar[str] = "RelatedIdentityFacet"
    class_model_uri: ClassVar[URIRef] = IDENTITY.RelatedIdentityFacet


@dataclass
class SimpleNameFacet(IdentityFacet):
    """
    A simple name facet is a grouping of characteristics unique to the personal name (e.g., Dr. John Smith Jr.) held
    by an identity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IDENTITY.SimpleNameFacet
    class_class_curie: ClassVar[str] = "identity:SimpleNameFacet"
    class_name: ClassVar[str] = "SimpleNameFacet"
    class_model_uri: ClassVar[URIRef] = IDENTITY.SimpleNameFacet

    familyName: Optional[Union[str, List[str]]] = empty_list()
    givenName: Optional[Union[str, List[str]]] = empty_list()
    honorificPrefix: Optional[Union[str, List[str]]] = empty_list()
    honorificSuffix: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.familyName, list):
            self.familyName = [self.familyName] if self.familyName is not None else []
        self.familyName = [v if isinstance(v, str) else str(v) for v in self.familyName]

        if not isinstance(self.givenName, list):
            self.givenName = [self.givenName] if self.givenName is not None else []
        self.givenName = [v if isinstance(v, str) else str(v) for v in self.givenName]

        if not isinstance(self.honorificPrefix, list):
            self.honorificPrefix = [self.honorificPrefix] if self.honorificPrefix is not None else []
        self.honorificPrefix = [v if isinstance(v, str) else str(v) for v in self.honorificPrefix]

        if not isinstance(self.honorificSuffix, list):
            self.honorificSuffix = [self.honorificSuffix] if self.honorificSuffix is not None else []
        self.honorificSuffix = [v if isinstance(v, str) else str(v) for v in self.honorificSuffix]

        super().__post_init__(**kwargs)


class VisaFacet(IdentityFacet):
    """
    Visa is a grouping of characteristics unique to information related to a person's ability to enter, leave, or stay
    for a specified period of time in a country.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IDENTITY.VisaFacet
    class_class_curie: ClassVar[str] = "identity:VisaFacet"
    class_name: ClassVar[str] = "VisaFacet"
    class_model_uri: ClassVar[URIRef] = IDENTITY.VisaFacet


@dataclass
class ConfidenceFacet(Facet):
    """
    A confidence is a grouping of characteristics unique to an asserted level of certainty in the accuracy of some
    information.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.ConfidenceFacet
    class_class_curie: ClassVar[str] = "core:ConfidenceFacet"
    class_name: ClassVar[str] = "ConfidenceFacet"
    class_model_uri: ClassVar[URIRef] = IDENTITY.ConfidenceFacet

    confidence: Union[int, NonNegativeIntegerType] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.confidence):
            self.MissingRequiredField("confidence")
        if not isinstance(self.confidence, NonNegativeIntegerType):
            self.confidence = NonNegativeIntegerType(self.confidence)

        super().__post_init__(**kwargs)


@dataclass
class UcoObject(UcoThing):
    """
    A UCO object is a representation of a fundamental concept either directly inherent to the cyber domain or
    indirectly related to the cyber domain and necessary for contextually characterizing cyber domain concepts and
    relationships. Within the Unified Cyber Ontology (UCO) structure this is the base class acting as a consistent,
    unifying and interoperable foundation for all explicit and inter-relatable content objects.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.UcoObject
    class_class_curie: ClassVar[str] = "core:UcoObject"
    class_name: ClassVar[str] = "UcoObject"
    class_model_uri: ClassVar[URIRef] = IDENTITY.UcoObject

    createdBy: Optional[str] = None
    description: Optional[Union[str, List[str]]] = empty_list()
    externalReference: Optional[Union[str, List[str]]] = empty_list()
    hasFacet: Optional[Union[str, List[str]]] = empty_list()
    modifiedTime: Optional[Union[Union[str, XSDDateTime], List[Union[str, XSDDateTime]]]] = empty_list()
    name: Optional[str] = None
    objectMarking: Optional[Union[Union[dict, MarkingDefinitionAbstraction], List[Union[dict, MarkingDefinitionAbstraction]]]] = empty_list()
    objectCreatedTime: Optional[Union[str, XSDDateTime]] = None
    specVersion: Optional[str] = None
    tag: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.createdBy is not None and not isinstance(self.createdBy, str):
            self.createdBy = str(self.createdBy)

        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        if not isinstance(self.externalReference, list):
            self.externalReference = [self.externalReference] if self.externalReference is not None else []
        self.externalReference = [v if isinstance(v, str) else str(v) for v in self.externalReference]

        if not isinstance(self.hasFacet, list):
            self.hasFacet = [self.hasFacet] if self.hasFacet is not None else []
        self.hasFacet = [v if isinstance(v, str) else str(v) for v in self.hasFacet]

        if not isinstance(self.modifiedTime, list):
            self.modifiedTime = [self.modifiedTime] if self.modifiedTime is not None else []
        self.modifiedTime = [v if isinstance(v, XSDDateTime) else XSDDateTime(v) for v in self.modifiedTime]

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.objectMarking, list):
            self.objectMarking = [self.objectMarking] if self.objectMarking is not None else []
        self.objectMarking = [v if isinstance(v, MarkingDefinitionAbstraction) else MarkingDefinitionAbstraction(**as_dict(v)) for v in self.objectMarking]

        if self.objectCreatedTime is not None and not isinstance(self.objectCreatedTime, XSDDateTime):
            self.objectCreatedTime = XSDDateTime(self.objectCreatedTime)

        if self.specVersion is not None and not isinstance(self.specVersion, str):
            self.specVersion = str(self.specVersion)

        if not isinstance(self.tag, list):
            self.tag = [self.tag] if self.tag is not None else []
        self.tag = [v if isinstance(v, str) else str(v) for v in self.tag]

        super().__post_init__(**kwargs)


@dataclass
class Assertion(UcoObject):
    """
    An assertion is a statement declared to be true.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Assertion
    class_class_curie: ClassVar[str] = "core:Assertion"
    class_name: ClassVar[str] = "Assertion"
    class_model_uri: ClassVar[URIRef] = IDENTITY.Assertion

    statement: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.statement, list):
            self.statement = [self.statement] if self.statement is not None else []
        self.statement = [v if isinstance(v, str) else str(v) for v in self.statement]

        super().__post_init__(**kwargs)


@dataclass
class Annotation(Assertion):
    """
    An annotation is an assertion made in relation to one or more objects.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Annotation
    class_class_curie: ClassVar[str] = "core:Annotation"
    class_name: ClassVar[str] = "Annotation"
    class_model_uri: ClassVar[URIRef] = IDENTITY.Annotation

    object: Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, list):
            self.object = [self.object] if self.object is not None else []
        self.object = [v if isinstance(v, UcoObject) else UcoObject(**as_dict(v)) for v in self.object]

        super().__post_init__(**kwargs)


@dataclass
class AttributedName(UcoObject):
    """
    An attributed name is a name of an entity issued by some attributed naming authority.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.AttributedName
    class_class_curie: ClassVar[str] = "core:AttributedName"
    class_name: ClassVar[str] = "AttributedName"
    class_model_uri: ClassVar[URIRef] = IDENTITY.AttributedName

    namingAuthority: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.namingAuthority is not None and not isinstance(self.namingAuthority, str):
            self.namingAuthority = str(self.namingAuthority)

        super().__post_init__(**kwargs)


class Compilation(UcoObject):
    """
    A compilation is a grouping of things.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Compilation
    class_class_curie: ClassVar[str] = "core:Compilation"
    class_name: ClassVar[str] = "Compilation"
    class_model_uri: ClassVar[URIRef] = IDENTITY.Compilation


@dataclass
class ContextualCompilation(Compilation):
    """
    A contextual compilation is a grouping of things sharing some context (e.g., a set of network connections observed
    on a given day, all accounts associated with a given person).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.ContextualCompilation
    class_class_curie: ClassVar[str] = "core:ContextualCompilation"
    class_name: ClassVar[str] = "ContextualCompilation"
    class_model_uri: ClassVar[URIRef] = IDENTITY.ContextualCompilation

    object: Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, list):
            self.object = [self.object] if self.object is not None else []
        self.object = [v if isinstance(v, UcoObject) else UcoObject(**as_dict(v)) for v in self.object]

        super().__post_init__(**kwargs)


@dataclass
class ControlledVocabulary(UcoObject):
    """
    A controlled vocabulary is an explicitly constrained set of string values.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.ControlledVocabulary
    class_class_curie: ClassVar[str] = "core:ControlledVocabulary"
    class_name: ClassVar[str] = "ControlledVocabulary"
    class_model_uri: ClassVar[URIRef] = IDENTITY.ControlledVocabulary

    value: str = None
    constrainingVocabularyReference: Optional[Union[str, IriType]] = None
    constrainingVocabularyName: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        if self.constrainingVocabularyReference is not None and not isinstance(self.constrainingVocabularyReference, IriType):
            self.constrainingVocabularyReference = IriType(self.constrainingVocabularyReference)

        if self.constrainingVocabularyName is not None and not isinstance(self.constrainingVocabularyName, str):
            self.constrainingVocabularyName = str(self.constrainingVocabularyName)

        super().__post_init__(**kwargs)


@dataclass
class EnclosingCompilation(Compilation):
    """
    An enclosing compilation is a container for a grouping of things.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.EnclosingCompilation
    class_class_curie: ClassVar[str] = "core:EnclosingCompilation"
    class_name: ClassVar[str] = "EnclosingCompilation"
    class_model_uri: ClassVar[URIRef] = IDENTITY.EnclosingCompilation

    object: Optional[Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.object, list):
            self.object = [self.object] if self.object is not None else []
        self.object = [v if isinstance(v, UcoObject) else UcoObject(**as_dict(v)) for v in self.object]

        super().__post_init__(**kwargs)


class Bundle(EnclosingCompilation):
    """
    A bundle is a container for a grouping of UCO content with no presumption of shared context.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Bundle
    class_class_curie: ClassVar[str] = "core:Bundle"
    class_name: ClassVar[str] = "Bundle"
    class_model_uri: ClassVar[URIRef] = IDENTITY.Bundle


@dataclass
class Grouping(ContextualCompilation):
    """
    A grouping is a compilation of referenced UCO content with a shared context.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Grouping
    class_class_curie: ClassVar[str] = "core:Grouping"
    class_name: ClassVar[str] = "Grouping"
    class_model_uri: ClassVar[URIRef] = IDENTITY.Grouping

    object: Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]] = None
    context: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.context, list):
            self.context = [self.context] if self.context is not None else []
        self.context = [v if isinstance(v, str) else str(v) for v in self.context]

        super().__post_init__(**kwargs)


class IdentityAbstraction(UcoObject):
    """
    An identity abstraction is a grouping of identifying characteristics unique to an individual or organization. This
    class is an ontological structural abstraction for this concept. Implementations of this concept should utilize
    the identity:Identity class.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.IdentityAbstraction
    class_class_curie: ClassVar[str] = "core:IdentityAbstraction"
    class_name: ClassVar[str] = "IdentityAbstraction"
    class_model_uri: ClassVar[URIRef] = IDENTITY.IdentityAbstraction


class Identity(IdentityAbstraction):
    """
    An identity is a grouping of identifying characteristics unique to an individual or organization.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IDENTITY.Identity
    class_class_curie: ClassVar[str] = "identity:Identity"
    class_name: ClassVar[str] = "Identity"
    class_model_uri: ClassVar[URIRef] = IDENTITY.Identity


class Organization(Identity):
    """
    An organization is a grouping of identifying characteristics unique to a group of people who work together in an
    organized way for a shared purpose. [based on https://dictionary.cambridge.org/us/dictionary/english/organization]
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IDENTITY.Organization
    class_class_curie: ClassVar[str] = "identity:Organization"
    class_name: ClassVar[str] = "Organization"
    class_model_uri: ClassVar[URIRef] = IDENTITY.Organization


class Person(Identity):
    """
    A person is a grouping of identifying characteristics unique to a human being regarded as an individual. [based on
    https://www.lexico.com/en/definition/person]
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IDENTITY.Person
    class_class_curie: ClassVar[str] = "identity:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = IDENTITY.Person


class Item(UcoObject):
    """
    An item is a distinct article or unit.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Item
    class_class_curie: ClassVar[str] = "core:Item"
    class_name: ClassVar[str] = "Item"
    class_model_uri: ClassVar[URIRef] = IDENTITY.Item


class MarkingDefinitionAbstraction(UcoObject):
    """
    A marking definition abstraction is a grouping of characteristics unique to the expression of a specific data
    marking conveying restrictions, permissions, and other guidance for how marked data can be used and shared. This
    class is an ontological structural abstraction for this concept. Implementations of this concept should utilize
    the marking MarkingDefinition class.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.MarkingDefinitionAbstraction
    class_class_curie: ClassVar[str] = "core:MarkingDefinitionAbstraction"
    class_name: ClassVar[str] = "MarkingDefinitionAbstraction"
    class_model_uri: ClassVar[URIRef] = IDENTITY.MarkingDefinitionAbstraction


class ModusOperandi(UcoObject):
    """
    A modus operandi is a particular method of operation (how a particular entity behaves or the resources they use).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.ModusOperandi
    class_class_curie: ClassVar[str] = "core:ModusOperandi"
    class_name: ClassVar[str] = "ModusOperandi"
    class_model_uri: ClassVar[URIRef] = IDENTITY.ModusOperandi


@dataclass
class Relationship(UcoObject):
    """
    A relationship is a grouping of characteristics unique to an assertion that one or more objects are related to
    another object in some way.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Relationship
    class_class_curie: ClassVar[str] = "core:Relationship"
    class_name: ClassVar[str] = "Relationship"
    class_model_uri: ClassVar[URIRef] = IDENTITY.Relationship

    isDirectional: Union[bool, BooleanType] = None
    source: Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]] = None
    target: Union[dict, "UcoObject"] = None
    endTime: Optional[Union[Union[str, XSDDateTime], List[Union[str, XSDDateTime]]]] = empty_list()
    kindOfRelationship: Optional[str] = None
    startTime: Optional[Union[Union[str, XSDDateTime], List[Union[str, XSDDateTime]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.isDirectional):
            self.MissingRequiredField("isDirectional")
        if not isinstance(self.isDirectional, BooleanType):
            self.isDirectional = BooleanType(self.isDirectional)

        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, list):
            self.source = [self.source] if self.source is not None else []
        self.source = [v if isinstance(v, UcoObject) else UcoObject(**as_dict(v)) for v in self.source]

        if self._is_empty(self.target):
            self.MissingRequiredField("target")
        if not isinstance(self.target, UcoObject):
            self.target = UcoObject(**as_dict(self.target))

        if not isinstance(self.endTime, list):
            self.endTime = [self.endTime] if self.endTime is not None else []
        self.endTime = [v if isinstance(v, XSDDateTime) else XSDDateTime(v) for v in self.endTime]

        if self.kindOfRelationship is not None and not isinstance(self.kindOfRelationship, str):
            self.kindOfRelationship = str(self.kindOfRelationship)

        if not isinstance(self.startTime, list):
            self.startTime = [self.startTime] if self.startTime is not None else []
        self.startTime = [v if isinstance(v, XSDDateTime) else XSDDateTime(v) for v in self.startTime]

        super().__post_init__(**kwargs)


@dataclass
class GPSCoordinatesFacet(Facet):
    """
    A GPS coordinates facet is a grouping of characteristics unique to the expression of quantified dilution of
    precision (DOP) for an asserted set of geolocation coordinates typically associated with satellite navigation such
    as the Global Positioning System (GPS).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LOCATION.GPSCoordinatesFacet
    class_class_curie: ClassVar[str] = "location:GPSCoordinatesFacet"
    class_name: ClassVar[str] = "GPSCoordinatesFacet"
    class_model_uri: ClassVar[URIRef] = IDENTITY.GPSCoordinatesFacet

    hdop: Optional[Union[Decimal, DecimalType]] = None
    pdop: Optional[Union[Decimal, DecimalType]] = None
    tdop: Optional[Union[Decimal, DecimalType]] = None
    vdop: Optional[Union[Decimal, DecimalType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.hdop is not None and not isinstance(self.hdop, DecimalType):
            self.hdop = DecimalType(self.hdop)

        if self.pdop is not None and not isinstance(self.pdop, DecimalType):
            self.pdop = DecimalType(self.pdop)

        if self.tdop is not None and not isinstance(self.tdop, DecimalType):
            self.tdop = DecimalType(self.tdop)

        if self.vdop is not None and not isinstance(self.vdop, DecimalType):
            self.vdop = DecimalType(self.vdop)

        super().__post_init__(**kwargs)


@dataclass
class LatLongCoordinatesFacet(Facet):
    """
    A lat long coordinates facet is a grouping of characteristics unique to the expression of a geolocation as the
    intersection of specific latitude, longitude, and altitude values.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LOCATION.LatLongCoordinatesFacet
    class_class_curie: ClassVar[str] = "location:LatLongCoordinatesFacet"
    class_name: ClassVar[str] = "LatLongCoordinatesFacet"
    class_model_uri: ClassVar[URIRef] = IDENTITY.LatLongCoordinatesFacet

    altitude: Optional[Union[Decimal, DecimalType]] = None
    latitude: Optional[Union[Decimal, DecimalType]] = None
    longitude: Optional[Union[Decimal, DecimalType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.altitude is not None and not isinstance(self.altitude, DecimalType):
            self.altitude = DecimalType(self.altitude)

        if self.latitude is not None and not isinstance(self.latitude, DecimalType):
            self.latitude = DecimalType(self.latitude)

        if self.longitude is not None and not isinstance(self.longitude, DecimalType):
            self.longitude = DecimalType(self.longitude)

        super().__post_init__(**kwargs)


class Location(UcoObject):
    """
    A location is a geospatial place, site, or position.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LOCATION.Location
    class_class_curie: ClassVar[str] = "location:Location"
    class_name: ClassVar[str] = "Location"
    class_model_uri: ClassVar[URIRef] = IDENTITY.Location


@dataclass
class SimpleAddressFacet(Facet):
    """
    A simple address facet is a grouping of characteristics unique to a geolocation expressed as an administrative
    address.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LOCATION.SimpleAddressFacet
    class_class_curie: ClassVar[str] = "location:SimpleAddressFacet"
    class_name: ClassVar[str] = "SimpleAddressFacet"
    class_model_uri: ClassVar[URIRef] = IDENTITY.SimpleAddressFacet

    addressType: Optional[str] = None
    country: Optional[str] = None
    locality: Optional[str] = None
    postalCode: Optional[str] = None
    region: Optional[str] = None
    street: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.addressType is not None and not isinstance(self.addressType, str):
            self.addressType = str(self.addressType)

        if self.country is not None and not isinstance(self.country, str):
            self.country = str(self.country)

        if self.locality is not None and not isinstance(self.locality, str):
            self.locality = str(self.locality)

        if self.postalCode is not None and not isinstance(self.postalCode, str):
            self.postalCode = str(self.postalCode)

        if self.region is not None and not isinstance(self.region, str):
            self.region = str(self.region)

        if self.street is not None and not isinstance(self.street, str):
            self.street = str(self.street)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.address = Slot(uri=IDENTITY.address, name="address", curie=IDENTITY.curie('address'),
                   model_uri=IDENTITY.address, domain=None, range=Optional[Union[dict, Location]])

slots.birthdate = Slot(uri=IDENTITY.birthdate, name="birthdate", curie=IDENTITY.curie('birthdate'),
                   model_uri=IDENTITY.birthdate, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.familyName = Slot(uri=IDENTITY.familyName, name="familyName", curie=IDENTITY.curie('familyName'),
                   model_uri=IDENTITY.familyName, domain=None, range=Optional[str])

slots.givenName = Slot(uri=IDENTITY.givenName, name="givenName", curie=IDENTITY.curie('givenName'),
                   model_uri=IDENTITY.givenName, domain=None, range=Optional[str])

slots.honorificPrefix = Slot(uri=IDENTITY.honorificPrefix, name="honorificPrefix", curie=IDENTITY.curie('honorificPrefix'),
                   model_uri=IDENTITY.honorificPrefix, domain=None, range=Optional[str])

slots.honorificSuffix = Slot(uri=IDENTITY.honorificSuffix, name="honorificSuffix", curie=IDENTITY.curie('honorificSuffix'),
                   model_uri=IDENTITY.honorificSuffix, domain=None, range=Optional[str])

slots.confidence = Slot(uri=CORE.confidence, name="confidence", curie=CORE.curie('confidence'),
                   model_uri=IDENTITY.confidence, domain=None, range=Optional[Union[int, NonNegativeIntegerType]])

slots.constrainingVocabularyName = Slot(uri=CORE.constrainingVocabularyName, name="constrainingVocabularyName", curie=CORE.curie('constrainingVocabularyName'),
                   model_uri=IDENTITY.constrainingVocabularyName, domain=None, range=Optional[str])

slots.constrainingVocabularyReference = Slot(uri=CORE.constrainingVocabularyReference, name="constrainingVocabularyReference", curie=CORE.curie('constrainingVocabularyReference'),
                   model_uri=IDENTITY.constrainingVocabularyReference, domain=None, range=Optional[Union[str, IriType]])

slots.context = Slot(uri=CORE.context, name="context", curie=CORE.curie('context'),
                   model_uri=IDENTITY.context, domain=None, range=Optional[str])

slots.createdBy = Slot(uri=CORE.createdBy, name="createdBy", curie=CORE.curie('createdBy'),
                   model_uri=IDENTITY.createdBy, domain=IdentityAbstraction, range=Optional[str])

slots.definingContext = Slot(uri=CORE.definingContext, name="definingContext", curie=CORE.curie('definingContext'),
                   model_uri=IDENTITY.definingContext, domain=None, range=Optional[str])

slots.description = Slot(uri=DCTERMS.description, name="description", curie=DCTERMS.curie('description'),
                   model_uri=IDENTITY.description, domain=None, range=Optional[str])

slots.endTime = Slot(uri=CORE.endTime, name="endTime", curie=CORE.curie('endTime'),
                   model_uri=IDENTITY.endTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.externalIdentifier = Slot(uri=CORE.externalIdentifier, name="externalIdentifier", curie=CORE.curie('externalIdentifier'),
                   model_uri=IDENTITY.externalIdentifier, domain=None, range=Optional[str])

slots.externalReference = Slot(uri=CORE.externalReference, name="externalReference", curie=CORE.curie('externalReference'),
                   model_uri=IDENTITY.externalReference, domain=ExternalReference, range=Optional[str])

slots.hasFacet = Slot(uri=CORE.hasFacet, name="hasFacet", curie=CORE.curie('hasFacet'),
                   model_uri=IDENTITY.hasFacet, domain=None, range=Optional[str])

slots.isDirectional = Slot(uri=CORE.isDirectional, name="isDirectional", curie=CORE.curie('isDirectional'),
                   model_uri=IDENTITY.isDirectional, domain=None, range=Optional[Union[bool, BooleanType]])

slots.kindOfRelationship = Slot(uri=CORE.kindOfRelationship, name="kindOfRelationship", curie=CORE.curie('kindOfRelationship'),
                   model_uri=IDENTITY.kindOfRelationship, domain=None, range=Optional[str])

slots.modifiedTime = Slot(uri=CORE.modifiedTime, name="modifiedTime", curie=CORE.curie('modifiedTime'),
                   model_uri=IDENTITY.modifiedTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.name = Slot(uri=RDFS.label, name="name", curie=RDFS.curie('label'),
                   model_uri=IDENTITY.name, domain=None, range=Optional[str])

slots.namingAuthority = Slot(uri=CORE.namingAuthority, name="namingAuthority", curie=CORE.curie('namingAuthority'),
                   model_uri=IDENTITY.namingAuthority, domain=None, range=Optional[str])

slots.object = Slot(uri=CORE.object, name="object", curie=CORE.curie('object'),
                   model_uri=IDENTITY.object, domain=None, range=Optional[Union[dict, UcoObject]])

slots.objectCreatedTime = Slot(uri=CORE.objectCreatedTime, name="objectCreatedTime", curie=CORE.curie('objectCreatedTime'),
                   model_uri=IDENTITY.objectCreatedTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.objectMarking = Slot(uri=CORE.objectMarking, name="objectMarking", curie=CORE.curie('objectMarking'),
                   model_uri=IDENTITY.objectMarking, domain=None, range=Optional[Union[dict, MarkingDefinitionAbstraction]])

slots.referenceURL = Slot(uri=CORE.referenceURL, name="referenceURL", curie=CORE.curie('referenceURL'),
                   model_uri=IDENTITY.referenceURL, domain=None, range=Optional[Union[str, IriType]])

slots.source = Slot(uri=CORE.source, name="source", curie=CORE.curie('source'),
                   model_uri=IDENTITY.source, domain=None, range=Optional[Union[dict, UcoObject]])

slots.specVersion = Slot(uri=CORE.specVersion, name="specVersion", curie=CORE.curie('specVersion'),
                   model_uri=IDENTITY.specVersion, domain=None, range=Optional[str])

slots.startTime = Slot(uri=CORE.startTime, name="startTime", curie=CORE.curie('startTime'),
                   model_uri=IDENTITY.startTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.statement = Slot(uri=CORE.statement, name="statement", curie=CORE.curie('statement'),
                   model_uri=IDENTITY.statement, domain=None, range=Optional[str])

slots.tag = Slot(uri=CORE.tag, name="tag", curie=CORE.curie('tag'),
                   model_uri=IDENTITY.tag, domain=None, range=Optional[str])

slots.target = Slot(uri=CORE.target, name="target", curie=CORE.curie('target'),
                   model_uri=IDENTITY.target, domain=None, range=Optional[Union[dict, UcoObject]])

slots.value = Slot(uri=CORE.value, name="value", curie=CORE.curie('value'),
                   model_uri=IDENTITY.value, domain=None, range=Optional[str])

slots.addressType = Slot(uri=LOCATION.addressType, name="addressType", curie=LOCATION.curie('addressType'),
                   model_uri=IDENTITY.addressType, domain=None, range=Optional[str])

slots.altitude = Slot(uri=LOCATION.altitude, name="altitude", curie=LOCATION.curie('altitude'),
                   model_uri=IDENTITY.altitude, domain=None, range=Optional[Union[Decimal, DecimalType]])

slots.country = Slot(uri=LOCATION.country, name="country", curie=LOCATION.curie('country'),
                   model_uri=IDENTITY.country, domain=None, range=Optional[str])

slots.hdop = Slot(uri=LOCATION.hdop, name="hdop", curie=LOCATION.curie('hdop'),
                   model_uri=IDENTITY.hdop, domain=None, range=Optional[Union[Decimal, DecimalType]])

slots.latitude = Slot(uri=LOCATION.latitude, name="latitude", curie=LOCATION.curie('latitude'),
                   model_uri=IDENTITY.latitude, domain=None, range=Optional[Union[Decimal, DecimalType]])

slots.locality = Slot(uri=LOCATION.locality, name="locality", curie=LOCATION.curie('locality'),
                   model_uri=IDENTITY.locality, domain=None, range=Optional[str])

slots.longitude = Slot(uri=LOCATION.longitude, name="longitude", curie=LOCATION.curie('longitude'),
                   model_uri=IDENTITY.longitude, domain=None, range=Optional[Union[Decimal, DecimalType]])

slots.pdop = Slot(uri=LOCATION.pdop, name="pdop", curie=LOCATION.curie('pdop'),
                   model_uri=IDENTITY.pdop, domain=None, range=Optional[Union[Decimal, DecimalType]])

slots.postalCode = Slot(uri=LOCATION.postalCode, name="postalCode", curie=LOCATION.curie('postalCode'),
                   model_uri=IDENTITY.postalCode, domain=None, range=Optional[str])

slots.region = Slot(uri=LOCATION.region, name="region", curie=LOCATION.curie('region'),
                   model_uri=IDENTITY.region, domain=None, range=Optional[str])

slots.street = Slot(uri=LOCATION.street, name="street", curie=LOCATION.curie('street'),
                   model_uri=IDENTITY.street, domain=None, range=Optional[str])

slots.tdop = Slot(uri=LOCATION.tdop, name="tdop", curie=LOCATION.curie('tdop'),
                   model_uri=IDENTITY.tdop, domain=None, range=Optional[Union[Decimal, DecimalType]])

slots.vdop = Slot(uri=LOCATION.vdop, name="vdop", curie=LOCATION.curie('vdop'),
                   model_uri=IDENTITY.vdop, domain=None, range=Optional[Union[Decimal, DecimalType]])

slots.AddressFacet_address = Slot(uri=IDENTITY.address, name="AddressFacet_address", curie=IDENTITY.curie('address'),
                   model_uri=IDENTITY.AddressFacet_address, domain=AddressFacet, range=Optional[Union[dict, "Location"]])

slots.BirthInformationFacet_birthdate = Slot(uri=IDENTITY.birthdate, name="BirthInformationFacet_birthdate", curie=IDENTITY.curie('birthdate'),
                   model_uri=IDENTITY.BirthInformationFacet_birthdate, domain=BirthInformationFacet, range=Optional[Union[str, XSDDateTime]])

slots.SimpleNameFacet_familyName = Slot(uri=IDENTITY.familyName, name="SimpleNameFacet_familyName", curie=IDENTITY.curie('familyName'),
                   model_uri=IDENTITY.SimpleNameFacet_familyName, domain=SimpleNameFacet, range=Optional[Union[str, List[str]]])

slots.SimpleNameFacet_givenName = Slot(uri=IDENTITY.givenName, name="SimpleNameFacet_givenName", curie=IDENTITY.curie('givenName'),
                   model_uri=IDENTITY.SimpleNameFacet_givenName, domain=SimpleNameFacet, range=Optional[Union[str, List[str]]])

slots.SimpleNameFacet_honorificPrefix = Slot(uri=IDENTITY.honorificPrefix, name="SimpleNameFacet_honorificPrefix", curie=IDENTITY.curie('honorificPrefix'),
                   model_uri=IDENTITY.SimpleNameFacet_honorificPrefix, domain=SimpleNameFacet, range=Optional[Union[str, List[str]]])

slots.SimpleNameFacet_honorificSuffix = Slot(uri=IDENTITY.honorificSuffix, name="SimpleNameFacet_honorificSuffix", curie=IDENTITY.curie('honorificSuffix'),
                   model_uri=IDENTITY.SimpleNameFacet_honorificSuffix, domain=SimpleNameFacet, range=Optional[Union[str, List[str]]])

slots.Annotation_object = Slot(uri=CORE.object, name="Annotation_object", curie=CORE.curie('object'),
                   model_uri=IDENTITY.Annotation_object, domain=Annotation, range=Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]])

slots.Assertion_statement = Slot(uri=CORE.statement, name="Assertion_statement", curie=CORE.curie('statement'),
                   model_uri=IDENTITY.Assertion_statement, domain=Assertion, range=Optional[Union[str, List[str]]])

slots.AttributedName_namingAuthority = Slot(uri=CORE.namingAuthority, name="AttributedName_namingAuthority", curie=CORE.curie('namingAuthority'),
                   model_uri=IDENTITY.AttributedName_namingAuthority, domain=AttributedName, range=Optional[str])

slots.ConfidenceFacet_confidence = Slot(uri=CORE.confidence, name="ConfidenceFacet_confidence", curie=CORE.curie('confidence'),
                   model_uri=IDENTITY.ConfidenceFacet_confidence, domain=ConfidenceFacet, range=Union[int, NonNegativeIntegerType])

slots.ContextualCompilation_object = Slot(uri=CORE.object, name="ContextualCompilation_object", curie=CORE.curie('object'),
                   model_uri=IDENTITY.ContextualCompilation_object, domain=ContextualCompilation, range=Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]])

slots.ControlledVocabulary_constrainingVocabularyReference = Slot(uri=CORE.constrainingVocabularyReference, name="ControlledVocabulary_constrainingVocabularyReference", curie=CORE.curie('constrainingVocabularyReference'),
                   model_uri=IDENTITY.ControlledVocabulary_constrainingVocabularyReference, domain=ControlledVocabulary, range=Optional[Union[str, IriType]])

slots.ControlledVocabulary_constrainingVocabularyName = Slot(uri=CORE.constrainingVocabularyName, name="ControlledVocabulary_constrainingVocabularyName", curie=CORE.curie('constrainingVocabularyName'),
                   model_uri=IDENTITY.ControlledVocabulary_constrainingVocabularyName, domain=ControlledVocabulary, range=Optional[str])

slots.ControlledVocabulary_value = Slot(uri=CORE.value, name="ControlledVocabulary_value", curie=CORE.curie('value'),
                   model_uri=IDENTITY.ControlledVocabulary_value, domain=ControlledVocabulary, range=str)

slots.EnclosingCompilation_object = Slot(uri=CORE.object, name="EnclosingCompilation_object", curie=CORE.curie('object'),
                   model_uri=IDENTITY.EnclosingCompilation_object, domain=EnclosingCompilation, range=Optional[Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]]])

slots.ExternalReference_referenceURL = Slot(uri=CORE.referenceURL, name="ExternalReference_referenceURL", curie=CORE.curie('referenceURL'),
                   model_uri=IDENTITY.ExternalReference_referenceURL, domain=ExternalReference, range=Optional[Union[str, IriType]])

slots.ExternalReference_definingContext = Slot(uri=CORE.definingContext, name="ExternalReference_definingContext", curie=CORE.curie('definingContext'),
                   model_uri=IDENTITY.ExternalReference_definingContext, domain=ExternalReference, range=Optional[str])

slots.ExternalReference_externalIdentifier = Slot(uri=CORE.externalIdentifier, name="ExternalReference_externalIdentifier", curie=CORE.curie('externalIdentifier'),
                   model_uri=IDENTITY.ExternalReference_externalIdentifier, domain=ExternalReference, range=Optional[str])

slots.Grouping_context = Slot(uri=CORE.context, name="Grouping_context", curie=CORE.curie('context'),
                   model_uri=IDENTITY.Grouping_context, domain=Grouping, range=Optional[Union[str, List[str]]])

slots.Relationship_endTime = Slot(uri=CORE.endTime, name="Relationship_endTime", curie=CORE.curie('endTime'),
                   model_uri=IDENTITY.Relationship_endTime, domain=Relationship, range=Optional[Union[Union[str, XSDDateTime], List[Union[str, XSDDateTime]]]])

slots.Relationship_isDirectional = Slot(uri=CORE.isDirectional, name="Relationship_isDirectional", curie=CORE.curie('isDirectional'),
                   model_uri=IDENTITY.Relationship_isDirectional, domain=Relationship, range=Union[bool, BooleanType])

slots.Relationship_kindOfRelationship = Slot(uri=CORE.kindOfRelationship, name="Relationship_kindOfRelationship", curie=CORE.curie('kindOfRelationship'),
                   model_uri=IDENTITY.Relationship_kindOfRelationship, domain=Relationship, range=Optional[str])

slots.Relationship_target = Slot(uri=CORE.target, name="Relationship_target", curie=CORE.curie('target'),
                   model_uri=IDENTITY.Relationship_target, domain=Relationship, range=Union[dict, "UcoObject"])

slots.Relationship_source = Slot(uri=CORE.source, name="Relationship_source", curie=CORE.curie('source'),
                   model_uri=IDENTITY.Relationship_source, domain=Relationship, range=Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]])

slots.Relationship_startTime = Slot(uri=CORE.startTime, name="Relationship_startTime", curie=CORE.curie('startTime'),
                   model_uri=IDENTITY.Relationship_startTime, domain=Relationship, range=Optional[Union[Union[str, XSDDateTime], List[Union[str, XSDDateTime]]]])

slots.UcoObject_description = Slot(uri=DCTERMS.description, name="UcoObject_description", curie=DCTERMS.curie('description'),
                   model_uri=IDENTITY.UcoObject_description, domain=UcoObject, range=Optional[Union[str, List[str]]])

slots.UcoObject_createdBy = Slot(uri=CORE.createdBy, name="UcoObject_createdBy", curie=CORE.curie('createdBy'),
                   model_uri=IDENTITY.UcoObject_createdBy, domain=UcoObject, range=Optional[str])

slots.UcoObject_externalReference = Slot(uri=CORE.externalReference, name="UcoObject_externalReference", curie=CORE.curie('externalReference'),
                   model_uri=IDENTITY.UcoObject_externalReference, domain=UcoObject, range=Optional[Union[str, List[str]]])

slots.UcoObject_hasFacet = Slot(uri=CORE.hasFacet, name="UcoObject_hasFacet", curie=CORE.curie('hasFacet'),
                   model_uri=IDENTITY.UcoObject_hasFacet, domain=UcoObject, range=Optional[Union[str, List[str]]])

slots.UcoObject_modifiedTime = Slot(uri=CORE.modifiedTime, name="UcoObject_modifiedTime", curie=CORE.curie('modifiedTime'),
                   model_uri=IDENTITY.UcoObject_modifiedTime, domain=UcoObject, range=Optional[Union[Union[str, XSDDateTime], List[Union[str, XSDDateTime]]]])

slots.UcoObject_name = Slot(uri=RDFS.label, name="UcoObject_name", curie=RDFS.curie('label'),
                   model_uri=IDENTITY.UcoObject_name, domain=UcoObject, range=Optional[str])

slots.UcoObject_objectCreatedTime = Slot(uri=CORE.objectCreatedTime, name="UcoObject_objectCreatedTime", curie=CORE.curie('objectCreatedTime'),
                   model_uri=IDENTITY.UcoObject_objectCreatedTime, domain=UcoObject, range=Optional[Union[str, XSDDateTime]])

slots.UcoObject_objectMarking = Slot(uri=CORE.objectMarking, name="UcoObject_objectMarking", curie=CORE.curie('objectMarking'),
                   model_uri=IDENTITY.UcoObject_objectMarking, domain=UcoObject, range=Optional[Union[Union[dict, MarkingDefinitionAbstraction], List[Union[dict, MarkingDefinitionAbstraction]]]])

slots.UcoObject_specVersion = Slot(uri=CORE.specVersion, name="UcoObject_specVersion", curie=CORE.curie('specVersion'),
                   model_uri=IDENTITY.UcoObject_specVersion, domain=UcoObject, range=Optional[str])

slots.UcoObject_tag = Slot(uri=CORE.tag, name="UcoObject_tag", curie=CORE.curie('tag'),
                   model_uri=IDENTITY.UcoObject_tag, domain=UcoObject, range=Optional[Union[str, List[str]]])

slots.GPSCoordinatesFacet_hdop = Slot(uri=LOCATION.hdop, name="GPSCoordinatesFacet_hdop", curie=LOCATION.curie('hdop'),
                   model_uri=IDENTITY.GPSCoordinatesFacet_hdop, domain=GPSCoordinatesFacet, range=Optional[Union[Decimal, DecimalType]])

slots.GPSCoordinatesFacet_pdop = Slot(uri=LOCATION.pdop, name="GPSCoordinatesFacet_pdop", curie=LOCATION.curie('pdop'),
                   model_uri=IDENTITY.GPSCoordinatesFacet_pdop, domain=GPSCoordinatesFacet, range=Optional[Union[Decimal, DecimalType]])

slots.GPSCoordinatesFacet_tdop = Slot(uri=LOCATION.tdop, name="GPSCoordinatesFacet_tdop", curie=LOCATION.curie('tdop'),
                   model_uri=IDENTITY.GPSCoordinatesFacet_tdop, domain=GPSCoordinatesFacet, range=Optional[Union[Decimal, DecimalType]])

slots.GPSCoordinatesFacet_vdop = Slot(uri=LOCATION.vdop, name="GPSCoordinatesFacet_vdop", curie=LOCATION.curie('vdop'),
                   model_uri=IDENTITY.GPSCoordinatesFacet_vdop, domain=GPSCoordinatesFacet, range=Optional[Union[Decimal, DecimalType]])

slots.LatLongCoordinatesFacet_altitude = Slot(uri=LOCATION.altitude, name="LatLongCoordinatesFacet_altitude", curie=LOCATION.curie('altitude'),
                   model_uri=IDENTITY.LatLongCoordinatesFacet_altitude, domain=LatLongCoordinatesFacet, range=Optional[Union[Decimal, DecimalType]])

slots.LatLongCoordinatesFacet_latitude = Slot(uri=LOCATION.latitude, name="LatLongCoordinatesFacet_latitude", curie=LOCATION.curie('latitude'),
                   model_uri=IDENTITY.LatLongCoordinatesFacet_latitude, domain=LatLongCoordinatesFacet, range=Optional[Union[Decimal, DecimalType]])

slots.LatLongCoordinatesFacet_longitude = Slot(uri=LOCATION.longitude, name="LatLongCoordinatesFacet_longitude", curie=LOCATION.curie('longitude'),
                   model_uri=IDENTITY.LatLongCoordinatesFacet_longitude, domain=LatLongCoordinatesFacet, range=Optional[Union[Decimal, DecimalType]])

slots.SimpleAddressFacet_addressType = Slot(uri=LOCATION.addressType, name="SimpleAddressFacet_addressType", curie=LOCATION.curie('addressType'),
                   model_uri=IDENTITY.SimpleAddressFacet_addressType, domain=SimpleAddressFacet, range=Optional[str])

slots.SimpleAddressFacet_country = Slot(uri=LOCATION.country, name="SimpleAddressFacet_country", curie=LOCATION.curie('country'),
                   model_uri=IDENTITY.SimpleAddressFacet_country, domain=SimpleAddressFacet, range=Optional[str])

slots.SimpleAddressFacet_locality = Slot(uri=LOCATION.locality, name="SimpleAddressFacet_locality", curie=LOCATION.curie('locality'),
                   model_uri=IDENTITY.SimpleAddressFacet_locality, domain=SimpleAddressFacet, range=Optional[str])

slots.SimpleAddressFacet_postalCode = Slot(uri=LOCATION.postalCode, name="SimpleAddressFacet_postalCode", curie=LOCATION.curie('postalCode'),
                   model_uri=IDENTITY.SimpleAddressFacet_postalCode, domain=SimpleAddressFacet, range=Optional[str])

slots.SimpleAddressFacet_region = Slot(uri=LOCATION.region, name="SimpleAddressFacet_region", curie=LOCATION.curie('region'),
                   model_uri=IDENTITY.SimpleAddressFacet_region, domain=SimpleAddressFacet, range=Optional[str])

slots.SimpleAddressFacet_street = Slot(uri=LOCATION.street, name="SimpleAddressFacet_street", curie=LOCATION.curie('street'),
                   model_uri=IDENTITY.SimpleAddressFacet_street, domain=SimpleAddressFacet, range=Optional[str])