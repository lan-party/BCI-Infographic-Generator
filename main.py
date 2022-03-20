import requests
from PIL import Image, ImageDraw, ImageFont
import os
import random

'''
# download available country silhouette PNGs from silhouettegarden.com/
countries = {'Afghanistan': 'AF', 'Albania': 'AL', 'Algeria': 'DZ', 'American Samoa': 'AS', 'Andorra': 'AD', 'Angola': 'AO', 'Anguilla': 'AI', 'Antarctica': 'AQ', 'Antigua and Barbuda': 'AG', 'Argentina': 'AR', 'Armenia': 'AM', 'Aruba': 'AW', 'Australia': 'AU', 'Austria': 'AT', 'Azerbaijan': 'AZ', 'Bahamas': 'BS', 'Bahrain': 'BH', 'Bangladesh': 'BD', 'Barbados': 'BB', 'Belarus': 'BY', 'Belgium': 'BE', 'Belize': 'BZ', 'Benin': 'BJ', 'Bermuda': 'BM', 'Bhutan': 'BT', 'Bolivia, Plurinational State of': 'BO', 'Bolivia': 'BO', 'Bosnia and Herzegovina': 'BA', 'Botswana': 'BW', 'Bouvet Island': 'BV', 'Brazil': 'BR', 'British Indian Ocean Territory': 'IO', 'Brunei Darussalam': 'BN', 'Brunei': 'BN', 'Bulgaria': 'BG', 'Burkina Faso': 'BF', 'Burundi': 'BI', 'Cambodia': 'KH', 'Cameroon': 'CM', 'Canada': 'CA', 'Cape Verde': 'CV', 'Cayman Islands': 'KY', 'Central African Republic': 'CF', 'Chad': 'TD', 'Chile': 'CL', 'China': 'CN', 'Christmas Island': 'CX', 'Cocos (Keeling) Islands': 'CC', 'Colombia': 'CO', 'Comoros': 'KM', 'Congo': 'CG', 'Congo, the Democratic Republic of the': 'CD', 'Cook Islands': 'CK', 'Costa Rica': 'CR', "Côte d'Ivoire": 'CI', 'Ivory Coast': 'CI', 'Croatia': 'HR', 'Cuba': 'CU', 'Cyprus': 'CY', 'Czech Republic': 'CZ', 'Denmark': 'DK', 'Djibouti': 'DJ', 'Dominica': 'DM', 'Dominican Republic': 'DO', 'Ecuador': 'EC', 'Egypt': 'EG', 'El Salvador': 'SV', 'Equatorial Guinea': 'GQ', 'Eritrea': 'ER', 'Estonia': 'EE', 'Ethiopia': 'ET', 'Falkland Islands (Malvinas)': 'FK', 'Faroe Islands': 'FO', 'Fiji': 'FJ', 'Finland': 'FI', 'France': 'FR', 'French Guiana': 'GF', 'French Polynesia': 'PF', 'French Southern Territories': 'TF', 'Gabon': 'GA', 'Gambia': 'GM', 'Georgia': 'GE', 'Germany': 'DE', 'Ghana': 'GH', 'Gibraltar': 'GI', 'Greece': 'GR', 'Greenland': 'GL', 'Grenada': 'GD', 'Guadeloupe': 'GP', 'Guam': 'GU', 'Guatemala': 'GT', 'Guernsey': 'GG', 'Guinea': 'GN', 'Guinea-Bissau': 'GW', 'Guyana': 'GY', 'Haiti': 'HT', 'Heard Island and McDonald Islands': 'HM', 'Holy See (Vatican City State)': 'VA', 'Honduras': 'HN', 'Hong Kong': 'HK', 'Hungary': 'HU', 'Iceland': 'IS', 'India': 'IN', 'Indonesia': 'ID', 'Iran, Islamic Republic of': 'IR', 'Iraq': 'IQ', 'Ireland': 'IE', 'Isle of Man': 'IM', 'Israel': 'IL', 'Italy': 'IT', 'Jamaica': 'JM', 'Japan': 'JP', 'Jersey': 'JE', 'Jordan': 'JO', 'Kazakhstan': 'KZ', 'Kenya': 'KE', 'Kiribati': 'KI', "Korea, Democratic People's Republic of": 'KP', 'Korea, Republic of': 'KR', 'South Korea': 'KR', 'Kuwait': 'KW', 'Kyrgyzstan': 'KG', "Lao People's Democratic Republic": 'LA', 'Latvia': 'LV', 'Lebanon': 'LB', 'Lesotho': 'LS', 'Liberia': 'LR', 'Libyan Arab Jamahiriya': 'LY', 'Libya': 'LY', 'Liechtenstein': 'LI', 'Lithuania': 'LT', 'Luxembourg': 'LU', 'Macao': 'MO', 'Macedonia, the former Yugoslav Republic of': 'MK', 'Madagascar': 'MG', 'Malawi': 'MW', 'Malaysia': 'MY', 'Maldives': 'MV', 'Mali': 'ML', 'Malta': 'MT', 'Marshall Islands': 'MH', 'Martinique': 'MQ', 'Mauritania': 'MR', 'Mauritius': 'MU', 'Mayotte': 'YT', 'Mexico': 'MX', 'Micronesia, Federated States of': 'FM', 'Moldova, Republic of': 'MD', 'Monaco': 'MC', 'Mongolia': 'MN', 'Montenegro': 'ME', 'Montserrat': 'MS', 'Morocco': 'MA', 'Mozambique': 'MZ', 'Myanmar': 'MM', 'Burma': 'MM', 'Namibia': 'NA', 'Nauru': 'NR', 'Nepal': 'NP', 'Netherlands': 'NL', 'Netherlands Antilles': 'AN', 'New Caledonia': 'NC', 'New Zealand': 'NZ', 'Nicaragua': 'NI', 'Niger': 'NE', 'Nigeria': 'NG', 'Niue': 'NU', 'Norfolk Island': 'NF', 'Northern Mariana Islands': 'MP', 'Norway': 'NO', 'Oman': 'OM', 'Pakistan': 'PK', 'Palau': 'PW', 'Palestinian Territory, Occupied': 'PS', 'Panama': 'PA', 'Papua New Guinea': 'PG', 'Paraguay': 'PY', 'Peru': 'PE', 'Philippines': 'PH', 'Pitcairn': 'PN', 'Poland': 'PL', 'Portugal': 'PT', 'Puerto Rico': 'PR', 'Qatar': 'QA', 'Réunion': 'RE', 'Romania': 'RO', 'Russian Federation': 'RU', 'Russia': 'RU', 'Rwanda': 'RW', 'Saint Helena, Ascension and Tristan da Cunha': 'SH', 'Saint Kitts and Nevis': 'KN', 'Saint Lucia': 'LC', 'Saint Pierre and Miquelon': 'PM', 'Saint Vincent and the Grenadines': 'VC', 'Saint Vincent & the Grenadines': 'VC', 'St. Vincent and the Grenadines': 'VC', 'Samoa': 'WS', 'San Marino': 'SM', 'Sao Tome and Principe': 'ST', 'Saudi Arabia': 'SA', 'Senegal': 'SN', 'Serbia': 'RS', 'Seychelles': 'SC', 'Sierra Leone': 'SL', 'Singapore': 'SG', 'Slovakia': 'SK', 'Slovenia': 'SI', 'Solomon Islands': 'SB', 'Somalia': 'SO', 'South Africa': 'ZA', 'South Georgia and the South Sandwich Islands': 'GS', 'South Sudan': 'SS', 'Spain': 'ES', 'Sri Lanka': 'LK', 'Sudan': 'SD', 'Suriname': 'SR', 'Svalbard and Jan Mayen': 'SJ', 'Swaziland': 'SZ', 'Sweden': 'SE', 'Switzerland': 'CH', 'Syrian Arab Republic': 'SY', 'Taiwan, Province of China': 'TW', 'Taiwan': 'TW', 'Tajikistan': 'TJ', 'Tanzania, United Republic of': 'TZ', 'Thailand': 'TH', 'Timor-Leste': 'TL', 'Togo': 'TG', 'Tokelau': 'TK', 'Tonga': 'TO', 'Trinidad and Tobago': 'TT', 'Tunisia': 'TN', 'Turkey': 'TR', 'Turkmenistan': 'TM', 'Turks and Caicos Islands': 'TC', 'Tuvalu': 'TV', 'Uganda': 'UG', 'Ukraine': 'UA', 'United Arab Emirates': 'AE', 'United Kingdom': 'GB', 'United States': 'US', 'United States Minor Outlying Islands': 'UM', 'Uruguay': 'UY', 'Uzbekistan': 'UZ', 'Vanuatu': 'VU', 'Venezuela, Bolivarian Republic of': 'VE', 'Venezuela': 'VE', 'Viet Nam': 'VN', 'Vietnam': 'VN', 'Virgin Islands, British': 'VG', 'Virgin Islands, U.S.': 'VI', 'Wallis and Futuna': 'WF', 'Western Sahara': 'EH', 'Yemen': 'YE', 'Zambia': 'ZM', 'Zimbabwe': 'ZW'}

for country in countries:
    url = "https://silhouettegarden.com/files/images//"+country.lower()+"-silhouette-thumbnail.png"
    url = url.replace(" ", "-")
    try:
        if not os.path.isfile("countries\\"+countries[country]+".png"):
            resp = requests.get(url, stream=True)
            resp.raw.decode_content
            pic = Image.open(resp.raw)
            pic.save("countries\\"+countries[country]+".png")
            print("countries\\"+countries[country]+".png")
        print(url)
    except Exception:
        pass
'''

