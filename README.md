**Google My Business API**
This python code is used to create a new business profile using the API call ***accounts.locations.create()*** method call from mybusiness business information API 

**The json payload to upload the business information in the body parameter of create() method is:**

{
#   "name": string,
#   "languageCode": string,
#   "storeCode": string,
#   "title": string,
#   "phoneNumbers": {
#       "primaryPhone": string,
#       "additionalPhones": [
#           string
#       ]
#   },
#   "categories": {
#     "primaryCategory": {
#       "name": string,
#       "displayName": string,
#       "serviceTypes": [
#       {
#           "serviceTypeId": string,
#           "displayName": string
#       }
#       ],
#       "moreHoursTypes": [
#       {
#           "hoursTypeId": string,
#           "displayName": string,
#           "localizedDisplayName": string
#       }
#       ]
#       },
#       "additionalCategories": [
#       {
#       "name": string,
#       "displayName": string,
#       "serviceTypes": [
#       {
#       "serviceTypeId": string,
#       "displayName": string
#       }
#       ],
#       "moreHoursTypes": [
#       {
#           "hoursTypeId": string,
#           "displayName": string,
#           "localizedDisplayName": string
#       }
#       ]
#       }
#       ]
#   },
#   "storefrontAddress": {
#       "revision": integer,
#       "regionCode": string,
#       "languageCode": string,
#       "postalCode": string,
#       "sortingCode": string,
#       "administrativeArea": string,
#       "locality": string,
#       "sublocality": string,
#       "addressLines": [
#               string
#       ],
#       "recipients": [
#           string
#       ],
#       "organization": string
#   },
#   "websiteUri": string,
#   "regularHours": {
#     "periods": [
#     {
#       "openDay": enum (DayOfWeek),
#       "openTime": {
#             "hours": integer,
#             "minutes": integer,
#             "seconds": integer,
#             "nanos": integer
#             },
#       "closeDay": enum (DayOfWeek), 
#       "closeTime": {
#             "hours": integer,
#             "minutes": integer,
#             "seconds": integer,
#             "nanos": integer
#             }
#     }
#     ]
#   },
#   "specialHours": {
#     "specialHourPeriods": [
#       {
#       "startDate": 
#       {
#             "year": integer,
#             "month": integer,
#             "day": integer
#       },
#       "openTime": 
#       {
#             "hours": integer,
#             "minutes": integer,
#             "seconds": integer,
#             "nanos": integer
#       },
#       "endDate": 
#       {
#             "year": integer,
#             "month": integer,
#             "day": integer
#       },
#       "closeTime": 
#       {
#             "hours": integer,
#             "minutes": integer,
#             "seconds": integer,
#             "nanos": integer
#       },
#       "closed": boolean
#   }
#   ]
#   },
#   "serviceArea": {
#     "businessType": enum (BusinessType),
#     "places": 
#     {
#           "placeInfos": [
#           {
#               "placeName": string,
#               "placeId": string
#           }
#           ]
#     },
#     "regionCode": string
#   },
#   "labels": [
#       string
#   ],
#   "adWordsLocationExtensions": {
#     "adPhone": string
#   },
#   "latlng": {
#     "latitude": number,
#     "longitude": number
#   },
#   "openInfo": {
#     "status": enum (OpenForBusiness),
#     "canReopen": boolean,
#     "openingDate": 
#     {
#           "year": integer,
#           "month": integer,
#           "day": integer
#     },
#   "metadata": 
#     {
#           "hasGoogleUpdated": boolean,
#           "hasPendingEdits": boolean,
#           "canDelete": boolean,
#           "canOperateLocalPost": boolean,
#           "canModifyServiceList": boolean,
#          "canHaveFoodMenus": boolean,
#           "canOperateHealthData": boolean,
#           "canOperateLodgingData": boolean,
#           "placeId": string,
#           "duplicateLocation": string,
#           "mapsUri": string,
#           "newReviewUri": string,
#           "canHaveBusinessCalls": boolean,
#           "hasVoiceOfMerchant": boolean
#     },
#   "profile": {
#     "description": string
#   },
#   "relationshipData": {
#     "parentLocation": 
#     {
#           "placeId": string,
#           "relationType": enum (RelationType)
#     },
#     "childrenLocations": [
#     {
#           "placeId": string,
#           "relationType": enum (RelationType)
#     }
#     ],
#     "parentChain": string
#   },
#   "moreHours": [
#     {
#       "hoursTypeId": string,
#       "periods": [
#       {
#       "openDay": enum (DayOfWeek),
#       "openTime": {
#             "hours": integer,
#             "minutes": integer,
#             "seconds": integer,
#             "nanos": integer
#             },
#       "closeDay": enum (DayOfWeek), 
#       "closeTime": {
#             "hours": integer,
#             "minutes": integer,
#             "seconds": integer,
#             "nanos": integer
#             }
#     
#       }
#       ]
#     }
#   ],
#   "serviceItems": [
#     {
#       "price": 
#       {
#             "currencyCode": string,
#             "units": string,
#             "nanos": integer
#       },
# // Union field service_item_info can be only one of the following:
#       "structuredServiceItem": 
#       {
#             "serviceTypeId": string,
#             "description": string
#       },
#       "freeFormServiceItem": 
#       {
#             "category": string,
#       "label": 
#       {
#             "displayName": string,
#             "description": string,
#             "languageCode": string
#       }
#       }
# // End of list of possible types for union field service_item_info.
#     }
#   ]
# }
