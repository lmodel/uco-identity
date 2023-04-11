

CREATE TABLE "AddressFacet" (
	address TEXT, 
	PRIMARY KEY (address)
);

CREATE TABLE "Annotation" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	statement TEXT, 
	object TEXT NOT NULL, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, statement, object)
);

CREATE TABLE "Assertion" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	statement TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, statement)
);

CREATE TABLE "AttributedName" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	"namingAuthority" TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, "namingAuthority")
);

CREATE TABLE "BirthInformationFacet" (
	birthdate DATETIME, 
	PRIMARY KEY (birthdate)
);

CREATE TABLE "Bundle" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	object TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, object)
);

CREATE TABLE "Compilation" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "ConfidenceFacet" (
	confidence INTEGER NOT NULL, 
	PRIMARY KEY (confidence)
);

CREATE TABLE "ContextualCompilation" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	object TEXT NOT NULL, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, object)
);

CREATE TABLE "ControlledVocabulary" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	"constrainingVocabularyReference" TEXT, 
	"constrainingVocabularyName" TEXT, 
	value TEXT NOT NULL, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, "constrainingVocabularyReference", "constrainingVocabularyName", value)
);

CREATE TABLE "EnclosingCompilation" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	object TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, object)
);

CREATE TABLE "ExternalReference" (
	"referenceURL" TEXT, 
	"definingContext" TEXT, 
	"externalIdentifier" TEXT, 
	PRIMARY KEY ("referenceURL", "definingContext", "externalIdentifier")
);

CREATE TABLE "GPSCoordinatesFacet" (
	hdop FLOAT, 
	pdop FLOAT, 
	tdop FLOAT, 
	vdop FLOAT, 
	PRIMARY KEY (hdop, pdop, tdop, vdop)
);

CREATE TABLE "Grouping" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	object TEXT NOT NULL, 
	context TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, object, context)
);

CREATE TABLE "Identity" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "IdentityAbstraction" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "Item" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "LatLongCoordinatesFacet" (
	altitude FLOAT, 
	latitude FLOAT, 
	longitude FLOAT, 
	PRIMARY KEY (altitude, latitude, longitude)
);

CREATE TABLE "Location" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "MarkingDefinitionAbstraction" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "ModusOperandi" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "Organization" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "Person" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "Relationship" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	"endTime" DATETIME, 
	"isDirectional" BOOLEAN NOT NULL, 
	"kindOfRelationship" TEXT, 
	source TEXT NOT NULL, 
	"startTime" DATETIME, 
	target TEXT NOT NULL, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, "endTime", "isDirectional", "kindOfRelationship", source, "startTime", target)
);

CREATE TABLE "SimpleAddressFacet" (
	"addressType" TEXT, 
	country TEXT, 
	locality TEXT, 
	"postalCode" TEXT, 
	region TEXT, 
	street TEXT, 
	PRIMARY KEY ("addressType", country, locality, "postalCode", region, street)
);

CREATE TABLE "SimpleNameFacet" (
	"familyName" TEXT, 
	"givenName" TEXT, 
	"honorificPrefix" TEXT, 
	"honorificSuffix" TEXT, 
	PRIMARY KEY ("familyName", "givenName", "honorificPrefix", "honorificSuffix")
);

CREATE TABLE "UcoObject" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);