'''
# list country codes that are on bciwiki without a corresponding PNG
files = os.listdir("countries")
countries1 = []
for f in files:
    countries1 += [f.replace(".png", "")]
print(countries1)
countries2 = ['NO', 'KR', 'RS', 'CO', 'UY', 'SA', 'LT', 'ID', 'RU', 'SG', 'IE', 'IN', 'JP', 'HR', 'SE', 'FI', 'MY', 'ES', 'HU', 'TR', 'SK', 'FR', 'CH', 'PT', 'SI', 'DE', 'IT', 'CN', 'IL', 'BE', 'DK', 'NL', 'AU', 'PL', 'CZ', 'UK', 'US', 'RO', 'AT', 'CA']
for country in countries2:
    if country not in countries1:
        print(country)
'''

testmode = False
countries = {'UK': 'United Kingdom', 'AF': 'Afghanistan', 'AL': 'Albania', 'DZ': 'Algeria', 'AS': 'American Samoa', 'AD': 'Andorra', 'AO': 'Angola', 'AI': 'Anguilla', 'AQ': 'Antarctica', 'AG': 'Antigua and Barbuda', 'AR': 'Argentina', 'AM': 'Armenia', 'AW': 'Aruba', 'AU': 'Australia', 'AT': 'Austria', 'AZ': 'Azerbaijan', 'BS': 'Bahamas', 'BH': 'Bahrain', 'BD': 'Bangladesh', 'BB': 'Barbados', 'BY': 'Belarus', 'BE': 'Belgium', 'BZ': 'Belize', 'BJ': 'Benin', 'BM': 'Bermuda', 'BT': 'Bhutan', 'BO': 'Bolivia', 'BA': 'Bosnia and Herzegovina', 'BW': 'Botswana', 'BV': 'Bouvet Island', 'BR': 'Brazil', 'IO': 'British Indian Ocean Territory', 'BN': 'Brunei', 'BG': 'Bulgaria', 'BF': 'Burkina Faso', 'BI': 'Burundi', 'KH': 'Cambodia', 'CM': 'Cameroon', 'CA': 'Canada', 'CV': 'Cape Verde', 'KY': 'Cayman Islands', 'CF': 'Central African Republic', 'TD': 'Chad', 'CL': 'Chile', 'CN': 'China', 'CX': 'Christmas Island', 'CC': 'Cocos (Keeling) Islands', 'CO': 'Colombia', 'KM': 'Comoros', 'CG': 'Congo', 'CD': 'Congo, the Democratic Republic of the', 'CK': 'Cook Islands', 'CR': 'Costa Rica', 'CI': 'Ivory Coast', 'HR': 'Croatia', 'CU': 'Cuba', 'CY': 'Cyprus', 'CZ': 'Czech Republic', 'DK': 'Denmark', 'DJ': 'Djibouti', 'DM': 'Dominica', 'DO': 'Dominican Republic', 'EC': 'Ecuador', 'EG': 'Egypt', 'SV': 'El Salvador', 'GQ': 'Equatorial Guinea', 'ER': 'Eritrea', 'EE': 'Estonia', 'ET': 'Ethiopia', 'FK': 'Falkland Islands (Malvinas)', 'FO': 'Faroe Islands', 'FJ': 'Fiji', 'FI': 'Finland', 'FR': 'France', 'GF': 'French Guiana', 'PF': 'French Polynesia', 'TF': 'French Southern Territories', 'GA': 'Gabon', 'GM': 'Gambia', 'GE': 'Georgia', 'DE': 'Germany', 'GH': 'Ghana', 'GI': 'Gibraltar', 'GR': 'Greece', 'GL': 'Greenland', 'GD': 'Grenada', 'GP': 'Guadeloupe', 'GU': 'Guam', 'GT': 'Guatemala', 'GG': 'Guernsey', 'GN': 'Guinea', 'GW': 'Guinea-Bissau', 'GY': 'Guyana', 'HT': 'Haiti', 'HM': 'Heard Island and McDonald Islands', 'VA': 'Holy See (Vatican City State)', 'HN': 'Honduras', 'HK': 'Hong Kong', 'HU': 'Hungary', 'IS': 'Iceland', 'IN': 'India', 'ID': 'Indonesia', 'IR': 'Iran, Islamic Republic of', 'IQ': 'Iraq', 'IE': 'Ireland', 'IM': 'Isle of Man', 'IL': 'Israel', 'IT': 'Italy', 'JM': 'Jamaica', 'JP': 'Japan', 'JE': 'Jersey', 'JO': 'Jordan', 'KZ': 'Kazakhstan', 'KE': 'Kenya', 'KI': 'Kiribati', 'KP': "Korea, Democratic People's Republic of", 'KR': 'South Korea', 'KW': 'Kuwait', 'KG': 'Kyrgyzstan', 'LA': "Lao People's Democratic Republic", 'LV': 'Latvia', 'LB': 'Lebanon', 'LS': 'Lesotho', 'LR': 'Liberia', 'LY': 'Libya', 'LI': 'Liechtenstein', 'LT': 'Lithuania', 'LU': 'Luxembourg', 'MO': 'Macao', 'MK': 'Macedonia, the former Yugoslav Republic of', 'MG': 'Madagascar', 'MW': 'Malawi', 'MY': 'Malaysia', 'MV': 'Maldives', 'ML': 'Mali', 'MT': 'Malta', 'MH': 'Marshall Islands', 'MQ': 'Martinique', 'MR': 'Mauritania', 'MU': 'Mauritius', 'YT': 'Mayotte', 'MX': 'Mexico', 'FM': 'Micronesia, Federated States of', 'MD': 'Moldova, Republic of', 'MC': 'Monaco', 'MN': 'Mongolia', 'ME': 'Montenegro', 'MS': 'Montserrat', 'MA': 'Morocco', 'MZ': 'Mozambique', 'MM': 'Burma', 'NA': 'Namibia', 'NR': 'Nauru', 'NP': 'Nepal', 'NL': 'Netherlands', 'AN': 'Netherlands Antilles', 'NC': 'New Caledonia', 'NZ': 'New Zealand', 'NI': 'Nicaragua', 'NE': 'Niger', 'NG': 'Nigeria', 'NU': 'Niue', 'NF': 'Norfolk Island', 'MP': 'Northern Mariana Islands', 'NO': 'Norway', 'OM': 'Oman', 'PK': 'Pakistan', 'PW': 'Palau', 'PS': 'Palestinian Territory, Occupied', 'PA': 'Panama', 'PG': 'Papua New Guinea', 'PY': 'Paraguay', 'PE': 'Peru', 'PH': 'Philippines', 'PN': 'Pitcairn', 'PL': 'Poland', 'PT': 'Portugal', 'PR': 'Puerto Rico', 'QA': 'Qatar', 'RE': 'Réunion', 'RO': 'Romania', 'RU': 'Russia', 'RW': 'Rwanda', 'SH': 'Saint Helena, Ascension and Tristan da Cunha', 'KN': 'Saint Kitts and Nevis', 'LC': 'Saint Lucia', 'PM': 'Saint Pierre and Miquelon', 'VC': 'St. Vincent and the Grenadines', 'WS': 'Samoa', 'SM': 'San Marino', 'ST': 'Sao Tome and Principe', 'SA': 'Saudi Arabia', 'SN': 'Senegal', 'RS': 'Serbia', 'SC': 'Seychelles', 'SL': 'Sierra Leone', 'SG': 'Singapore', 'SK': 'Slovakia', 'SI': 'Slovenia', 'SB': 'Solomon Islands', 'SO': 'Somalia', 'ZA': 'South Africa', 'GS': 'South Georgia and the South Sandwich Islands', 'SS': 'South Sudan', 'ES': 'Spain', 'LK': 'Sri Lanka', 'SD': 'Sudan', 'SR': 'Suriname', 'SJ': 'Svalbard and Jan Mayen', 'SZ': 'Swaziland', 'SE': 'Sweden', 'CH': 'Switzerland', 'SY': 'Syrian Arab Republic', 'TW': 'Taiwan', 'TJ': 'Tajikistan', 'TZ': 'Tanzania, United Republic of', 'TH': 'Thailand', 'TL': 'Timor-Leste', 'TG': 'Togo', 'TK': 'Tokelau', 'TO': 'Tonga', 'TT': 'Trinidad and Tobago', 'TN': 'Tunisia', 'TR': 'Turkey', 'TM': 'Turkmenistan', 'TC': 'Turks and Caicos Islands', 'TV': 'Tuvalu', 'UG': 'Uganda', 'UA': 'Ukraine', 'AE': 'United Arab Emirates', 'GB': 'United Kingdom', 'US': 'United States', 'UM': 'United States Minor Outlying Islands', 'UY': 'Uruguay', 'UZ': 'Uzbekistan', 'VU': 'Vanuatu', 'VE': 'Venezuela', 'VN': 'Vietnam', 'VG': 'Virgin Islands, British', 'VI': 'Virgin Islands, U.S.', 'WF': 'Wallis and Futuna', 'EH': 'Western Sahara', 'YE': 'Yemen', 'ZM': 'Zambia', 'ZW': 'Zimbabwe'}
background_colors = [(255, 154, 162), (255, 183, 178), (255, 218, 193), (226, 240, 203), (181, 234, 215), (199, 206, 234)]
font = ImageFont.truetype("fonts\\DejaVuSans-Bold.ttf", 50)
font2 = ImageFont.truetype("fonts\\DejaVuSans.ttf", 50)
font3 = ImageFont.truetype("fonts\\DejaVuSans-Italic.ttf", 30)

