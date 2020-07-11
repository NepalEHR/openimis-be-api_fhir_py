from api_fhir_R4.models import Element, Property


class Extension(Element):

    url = Property('url', str, required=True)
    valueAddress = Property('valueAddress', 'Address')
    valueAge = Property('valueAge', 'Age')
    valueAnnotation = Property('valueAnnotation', 'Annotation')
    valueAttachment = Property('valueAttachment', 'Attachment')
    valueBase64Binary = Property('valueBase64Binary', str)
    valueBoolean = Property('valueBoolean', bool)
    valueCanonical = Property('valueCanonical', str)
    valueCode = Property('valueCode', str)
    valueCodeableConcept = Property('valueCodeableConcept', 'CodeableConcept')
    valueCoding = Property('valueCoding', 'Coding')
    valueContactPoint = Property('valueContactPoint', 'ContactPoint')
    valueCount = Property('valueCount', 'Count')
    valueDate = Property('valueDate', 'FHIRDate')
    valueDateTime = Property('valueDateTime', 'FHIRDate')
    valueDecimal = Property('valueDecimal', float)
    valueDistance = Property('valueDistance', 'Distance')
    valueDuration = Property('valueDuration', 'Duration')
    valueHumanName = Property('valueHumanName', 'HumanName')
    valueId = Property('valueId', str)
    valueIdentifier = Property('valueIdentifier', 'Identifier')
    valueInstant = Property('valueInstant', 'FHIRDate')
    valueInteger = Property('valueInteger', int)
    valueMarkdown = Property('valueMarkdown', str)
    valueMeta = Property('valueMeta', 'Meta')
    valueMoney = Property('valueMoney', 'Money')
    valueOid = Property('valueOid', str)
    valuePeriod = Property('valuePeriod', 'Period')
    valuePositiveInt = Property('valuePositiveInt', int)
    valueQuantity = Property('valueQuantity', 'Quantity')
    valueRange = Property('valueRange', 'Range')
    valueRatio = Property('valueRatio', 'Ratio')
    valueReference = Property('valueReference', 'Reference')
    valueSampledData = Property('valueSampledData', 'SampledData')
    valueSignature = Property('valueSignature', 'Signature')
    valueString = Property('valueString', str)
    valueTime = Property('valueTime', 'FHIRDate')
    valueTiming = Property('valueTiming', 'Timing')
    valueUnsignedInt = Property('valueUnsignedInt', int)
    valueUsageContext = Property("valueUsageContext", "UsageContext")
    valueUri = Property('valueUri', str)