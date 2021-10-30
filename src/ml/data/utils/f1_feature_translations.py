from .FeatureTranslation import FeatureTranslation

def get_translations():
	ANurLvl_mappings = {
		'X00': 'Normal',
		'C99': 'C Unknown',
		'T99': 'T Unknown',
		'L99': 'L Unknown',
		'S99': 'S Unknown',
		'X99': 'Unknown'
	}
	ANCat_mappings = {
		'1': 'Incomplete Paraplegic',
		'2': 'Complete Paraplegic',
		'3': 'Minimal Deficit Paraplegic',
		'4': 'Incomplete Tetraplegic',
		'5': 'Complete Tetraplegic',
		'6': 'Minimal Deficit Tetraplegic',
		'7': 'Normal',
		'8': 'Minimal Deficit Normal',
		'9': 'Unknown'
	}
	AASAIm_mappings = {
		'5': 'A',
		'1': 'B',
		'2': 'C',
		'3': 'D',
		'4': 'E',
		'9': 'Unknown',
		'U': 'Unknown' # key not documented, but discovered
	}
	
	return {
		'AInjDt': FeatureTranslation('Injury Date', {}),
		'ASex': FeatureTranslation('Sex', {
			'1': 'Male',
			'2': 'Female',
			'3': 'Other',
			'4': 'Unknown'
		}),
		'AInjAge': FeatureTranslation('Age - Injury', {
			'999': 'Unknown'
		}),
		'AHghtRhb': FeatureTranslation('Height - Admission', {
			'999': 'Unknown'
		}),
		'AWghtRhb': FeatureTranslation('Weight - Admission', {
			'888': 'Over Maximum',
			'999': 'Unknown'
		}),
		'ANurLvlA': FeatureTranslation('Level of Injury - Admission', ANurLvl_mappings),
		'AAnSnAdm': FeatureTranslation('Anal Sensation - Admission', {
			'0': 'False',
			'1': 'True',
			'8': 'Unknown',
			'9': 'Unknown'
		}),
		'AVoSphAd': FeatureTranslation('Anal Contraction - Admission', {
			'0': 'False',
			'1': 'True',
			'8': 'Unknown',
			'9': 'Unknown'
		}),
		'AASAImAd': FeatureTranslation('ASIA - Admission', AASAIm_mappings),
		'AASAImDs': FeatureTranslation('ASIA - Discharge', AASAIm_mappings),
		'ANCatAdm': FeatureTranslation('Neurologic Category - Admission', ANCat_mappings),
		'ANurLvlD': FeatureTranslation('Level of Injury - Discharge', ANurLvl_mappings),
		'ANCatDis': FeatureTranslation('Neurologic Category - Discharge', ANCat_mappings),
		'ARace': FeatureTranslation('Race', {
			'1': 'White',
			'2': 'Black',
			'3': 'Native American',
			'4': 'Asian',
			'5': 'Multiracial',
			'7': 'Unknown',
			'9': 'Unknown'
		}),
		'AMarStIj': FeatureTranslation('Marital Status - Injury', {
			'1': 'Never Married',
			'2': 'Married',
			'3': 'Divorced',
			'4': 'Separated',
			'5': 'Widowed',
			'6': 'Other',
			'7': 'Living Unmarried With Partner',
			'9': 'Unknown'
		}),
		'AEducLvl': FeatureTranslation('Education - Injury', {
			'1': 'Less Than 9th Grade',
			'2': '9th-11th Grade',
			'3': 'High School',
			'4': 'Associate Degree',
			'5': 'Bachelors Degree',
			'6': 'Masters Degree',
			'7': 'Doctorate',
			'8': 'Other',
			'9': 'Unknown'
		}),
		'APrLvlSt': FeatureTranslation('Occupation Status - Injury', {
			'1': 'Working',
			'2': 'Homemaker',
			'3': 'In Training',
			'4': 'In Workshop',
			'5': 'Retired',
			'6': 'Student or Infant',
			'7': 'Unemployed',
			'8': 'Other',
			'9': 'Unknown'
		}),
		'AJobCnCd': FeatureTranslation('Occupation Code - Injury', {
			'1': 'Managerial',
			'2': 'Specialty',
			'3': 'Technicians',
			'4': 'Sales',
			'5': 'Administrative Support',
			'6': 'Private Household',
			'7': 'Protective Service',
			'8': 'Service',
			'9': 'Farming, Forestry, Fishing',
			'10': 'Precision Craft and Repair',
			'11': 'Machinery and Inspection',
			'12': 'Transportation',
			'13': 'Cleaners and Labourers',
			'14': 'Military',
			'88': 'Not Applicable',
			'99': 'Unknown'
		}),
		'AFmIncLv': FeatureTranslation('Family Income - Injury', {
			'1': '<25,000',
			'2': '25,000-49,999',
			'3': '50,000-74,999',
			'4': '>75,000',
			'6': 'Unknown',
			'7': 'Unknown',
			'9': 'Unknown'
		}),
		'AVeteran': FeatureTranslation('Veteran', {
			'0': 'False',
			'1': 'True',
			'9': 'Unknown'
		}),
		'APrimPay': FeatureTranslation('Primary Insurance', {
			'1': 'Private Insurance',
			'2': 'Medicare',
			'3': 'Medicaid',
			'4': "Workers' Compensation",
			'5': 'VA',
			'6': 'Other Government',
			'7': 'No Pay',
			'8': 'Private Funds',
			'9': 'Other',
			'77': 'Unknown',
			'99': 'Unknown'
		}),
		'ADepress': FeatureTranslation('Depression - History', {
			'0': 'False',
			'1': 'True',
			'7': 'Unknown',
			'9': 'Unknown'
		}),
		'AAnxiety': FeatureTranslation('Anxiety - History', {
			'0': 'False',
			'1': 'PTSD',
			'2': 'Panic Disorder',
			'3': 'General Anxiety',
			'4': 'Multiple',
			'7': 'Unknown',
			'9': 'Unknown'
		}),
		'ADiabete': FeatureTranslation('Diabetes - History', {
			'0': 'False',
			'1': 'Medication Controlled',
			'2': 'Lifestyle Controlled',
			'3': 'Not Controlled',
			'4': 'Unknown If Controlled',
			'7': 'Unknown',
			'9': 'Unknown'
		}),
		'AAlcNbDr': FeatureTranslation('Daily Alcohol - History', {
			'1': '1-2',
			'2': '3-4',
			'3': '5-6',
			'4': '7-9',
			'5': '10+',
			'7': 'Unknown',
			'9': 'Unknown'
		}),
		'ATBILOC': FeatureTranslation('Loss of Consciousness - Injury', {
			'0': 'False',
			'1': '<=30min',
			'2': '31min-24hrs',
			'3': '24hrs+',
			'7': 'Unknown',
			'9': 'Unknown'
		}),
		'ATBIMem': FeatureTranslation('Loss of Memory - Injury', {
			'0': 'False',
			'1': 'True',
			'7': 'Unknown',
			'9': 'Unknown'
		}),
		'ATBISevR': FeatureTranslation('TBI Likelihood - Injury', {
			'1': 'Improbable',
			'2': 'Possible',
			'3': 'Mild',
			'4': 'Moderate',
			'5': 'Severe',
			'7': 'Unknown',
			'9': 'Unknown'
		})
	}