# get neuroimaging/stimulation technique descriptions
neuroimaging_techniques = {"EEG": "Electroencephalography (EEG) is an electrophysiological monitoring method to record electrical activity of the brain. It is typically noninvasive, with the electrodes placed along the scalp, although invasive electrodes are sometimes used, as in electrocorticography, sometimes called intracranial EEG.",
"Electrocardiography": "Electrocardiography is the process of producing an electrocardiogram (ECG or EKG). It is a graph of voltage versus time of the electrical activity of the heart using electrodes placed on the skin. These electrodes detect the small electrical changes that are a consequence of cardiac muscle depolarization followed by repolarization during each cardiac cycle (heartbeat).",
"ECG": "Electrocardiography(ECG) is the process of producing an electrocardiogram (ECG or EKG). It is a graph of voltage versus time of the electrical activity of the heart using electrodes placed on the skin. These electrodes detect the small electrical changes that are a consequence of cardiac muscle depolarization followed by repolarization during each cardiac cycle (heartbeat).",
"EKG": "Electrocardiography(EKG) is the process of producing an electrocardiogram (ECG or EKG). It is a graph of voltage versus time of the electrical activity of the heart using electrodes placed on the skin. These electrodes detect the small electrical changes that are a consequence of cardiac muscle depolarization followed by repolarization during each cardiac cycle (heartbeat).",
"Electromyography": "Electromyography (EMG) is an electrodiagnostic medicine technique for evaluating and recording the electrical activity produced by skeletal muscles.",
"EMG": "Electromyography (EMG) is an electrodiagnostic medicine technique for evaluating and recording the electrical activity produced by skeletal muscles.",
"ENG": "An electroneurogram is a method used to visualize directly recorded electrical activity of neurons in the central nervous system (brain, spinal cord) or the peripheral nervous system (nerves, ganglions). The acronym ENG is often used. An electroneurogram is similar to an electromyogram (EMG), but the latter is used to visualize muscular activity. An electroencephalogram (EEG) is a particular type of electroneurogram in which several electrodes are placed around the head and the general activity of the brain is recorded, without having very high resolution to distinguish between the activity of different groups of neurons.",
"FMRI": "Functional magnetic resonance imaging or functional MRI (fMRI) measures brain activity by detecting changes associated with blood flow. This technique relies on the fact that cerebral blood flow and neuronal activation are coupled. When an area of the brain is in use, blood flow to that region also increases.",
"FNIRS": "Functional near-infrared spectroscopy (fNIRS) is an optical brain monitoring technique which uses near-infrared spectroscopy for the purpose of functional neuroimaging. Using fNIRS, brain activity is measured by using near-infrared light to estimate cortical hemodynamic activity which occur in response to neural activity.",
"FUS": "Functional ultrasound imaging (fUS) is a medical ultrasound imaging technique of detecting or measuring changes in neural activities or metabolism, for example, the loci of brain activity, typically through measuring blood flow or hemodynamic changes. The method can be seen as an extension of Doppler imaging.",
"IEEG": "Intracranial electroencephalography (iEEG) comes in two forms, Electrocorticography (ECoG) and Stereoelectroencephalography (SEEG).",
"MEG": "Magnetoencephalography (MEG) is a functional neuroimaging technique for mapping brain activity by recording magnetic fields produced by electrical currents occurring naturally in the brain, using very sensitive magnetometers. Arrays of SQUIDs (superconducting quantum interference devices) are currently the most common magnetometer, while the SERF (spin exchange relaxation-free) magnetometer is being investigated for future machines.",
"MRI": "Magnetic resonance imaging (MRI) is a medical imaging technique used in radiology to form pictures of the anatomy and the physiological processes of the body. MRI scanners use strong magnetic fields, magnetic field gradients, and radio waves to generate images of the organs in the body.",
"MWT": "Microwave tomography (MWT) is an emerging biomedical imaging modality with great potential for non-invasive assessment of functional and pathological conditions of soft tissues.",
"NIRS": "Near-infrared spectroscopy (NIRS) is a spectroscopic method that uses the near-infrared region of the electromagnetic spectrum (from 780 nm to 2500 nm).",
"Optogenetics": "Optogenetics most commonly refers to a biological technique that involves the use of light to control neurons that have been genetically modified to express light-sensitive ion channels. As such, optogenetics is a neuromodulation method that uses a combination of techniques from optics and genetics to control the activities of individual neurons in living tissue even within freely-moving animals. In some usages, optogenetics also refers to optical monitoring of neuronal activity or control of other biochemical pathways in non-neuronal cells, although these research activities preceded the use of light-sensitive ion channels in neurons.",
"PET": "Positron emission tomography (PET) is a functional imaging technique that uses radioactive substances known as radiotracers to visualize and measure changes in metabolic processes, and in other physiological activities including blood flow, regional chemical composition, and absorption. Different tracers are used for various imaging purposes, depending on the target process within the body.",
"PIR": "Developed by Dr. Jeffrey Carmen, a privately practicing psychologist in New York, passive infrared HEG is a marriage of the classic hemoencephalography principles employed by Toomim and a technique known as thermoscopy. PIR uses a sensor similar to the NIR sensor to detect light from a narrow band of the infrared spectrum that corresponds to the amount of heat being generated by an active brain region, as well as the local blood oxygenation level. The heat detected by PIR is proportional to the amount of sugar being burned to maintain the increased metabolic rate necessary to fuel elevated neuronal activity. PIR has a poorer resolution than NIR and this treatment typically focuses on more global increases in cerebral blood flow.",
"TCD": "Transcranial Doppler (TCD) and transcranial color Doppler (TCCD) are types of Doppler ultrasonography that measure the velocity of blood flow through the brain\'s blood vessels by measuring the echoes of ultrasound waves moving transcranially (through the cranium). These modes of medical imaging conduct a spectral analysis of the acoustic signals they receive and can therefore be classified as methods of active acoustocerebrography.",
"Neuos": "Neuos is an EEG-software platform that decodes feelings, reactions, and cognitive states using a matrix of proprietary algorithms."}
'''
resp = str(requests.get("https://bciwiki.org/index.php/Category:Neurosensing_Techniques").content)
resp = resp.split('<li>')[1:]
print("{")
for technique in resp:
    technique = technique.split(">")[1]
    technique = technique.split("<")[0]
    desc = str(requests.get("https://bciwiki.org/index.php/"+technique).content)
    desc = desc.split("<p>")[2]
    desc = desc.split("</p>")[0]
    desc = desc.replace("\\n", "")
    print('"'+technique+'": "'+desc+'",')
    neuroimaging_techniques[technique] = desc
input("}")
'''
neurostimulation_techniques = {"CES": "Cranial electrotherapy stimulation (CES) is a form of neurostimulation that delivers a small, pulsed, alternating current via electrodes on the head. CES is used with the intention of treating a variety of conditions such as anxiety, depression and insomnia.",
"CNS": "Among other neuromodulation approaches such as peripheral, transcranial and deep brain stimulation, cranial nerve stimulation is unique in allowing axon pathway-specific engagement of brain circuits, including thalamo-cortical networks.",
"DBS": "Deep brain stimulation (DBS) is a neurosurgical procedure involving the placement of a medical device called a neurostimulator (sometimes referred to as a \"brain pacemaker\"), which sends electrical impulses, through implanted electrodes, to specific targets in the brain (brain nuclei) for the treatment of movement disorders, including Parkinson\'s disease, essential tremor, and dystonia. While its underlying principles and mechanisms are not fully understood, DBS directly changes brain activity in a controlled manner.",
"EBS": "Electrical brain stimulation (EBS), also referred to as focal brain stimulation (FBS), is a form of electrotherapy and technique used in research and clinical neurobiology to stimulate a neuron or neural network in the brain through the direct or indirect excitation of its cell membrane by using an electric current. It is used for research or for therapeutic purposes.",
"EMS": "Electrical muscle stimulation (EMS), also known as neuromuscular electrical stimulation (NMES) or electromyostimulation, is the elicitation of muscle contraction using electric impulses.",
"HNS": "Hypoglossal nerve stimulation (HNS) decreases obstructive sleep apnoea (OSA) severity via genioglossus muscle activation and decreased upper airway collapsibility.",
"Microstimulation": "Microstimulation is a technique that stimulates a small population of neurons by passing a small electrical current through a nearby microelectrode.",
"Optogenetics": "Optogenetics most commonly refers to a biological technique that involves the use of light to control neurons that have been genetically modified to express light-sensitive ion channels. As such, optogenetics is a neuromodulation method that uses a combination of techniques from optics and genetics to control the activities of individual neurons in living tissue even within freely-moving animals. In some usages, optogenetics also refers to optical monitoring of neuronal activity or control of other biochemical pathways in non-neuronal cells, although these research activities preceded the use of light-sensitive ion channels in neurons.",
"PBM": "Transcranial photobiomodulation (PBM) also known as low level laser therapy (tLLLT) relies on the use of red/NIR light to stimulate, preserve and regenerate cells and tissues. The mechanism of action involves photon absorption in the mitochondria (cytochrome c oxidase), and ion channels in cells leading to activation of signaling pathways, up-regulation of transcription factors, and increased expression of protective genes.",
"PNS": "Peripheral nerve stimulation, frequently referred to as PNS, is a commonly used approach to treat chronic pain. It involves surgery that places a small electrical device (a wire-like electrode) next to one of the peripheral nerves. (These are the nerves that are located beyond the brain or spinal cord). The electrode delivers rapid electrical pulses that are felt like mild tingles (so-called paresthesias). During the testing period (trial), the electrode is connected to an external device, and if the trial is successful, a small generator gets implanted into the patient\xe2\x80\x99s body. Similar to heart pacemakers, electricity is delivered from the generator to the nerve or nerves using one or several electrodes. The patient is able to control stimulation by turning the device on and off and adjusting stimulation parameters as needed.",
"SCS": "Spinal cord stimulation (SCS) is a relatively new technology that can help manage chronic pain when the cause cannot be removed or the injury cannot be repaired. The device consists of a stimulating wire or \xe2\x80\x9celectrode\xe2\x80\x9d or connected to control unit or \xe2\x80\x9cgenerator.\xe2\x80\x9d By placing a stimulating electrode over the spinal cord, the pain signal cannot be sent up from the spine to the brain.",
"SNS": "Sacral Neuromodulation (SNM) (also known as Sacral Nerve Stimulation) is an NHS funded therapy that may be able to help certain people who experience bladder and bowel problems.  Where successful, the treatment can be a life changing therapy. As with all treatments, it is not suitable for everyone and your doctor or specialist healthcare professional will be able to discuss its potential suitability for you, or those you care for.",
"TACS": "Transcranial alternating current stimulation (tACS) and transcranial random noise stimulation (tRNS) are two noninvasive brain stimulation techniques that use electrical currents to modulate brain activity and change behavior. tACS consists of the application of oscillating electrical current to modulate brain activity and tRNS uses random interstimulus-intervals and amplitudes.",
"TAN": "Transcutaneous auricular neurostimulation (tAN), a novel and non-invasive form of electrostimulation, may serve as a promising alternative to morphine.",
"TDCS": "Transcranial direct current stimulation (tDCS) is a form of neuromodulation that uses constant, low direct current delivered via electrodes on the head. It was originally developed to help patients with brain injuries or neuropsychiatric conditions such as major depressive disorder.",
"TENS": "Transcutaneous electrical nerve stimulation (TENS) is a therapy that uses low voltage electrical current to provide pain relief. A TENS unit consists of a battery-powered device that delivers electrical impulses through electrodes placed on the surface of your skin. The electrodes are placed at or near nerves where the pain is located or at trigger points.",
"TES": "Transcranial electrical stimulation (tES) is a noninvasive brain stimulation technique that passes an electrical current through the cortex of the brain in to alter brain function.",
"TFS": "TFS is the acronym for transcranial focal electrical stimulation. TFS is a unique, noninvasive, and focal stimulation modality utilizing novel concentric ring electrodes (CREs). TFS via CREs has a uniform current density and focused stimulation directly below the electrodes with a very steep electric field, which is an advantage over transcranial direct-current stimulation (tDCS) or other transcranial stimulation methods.",
"TFUS": "Transcranial focused ultrasound is an emerging technique for non-invasive neurostimulation. Compared to magnetic or electric non-invasive brain stimulation, this technique has a higher spatial resolution and can reach deep structures. In addition, both animal and human studies suggest that, potentially, different sites of the central and peripheral nervous system can be targeted by this technique.",
"TMS": "Transcranial magnetic stimulation (TMS) is a noninvasive form of brain stimulation in which a changing magnetic field is used to cause electric current at a specific area of the brain through electromagnetic induction. An electric pulse generator, or stimulator, is connected to a magnetic coil, which in turn is connected to the scalp. The stimulator generates a changing electric current within the coil which induces a magnetic field; this field then causes a second inductance of inverted electric charge within the brain itself.",
"TNS": "Trigeminal Nerve Stimulation (TNS) is a novel medical treatment in which mild electrical signals stimulate branches of the trigeminal nerve (the largest cranial nerve) in order to modulate the activity of targeted brain regions. NeuroSigma is developing two embodiments of TNS: eTNSTM (TNS with external electrodes and an external pulse generator) and sTNSTM (subcutaneous electrodes and implantable pulse generator).",
"TPCS": "Transcranial pulsed current stimulation (tPCS) is a non-invasive brain stimulation technique that modulates neuronal activity by delivering oscillatory current to the cortex via surface electrodes placed on the auricular structures (Datta et al., 2013). This method shows promising features as a neuromodulatory tool, as it is simple, painless, easy to use, portable and safe (Castillo Saavedra et al., 2014, Fitzgerald, 2014, Morales-Quezada et al., 2014); however little is known regarding its mechanisms of modifying behaviors.",
"TRNS": "Transcranial random noise stimulation (tRNS) is a non-invasive brain stimulation technique and a form of transcranial electrical stimulation (tES). Terney et al from G\xc3\xb6ttingen University was the first group to apply tRNS in humans in 2008. They showed that by using an alternate current along with random amplitude and frequency (between 0.1 and 640 Hz) in healthy subjects, the motor cortex excitability increased (i.e. increased amplitude of motor evoked potentials) for up to 60 minutes after 10 minutes of stimulation. The study included all the frequencies up to half of the sampling rate (1280 samples/s) i.e. 640 Hz, however the positive effect was limited only to higher frequencies.",
"TSDCS": "Transcutaneous spinal direct current stimulation (tsDCS) is a safe and convenient method of neuromodulation.",
"VNS": "Vagus nerve stimulation (VNS) is a medical treatment that involves delivering electrical impulses to the vagus nerve. It is used as an add-on treatment for certain types of intractable epilepsy and treatment-resistant depression."}
'''
resp = str(requests.get("https://bciwiki.org/index.php/Category:Neurostimulation_Techniques").content)
resp = resp.split('<li>')[1:]
print("{")
for technique in resp:
    technique = technique.split(">")[1]
    technique = technique.split("<")[0]
    desc = str(requests.get("https://bciwiki.org/index.php/"+technique).content)
    desc = desc.split("<p>")[2]
    desc = desc.split("</p>")[0]
    desc = desc.replace("\\n", "")
    print('"'+technique+'": "'+desc+'",')
    neurostimulation_techniques[technique] = desc
input("}")
'''

def pasteImage(newimgname, finalimg, width, x, y):
    newimg = Image.open(r""+newimgname+".png")
    w, h = newimg.size
    newwidth = width
    newheight = int((h/w)*newwidth)
    newimg = newimg.resize((newwidth, newheight))
    finalimg.paste(newimg, (x, y), newimg.convert('RGBA'))
    return newheight+y

def wordWrap(text, max_width, char_length=22):
    max_chars = round(max_width/char_length)
    textlines = []
    textcopy = text
    textfinal = ""
    while len(textcopy) > max_chars:
        if textcopy[max_chars] == " ":
            textlines += [textcopy[:max_chars]]
            textcopy = textcopy[max_chars:]
        else:
            a = 1
            while textcopy[max_chars-a] != " ":
                a += 1
            textlines += [textcopy[:max_chars-a]]
            textcopy = textcopy[max_chars-a:]
    textlines += [textcopy]
    for textline in textlines:
        textfinal += textline+"\n"
    spaceradd = len(textlines)*75
    if spaceradd > 750:
        spaceradd = 750
    return spaceradd, textfinal

# collect categorized company data
resp = str(requests.get("https://bciwiki.org/index.php/Category:Companies").content)
resp = resp.split("</th></tr>")[1]
resp = resp.split("</tbody>")[0]
companies = resp.split("<tr>")
companynames = []
allcompanyinfo = [[]]
allcompanyindex = 0
for a in range(1, len(companies)):
    companyinfo = companies[a].split("<td>")
    for b in range(1, len(companyinfo)):
        if "<a" in companyinfo[b]:
            names = companyinfo[b].split('<a href="')[1:]
            name = ""
            for n in names:
                n = n.split('"')[0]
                if len(names) > 1:
                    n = " "+n.split("/")[2]+","
                else:
                    n = n.split("/")[2]
                name += n
            if len(names) > 1:
                name = name[:-1]
            allcompanyinfo[allcompanyindex] += [name]
        else:
            info = companyinfo[b].split("\\n</td>")[0]
            allcompanyinfo[allcompanyindex] += [info]
        if b == 11:
            allcompanyindex += 1
            allcompanyinfo += [[]]
allcompanyinfo.pop()

for companyinfo in allcompanyinfo:
    if not os.path.exists("companyprofiles\\"+companyinfo[0]+".png"):
        # create template background based on most common logo color
        # combine logo and country layers
        companylogo = Image.open(r"images\\"+companyinfo[0]+".png").convert('RGBA')
        w, h = companylogo.size
        px = companylogo.load()
        print("images\\"+companyinfo[0]+".png")
        pixelcolors = {}
        for pixelrow in range(2, 20):
            for pixelcol in range(2, 20):
                currentcolor = companylogo.getpixel((round(w/pixelcol), round(h/pixelrow)))
                if currentcolor in pixelcolors:
                    pixelcolors[currentcolor] += 1
                else:
                    pixelcolors[currentcolor] = 1
        maincolor = ""
        maincolorval = 0
        print(pixelcolors)
        for color in pixelcolors:
            if type(color) == type(1):
                if pixelcolors[color] > maincolorval:
                    maincolorval = pixelcolors[color]
                    maincolor = color
            else:
                if pixelcolors[color] > maincolorval and (len(color) < 4 or color[3] > 0):
                    maincolorval = pixelcolors[color]
                    maincolor = color
        print(maincolor)
        lightlogo = False
        if type(maincolor) == type(1):
            if maincolor > 128:
                lightlogo = True
        elif type(maincolor) != type(""):
            if (maincolor[0] > 128 and (maincolor[1] > 128 or maincolor[2] > 128)) or (maincolor[1] > 128 and maincolor[2] > 128):
                lightlogo = True

        if lightlogo:
            # light logo
            colorpallete = {'fonts':
                            {'h1': {'font': ImageFont.truetype("fonts\\Muli-Bold.ttf", 40), 'color': (255, 255, 255)},
                             'h2': {'font': ImageFont.truetype("fonts\\Kollektif.ttf", 66), 'color': (172, 213, 230)},
                             'h3': {'font': ImageFont.truetype("fonts\\Kollektif.ttf", 66), 'color': (0, 63, 100)},
                             'p1': {'font': ImageFont.truetype("fonts\\Muli.ttf", 30), 'color': (255, 255, 255)},
                             'p2': {'font': ImageFont.truetype("fonts\\Muli.ttf", 30), 'color': (0, 63, 100)},
                             'p3': {'font': ImageFont.truetype("fonts\\Muli-Bold.ttf", 45), 'color': (0, 63, 100)}},
                            'colors': {'bg1': (0, 63, 100), 'bg2': (233, 235, 255), 'logoext': '-light'}
                            }
        else:
            # dark logo
            colorpallete = {'fonts':
                            {'h1': {'font': ImageFont.truetype("fonts\\Muli-Bold.ttf", 40), 'color': (0, 0, 0)},
                             'h2': {'font': ImageFont.truetype("fonts\\Kollektif.ttf", 66), 'color': (0, 63, 100)},
                             'h3': {'font': ImageFont.truetype("fonts\\Kollektif.ttf", 66), 'color': (172, 213, 230)},
                             'p1': {'font': ImageFont.truetype("fonts\\Muli.ttf", 30), 'color': (0, 0, 0)},
                             'p2': {'font': ImageFont.truetype("fonts\\Muli.ttf", 30), 'color': (172, 213, 230)},
                             'p3': {'font': ImageFont.truetype("fonts\\Muli-Bold.ttf", 45), 'color': (172, 213, 230)}},
                            'colors': {'bg1': (233, 235, 255), 'bg2': (0, 63, 100), 'logoext': '-dark'}
                            }
        
        finalwidth = 1400
        newwidth = int(finalwidth/2)
        newheight = int((h/w)*newwidth)
        companylogo = companylogo.resize((newwidth, newheight))

        topspacer = newheight+150
        randomcolor = random.randint(0, len(background_colors)-1)
        finalimg = Image.new('RGBA', (finalwidth, newheight+15000), colorpallete['colors']['bg1'])
        finalimg.paste(companylogo, (350, 100), companylogo)

        
        # company name title
        d = ImageDraw.Draw(finalimg)
        d.text((finalwidth/2, 50), companyinfo[0].replace("_", " "), fill=colorpallete['fonts']['h1']['color'], anchor="ms", font=colorpallete['fonts']['h1']['font'])
        d.text((finalwidth/2, topspacer), "An introduction by BCIwiki.org", fill=colorpallete['fonts']['h1']['color'], anchor="ms", font=colorpallete['fonts']['h1']['font'])
        d.line([(200, topspacer+25), (finalwidth-200, topspacer+25)], fill=colorpallete['colors']['bg2'], width=7)
        

        # country and founding year
        d.text((finalwidth/2, topspacer+150), "Founded in", fill=colorpallete['fonts']['p1']['color'], anchor="la", font=colorpallete['fonts']['p1']['font'])
        d.text((finalwidth/2, topspacer+200), countries[companyinfo[5]], fill=colorpallete['fonts']['h2']['color'], anchor="la", font=colorpallete['fonts']['h2']['font'])
        d.text((finalwidth/2, topspacer+260), "around", fill=colorpallete['fonts']['p1']['color'], anchor="la", font=colorpallete['fonts']['p1']['font'])
        d.text((finalwidth/2, topspacer+310), companyinfo[6], fill=colorpallete['fonts']['h2']['color'], anchor="la", font=colorpallete['fonts']['h2']['font'])
        topspacer = pasteImage("countries\\"+companyinfo[5]+colorpallete['colors']['logoext'], finalimg, 550, 75, topspacer)
        
        d.rectangle([(0, topspacer), (finalwidth, topspacer+2500)], fill=colorpallete['colors']['bg2'])
        pasteImage("icons\\triangle", finalimg, 150, int(finalwidth/2)-75, topspacer-70)
        topspacer += 150
        # invasive and/or noninvasive icons+text
        d.text((finalwidth/2, topspacer), "Produces", fill=colorpallete['fonts']['p2']['color'], anchor="ms", font=colorpallete['fonts']['p2']['font'])
        topspacer += 25
        if companyinfo[1] == 'True' or testmode:
            d.text((finalwidth/2, topspacer+60), "noninvasive hardware", fill=colorpallete['fonts']['h3']['color'], anchor="ms", font=colorpallete['fonts']['h3']['font'])
            topspacer += 60
        if companyinfo[2] == 'True' or testmode:
            d.text((finalwidth/2, topspacer+60), "invasive hardware", fill=colorpallete['fonts']['h3']['color'], anchor="ms", font=colorpallete['fonts']['h3']['font'])
            topspacer += 60

        # software and/or dev tools text
        if companyinfo[3] == 'True' or testmode:
            d.text((finalwidth/2, topspacer+60), "end-user software", fill=colorpallete['fonts']['h3']['color'], anchor="ms", font=colorpallete['fonts']['h3']['font'])
            topspacer += 60
        if companyinfo[4] == 'True' or testmode:
            d.text((finalwidth/2, topspacer+60), "developer tools", fill=colorpallete['fonts']['h3']['color'], anchor="ms", font=colorpallete['fonts']['h3']['font'])
            topspacer += 60
        if companyinfo[1] == 'False' and companyinfo[2] == 'False' and companyinfo[3] == 'False' and companyinfo[4] == 'False':
            d.text((finalwidth/2, topspacer+60), "neurotech consulting services", fill=colorpallete['fonts']['h3']['color'], anchor="ms", font=colorpallete['fonts']['h3']['font'])
            topspacer += 60
        topspacer += 200
        d.rectangle([(0, topspacer), (finalwidth, topspacer+2500)], fill=colorpallete['colors']['bg1'])
        pasteImage("icons\\triangle", finalimg, 150, int(finalwidth/2)-75, topspacer-70)

        # application cetegories
        topspacer += 150
        d.text((finalwidth/2, topspacer), "Makes tools for", fill=colorpallete['fonts']['p1']['color'], anchor="ms", font=colorpallete['fonts']['p1']['font'])
        first = True
        if 'Clinical' in companyinfo[7] or testmode:
            topspacer += 100
            if not first:
                topspacer += 150
            first = False
            d.text((finalwidth/2, topspacer), "medical diagnosis and treatment through", fill=colorpallete['fonts']['h2']['color'], anchor="mm", font=colorpallete['fonts']['h2']['font'])
            d.text((finalwidth/2, topspacer+60), "body/mind state interpretation and/or", fill=colorpallete['fonts']['h2']['color'], anchor="mm", font=colorpallete['fonts']['h2']['font'])
            d.text((finalwidth/2, topspacer+120), "neurostimulation therapies", fill=colorpallete['fonts']['h2']['color'], anchor="mm", font=colorpallete['fonts']['h2']['font'])
        if 'RC/UI' in companyinfo[7] or testmode:
            topspacer += 100
            if not first:
                topspacer += 150
            first = False
            d.text((finalwidth/2, topspacer), "the assisted control of mechanical,", fill=colorpallete['fonts']['h2']['color'], anchor="mm", font=colorpallete['fonts']['h2']['font'])
            d.text((finalwidth/2, topspacer+60), "electrical, and digital devices/applications", fill=colorpallete['fonts']['h2']['color'], anchor="mm", font=colorpallete['fonts']['h2']['font'])
        if 'Subjective Measurement' in companyinfo[7] or testmode:
            topspacer += 100
            if not first:
                topspacer += 150
            first = False
            d.text((finalwidth/2, topspacer), "the objective measurement of subjective", fill=colorpallete['fonts']['h2']['color'], anchor="mm", font=colorpallete['fonts']['h2']['font'])
            d.text((finalwidth/2, topspacer+60), "experiences through mind/body state", fill=colorpallete['fonts']['h2']['color'], anchor="mm", font=colorpallete['fonts']['h2']['font'])
            d.text((finalwidth/2, topspacer+120), "interpretation", fill=colorpallete['fonts']['h2']['color'], anchor="mm", font=colorpallete['fonts']['h2']['font'])
        if 'Motor-Sensory Augmentation' in companyinfo[7] or testmode:
            topspacer += 100
            if not first:
                topspacer += 150
            first = False
            d.text((finalwidth/2, topspacer), "feedback through neurostimulation techniques", fill=colorpallete['fonts']['h2']['color'], anchor="mm", font=colorpallete['fonts']['h2']['font'])
        if 'Wetwear Computing' in companyinfo[7] or testmode:
            topspacer += 100
            if not first:
                topspacer += 150
            first = False
            d.text((finalwidth/2, topspacer), "the sensing and stimulation of in vitro", fill=colorpallete['fonts']['h2']['color'], anchor="mm", font=colorpallete['fonts']['h2']['font'])
            d.text((finalwidth/2, topspacer+60), "neural networks to perform calculations", fill=colorpallete['fonts']['h2']['color'], anchor="mm", font=colorpallete['fonts']['h2']['font'])
        topspacer += 300
        d.rectangle([(0, topspacer), (finalwidth, topspacer+6500)], fill=colorpallete['colors']['bg2'])
        pasteImage("icons\\triangle", finalimg, 150, int(finalwidth/2)-75, topspacer-70)

        # bci categories
        subtitletext = "category"
        if "," in companyinfo[8]:
            subtitletext = "categories"
        textimg = Image.new('RGBA', (300, 300), colorpallete['colors']['bg2'])
        d2 = ImageDraw.Draw(textimg)
        d2.text((150, 25), "BCI", fill=colorpallete['fonts']['p3']['color'], anchor="mm", font=colorpallete['fonts']['p3']['font'])
        d2.text((150, 75), subtitletext, fill=colorpallete['fonts']['p3']['color'], anchor="mm", font=colorpallete['fonts']['p3']['font'])
        textimgrot = textimg.rotate(90)
        commacount = companyinfo[8].count(",")+1
        finalimg.paste(textimgrot, (50, topspacer+commacount*150), textimgrot.convert('RGBA'))
        topspacertmp = topspacer
        topspacer += 150
        first = True
        if 'Open-Loop Efferent BCI' in companyinfo[8] or testmode:
            topspacer += 100
            first = False
            d.text((finalwidth/4, topspacer), "Open-Loop Efferent BCI", fill=colorpallete['fonts']['h3']['color'], anchor="la", font=colorpallete['fonts']['h3']['font'])
            d.text((finalwidth/4, topspacer+100), "Brain signals control an external device", fill=colorpallete['fonts']['p2']['color'], anchor="la", font=colorpallete['fonts']['p2']['font'])
        if 'Open-Loop Afferent BCI' in companyinfo[8] or testmode:
            topspacer += 100
            if not first:
                topspacer += 150
            first = False
            d.text((finalwidth/4, topspacer), "Open-Loop Afferent BCI", fill=colorpallete['fonts']['h3']['color'], anchor="la", font=colorpallete['fonts']['h3']['font'])
            d.text((finalwidth/4, topspacer+100), "Electrical stimulation to the brain by a device", fill=colorpallete['fonts']['p2']['color'], anchor="la", font=colorpallete['fonts']['p2']['font'])
        if 'Closed-Loop Efferent BCI' in companyinfo[8] or testmode:
            topspacer += 100
            if not first:
                topspacer += 150
            first = False
            d.text((finalwidth/4, topspacer), "Closed-Loop Efferent BCI", fill=colorpallete['fonts']['h3']['color'], anchor="la", font=colorpallete['fonts']['h3']['font'])
            d.text((finalwidth/4, topspacer+100), "Brain signals control an external device\nand then feedback is given to the user that\nenables them to change brain signals", fill=colorpallete['fonts']['p2']['color'], anchor="la", font=colorpallete['fonts']['p2']['font'])
        if 'Closed-Loop Afferent BCI' in companyinfo[8] or testmode:
            topspacer += 100
            if not first:
                topspacer += 150
            first = False
            d.text((finalwidth/4, topspacer), "Closed-Loop Afferent BCI", fill=colorpallete['fonts']['h3']['color'], anchor="la", font=colorpallete['fonts']['h3']['font'])
            d.text((finalwidth/4, topspacer+100), "Electrical stimulation to the brain by\na device and moderated by movement monitoring.", fill=colorpallete['fonts']['p2']['color'], anchor="la", font=colorpallete['fonts']['p2']['font'])
        if 'Bidirectional Afferent Closed-Loop BCI' in companyinfo[8] or testmode:
            topspacer += 100
            if not first:
                topspacer += 150
            first = False
            d.text((finalwidth/4, topspacer), "Bidirectional Afferent Closed-Loop\nBCI", fill=colorpallete['fonts']['h3']['color'], anchor="la", font=colorpallete['fonts']['h3']['font'])
            d.text((finalwidth/4, topspacer+120), "Electrical stimulation to the brain is modulated\ndepending on the recordings.", fill=colorpallete['fonts']['p2']['color'], anchor="la", font=colorpallete['fonts']['p2']['font'])

        # neuroimaging techniques
        if companyinfo[9] != "" or testmode:
            topspacer += 200
            subtitletext = "Technique"
            if "," in companyinfo[9]:
                subtitletext = "Techniques"
            textimg = Image.new('RGBA', (400, 400), colorpallete['colors']['bg2'])
            d2 = ImageDraw.Draw(textimg)
            d2.text((200, 25), "Neuroimaging", fill=colorpallete['fonts']['p3']['color'], anchor="mm", font=colorpallete['fonts']['p3']['font'])
            d2.text((200, 75), subtitletext, fill=colorpallete['fonts']['p3']['color'], anchor="mm", font=colorpallete['fonts']['p3']['font'])
            textimgrot = textimg.rotate(90)
            textimgrot = textimgrot.crop((0, 0, 200, 400))
            finalimg.paste(textimgrot, (50, topspacer), textimgrot.convert('RGBA'))
            first = True
            topspaceradd = 0
            for neuroimaging_technique in neuroimaging_techniques:
                if neuroimaging_technique.lower() == companyinfo[9].lower() or " "+neuroimaging_technique.lower() in companyinfo[9].lower() or testmode:
                    topspaceradd, imaging_text = wordWrap(neuroimaging_techniques[neuroimaging_technique], 1400)
                    d.text((finalwidth/4, topspacer+75), neuroimaging_technique, fill=colorpallete['fonts']['h3']['color'], anchor="la", font=colorpallete['fonts']['h3']['font'])
                    d.text((finalwidth/4, topspacer+175), imaging_text, fill=colorpallete['fonts']['p2']['color'], anchor="la", font=colorpallete['fonts']['p2']['font'])
                    topspacer += topspaceradd
            if topspaceradd < 400 and companyinfo[10] == "":
                    topspacer += 400
        
        # neurostimulation techniques
        if companyinfo[10] != "" or testmode:
            topspacer += 200
            subtitletext = "Technique"
            if "," in companyinfo[9]:
                subtitletext = "Techniques"
            textimg = Image.new('RGBA', (400, 400), colorpallete['colors']['bg2'])
            d2 = ImageDraw.Draw(textimg)
            d2.text((200, 25), "Neurostimulation", fill=colorpallete['fonts']['p3']['color'], anchor="mm", font=colorpallete['fonts']['p3']['font'])
            d2.text((200, 75), subtitletext, fill=colorpallete['fonts']['p3']['color'], anchor="mm", font=colorpallete['fonts']['p3']['font'])
            textimgrot = textimg.rotate(90)
            textimgrot = textimgrot.crop((0, 0, 200, 400))
            finalimg.paste(textimgrot, (50, topspacer), textimgrot.convert('RGBA'))
            first = True
            topspaceradd = 0
            for neurostimulation_technique in neurostimulation_techniques:
                if neurostimulation_technique.lower() == companyinfo[10].lower() or " "+neurostimulation_technique.lower() in companyinfo[10].lower() or testmode:
                    topspaceradd, stimulation_text = wordWrap(neurostimulation_techniques[neurostimulation_technique], 1400)
                    first = False
                    d.text((finalwidth/4, topspacer+75), neurostimulation_technique, fill=colorpallete['fonts']['h3']['color'], anchor="la", font=colorpallete['fonts']['h3']['font'])
                    d.text((finalwidth/4, topspacer+175), stimulation_text, fill=colorpallete['fonts']['p2']['color'], anchor="la", font=colorpallete['fonts']['p2']['font'])
                    topspacer += topspaceradd
            if topspaceradd < 400:
                    topspacer += 400
        d.line([(250, topspacertmp+150), (250, topspacer-150)], fill=colorpallete['colors']['bg1'], width=7)

        # footer
        d.rectangle([(0, topspacer), (finalwidth, topspacer+500)], fill=colorpallete['colors']['bg1'])
        d.text((finalwidth/2, topspacer+100), "BCIwiki.org", fill=colorpallete['fonts']['h1']['color'], anchor="ms", font=colorpallete['fonts']['h1']['font'])
        topspacer += 175

        # crop bottom of image
        w, h = finalimg.size
        finalimgcrop = finalimg.crop((0, 0, w, topspacer))
        
        #finalimgcrop.show()
        finalimgcrop.save("companyprofiles\\"+companyinfo[0]+".png")
        #input()
