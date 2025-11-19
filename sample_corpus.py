"""
Sample corpus data structure for the kingdom history chatbot.
In production, this should be replaced with actual Wikipedia data.
"""

sample_data = [
        # Kakatiya Kingdom - English
        {
            'paragraph_id': 'kakatiya_en_001',
            'text': 'The Kakatiya dynasty was a Telugu dynasty that ruled most of eastern Deccan region comprising present day Telangana and Andhra Pradesh from 1083 to 1323 CE. Their capital was Orugallu, now known as Warangal. The dynasty reached its zenith under the rule of Ganapati Deva and his daughter Rudrama Devi, followed by grandson Prataparudra.',
            'language': 'en',
            'kingdom_label': 'Kakatiya'
        },
        {
            'paragraph_id': 'kakatiya_en_002', 
            'text': 'Rudrama Devi was one of the most prominent rulers of the Kakatiya dynasty and among the few ruling queens in Indian history. She ruled from 1263 to 1289 CE. She was known for her military prowess and administrative skills. She successfully defended her kingdom against invasions from the Yadavas of Devagiri and the Hoysalas.',
            'language': 'en',
            'kingdom_label': 'Kakatiya'
        },
        {
            'paragraph_id': 'kakatiya_en_003',
            'text': 'The Thousand Pillar Temple in Warangal is one of the finest examples of Kakatiya architecture. Built during the reign of Rudrama Devi in 1163 CE, it showcases the unique architectural style of the dynasty. The temple complex features intricate stone carvings and sculptures that reflect the artistic excellence of the period.',
            'language': 'en', 
            'kingdom_label': 'Kakatiya'
        },
         {
            'paragraph_id': 'kakatiya_en_004',
            'text': 'The Thousand Pillar Temple in Warangal is one of the finest examples of Kakatiya architecture. Built during the reign of Rudrama Devi in 1163 CE, it showcases the unique architectural style of the dynasty. The temple complex features intricate stone carvings and sculptures that reflect the artistic excellence of the period.',
            'language': 'en', 
            'kingdom_label': 'Kakatiya'
        },

        
        # Kakatiya Kingdom - Telugu
        {
            'paragraph_id': 'kakatiya_te_001',
            'text': 'కాకతీయ వంశం 1083 నుండి 1323 వరకు తూర్పు దక్కన్ ప్రాంతంలో పాలించిన తెలుగు రాజవంశం. వారి రాజధాని ఒరుగల్లు, ఇప్పుడు వరంగల్ అని పిలుస్తారు. గణపతి దేవుడు మరియు అతని కుమార్తె రుద్రమదేవి, ఆ తర్వాత మనవడు ప్రతాపరుద్రుడి పాలనలో వంశం శిఖరాగ్రానికి చేరుకుంది.',
            'language': 'te',
            'kingdom_label': 'Kakatiya'
        },
        {
            'paragraph_id': 'kakatiya_te_002',
            'text': 'రుద్రమదేవి కాకతీయ వంశంలోని అత్యంత ప్రముఖ పాలకురాలు మరియు భారత చరిత్రలో అరుదైన మహిళా పాలకులలో ఒకరు. ఆమె 1263 నుండి 1289 వరకు పాలించారు. ఆమె యుద్ధ నైపుణ్యం మరియు పరిపాలనా నైపుణ్యాలకు ప్రసిద్ధి చెందింది. దేవగిరి యాదవులు మరియు హోయసాళుల దండయాత్రలను విజయవంతంగా తిప్పికొట్టింది.',
            'language': 'te',
            'kingdom_label': 'Kakatiya'
        },
        
        # Satavahana Kingdom - English
        {
            'paragraph_id': 'satavahana_en_001',
            'text': 'The Satavahana dynasty was an ancient Indian dynasty based in the Deccan region. They ruled from around 2nd century BCE to 2nd century CE. The dynasty was founded by Simuka and reached its peak under Gautamiputra Satakarni. Their capital cities included Pratishthana (modern Paithan) and Amaravati.',
            'language': 'en',
            'kingdom_label': 'Satavahana'
        },
        {
            'paragraph_id': 'satavahana_en_002',
            'text': 'Gautamiputra Satakarni was the most famous ruler of the Satavahana dynasty. He ruled in the 1st century CE and was known for his military conquests and patronage of Buddhism. He defeated the Scythian rulers and expanded the empire significantly. His achievements are recorded in the Nashik inscription by his mother Gautami Balasri.',
            'language': 'en',
            'kingdom_label': 'Satavahana'
        },
        
        # Satavahana Kingdom - Telugu
        {
            'paragraph_id': 'satavahana_te_001',
            'text': 'శాతవాహన వంశం దక్కన్ ప్రాంతంలో స్థాపించబడిన పురాతన భారతీయ రాజవంశం. వారు దాదాపు క్రీ.పూ. 2వ శతాబ్దం నుండి క్రీ.శ. 2వ శతాబ్దం వరకు పాలించారు. సిముకుడు ఈ వంశాన్ని స్థాపించాడు మరియు గౌతమీపుత్ర శాతకర్ణి కాలంలో శిఖరాగ్రానికి చేరుకుంది. వారి రాజధానులు ప్రతిష్ఠాన (ఇప్పటి పైఠాన్) మరియు అమరావతి.',
            'language': 'te',
            'kingdom_label': 'Satavahana'
        },
        
        # Chalukya Kingdom - English  
        {
            'paragraph_id': 'chalukya_en_001',
            'text': 'The Chalukya dynasty ruled large parts of southern and central India between the 6th and 12th centuries. The dynasty had three distinct branches: the Badami Chalukyas, the Eastern Chalukyas, and the Western Chalukyas. They were known for their architectural achievements, including the temples at Badami, Aihole, and Pattadakal.',
            'language': 'en',
            'kingdom_label': 'Chalukya'
        },
        {
            'paragraph_id': 'chalukya_en_002',
            'text': 'Pulakeshin II was one of the greatest rulers of the Badami Chalukya dynasty. He ruled from 610 to 642 CE and was known for his military prowess. He successfully resisted the northern expansion of Harsha Vardhana and established diplomatic relations with the Persian empire. His court was visited by the Chinese pilgrim Hiuen Tsang.',
            'language': 'en',
            'kingdom_label': 'Chalukya'
        },
        
        # Chalukya Kingdom - Telugu
        {
            'paragraph_id': 'chalukya_te_001', 
            'text': 'చాలుక్య వంశం 6వ మరియు 12వ శతాబ్దాల మధ్య దక్షిణ మరియు మధ్య భారతదేశంలోని పెద్ద భాగాలను పాలించింది. వంశానికి మూడు విభిన్న శాఖలు ఉన్నాయి: బాదామి చాలుక్యులు, తూర్పు చాలుక్యులు మరియు పశ్చిమ చాలుక్యులు. బాదామి, ఐహోలె మరియు పట్టడకల్లోని దేవాలయాలతో సహా వారి వాస్తు శిల్ప విజయాలకు ప్రసిద్ధి చెందారు.',
            'language': 'te',
            'kingdom_label': 'Chalukya'
        },
        
        # Vijayanagara Kingdom - English
        {
            'paragraph_id': 'vijayanagara_en_001',
            'text': 'The Vijayanagara Empire was a South Indian empire based in the Deccan Plateau. It was established in 1336 by Harihara I and his brother Bukka Raya I. The empire reached its peak under Krishnadevaraya in the early 16th century. The capital city Vijayanagara, now known as Hampi, was one of the largest cities in the world during its peak.',
            'language': 'en',
            'kingdom_label': 'Vijayanagara'
        },
        {
            'paragraph_id': 'vijayanagara_en_002',
            'text': 'Krishnadevaraya was the most famous ruler of the Vijayanagara Empire, ruling from 1509 to 1529 CE. He was a patron of art and literature, and his court was home to the Ashtadiggajas, eight great poets in Telugu literature. He was also a successful military commander who expanded the empire and defeated several rival kingdoms.',
            'language': 'en',
            'kingdom_label': 'Vijayanagara'
        },
        
        # Vijayanagara Kingdom - Telugu
        {
            'paragraph_id': 'vijayanagara_te_001',
            'text': 'విజయనగర సామ్రాజ్యం దక్కన్ పీఠభూమిలో స్థాపించబడిన దక్షిణ భారత సామ్రాజ్యం. దీనిని 1336లో హరిహరరాయలు మరియు అతని సోదరుడు బుక్కరాయలు స్థాపించారు. 16వ శతాబ్దం ప్రారంభంలో కృష్ణదేవరాయల కాలంలో సామ్రాజ్యం శిఖరాగ్రానికి చేరుకుంది. రాజధాని విజయనగరం, ఇప్పుడు హంపి అని పిలుస్తారు, దాని అత్యున్నత కాలంలో ప్రపంచంలోని అతిపెద్ద నగరాలలో ఒకటి.',
            'language': 'te',
            'kingdom_label': 'Vijayanagara'
        },
        
        # Rashtrakuta Kingdom - English
        {
            'paragraph_id': 'rashtrakuta_en_001',
            'text': 'The Rashtrakuta dynasty was a royal dynasty ruling large parts of the Indian subcontinent between the 6th and 10th centuries CE. They ruled from Manyakheta in present-day Karnataka. The dynasty reached its zenith under rulers like Amoghavarsha I and Indra III. They were great patrons of art, architecture, and literature.',
            'language': 'en',
            'kingdom_label': 'Rashtrakuta'
        },
        
        # Rashtrakuta Kingdom - Telugu  
        {
            'paragraph_id': 'rashtrakuta_te_001',
            'text': 'రాష్ట్రకూట వంశం 6వ మరియు 10వ శతాబ్దాల మధ్య భారత ఉపఖండంలోని పెద్ద భాగాలను పాలించిన రాజవంశం. వారు ప్రస్తుత కర్ణాటకలోని మాన్యఖేట నుండి పాలించారు. అమోఘవర్ష మొదలైనవారు మరియు ఇంద్ర మూడవ వంటి పాలకుల కాలంలో వంశం శిఖరాగ్రానికి చేరుకుంది. వారు కళ, వాస్తుశిల్పం మరియు సాహిత్యానికి గొప్ప పోషకులు.',
            'language': 'te',
            'kingdom_label': 'Rashtrakuta'
        },
        
        # Chola Kingdom - English
        {
            'paragraph_id': 'chola_en_001', 
            'text': 'The Chola dynasty was a Tamil thalassocratic empire of southern India, one of the longest-ruling dynasties in the world. They ruled from the 9th to 13th centuries CE. The dynasty reached its peak under Rajaraja Chola I and his son Rajendra Chola I. They were known for their naval power, trade networks, and magnificent temple architecture.',
            'language': 'en',
            'kingdom_label': 'Chola'
        },
        {
            'paragraph_id': 'chola_en_002',
            'text': 'Rajaraja Chola I was one of the greatest rulers of the Chola dynasty, ruling from 985 to 1014 CE. He expanded the Chola empire significantly and built the magnificent Brihadisvara Temple in Thanjavur. He also established a powerful navy that dominated the seas around South India and Southeast Asia.',
            'language': 'en',
            'kingdom_label': 'Chola'
        },
        
        # Chola Kingdom - Telugu
        {
            'paragraph_id': 'chola_te_001',
            'text': 'చోళ వంశం దక్షిణ భారతదేశంలోని తమిళ సముద్ర సామ్రాజ్యం, ప్రపంచంలోని అత్యంత దీర్ఘకాలం పాలించిన వంశాలలో ఒకటి. వారు 9వ నుండి 13వ శతాబ్దాల వరకు పాలించారు. రాజరాజ చోళుడు మరియు అతని కుమారుడు రాజేంద్ర చోళుడి కాలంలో వంశం శిఖరాగ్రానికి చేరుకుంది. వారు నౌకాబల, వాణిజ్య నెట్‌వర్కులు మరియు అద్భుతమైన దేవాలయ వాస్తుశిల్పానికి ప్రసిద్ధి చెందారు.',
            'language': 'te',
            'kingdom_label': 'Chola'
        }
    ]

# Kakatiya (add _005 .. _008)
sample_data += [
    {
        'paragraph_id': 'kakatiya_en_005',
        'text': 'The Kakatiyas rose from Western Chalukya feudatories to sovereign rulers under Prola II and Rudradeva. Their capital at Orugallu (Warangal) was planned with concentric fortifications, granite gateways, and elaborate moats.',
        'language': 'en',
        'kingdom_label': 'Kakatiya'
    },
    {
        'paragraph_id': 'kakatiya_en_006',
        'text': 'Ganapati Deva and Rudrama Devi extended the empire and promoted irrigation through large tanks, while the port of Motupalli facilitated trade with Southeast Asia. Rudrama Devi is revered as one of the very few ruling queens in Indian history.',
        'language': 'en',
        'kingdom_label': 'Kakatiya'
    },
    {
        'paragraph_id': 'kakatiya_en_007',
        'text': 'Kakatiya architecture, seen at the Ramappa Temple and Warangal, is marked by star-shaped platforms, intricate carvings, and distinctive gateway pillars (kirtistambhas). Their patronage strengthened Telugu literature and identity.',
        'language': 'en',
        'kingdom_label': 'Kakatiya'
    },
    {
        'paragraph_id': 'kakatiya_en_008',
        'text': 'The Kakatiya state fell in 1323 CE to the Tughlaqs after long sieges. Their legacy includes advanced water-management systems and a tolerant polity that supported Shaivism, Vaishnavism, and local cults alongside Jain and Buddhist traditions.',
        'language': 'en',
        'kingdom_label': 'Kakatiya'
    },
]

# Satavahana (add _003)
sample_data += [
    {
        'paragraph_id': 'satavahana_en_003',
        'text': 'The Satavahanas connected the Deccan to northern India and the Roman world via western ports. Inscriptions in Prakrit and early Telugu, coinage reforms, and patronage of both Buddhism and Brahmanism defined their polity.',
        'language': 'en',
        'kingdom_label': 'Satavahana'
    },
]

# Chalukya (add _003)
sample_data += [
    {
        'paragraph_id': 'chalukya_en_003',
        'text': 'Monuments at Aihole, Pattadakal, and Badami illustrate the evolution from rock-cut to structural temples. The Pattadakal complex is a UNESCO World Heritage site, reflecting synthesis of Nagara and Dravida styles.',
        'language': 'en',
        'kingdom_label': 'Chalukya'
    },
]

# Vijayanagara (add _003)
sample_data += [
    {
        'paragraph_id': 'vijayanagara_en_003',
        'text': 'Vijayanagara’s capital (Hampi) featured advanced urban planning, bazaars, waterworks, and granite fortifications. Foreign travelers like Domingo Paes praised its wealth. The empire declined after the 1565 Battle of Talikota.',
        'language': 'en',
        'kingdom_label': 'Vijayanagara'
    },
]

# Rashtrakuta (add _002, _003)
sample_data += [
    {
        'paragraph_id': 'rashtrakuta_en_002',
        'text': 'Amoghavarsha I’s reign favored learning, peace, and Jainism; he authored the Kavirajamarga, the earliest known Kannada literary work. The Rashtrakutas were noted for religious tolerance and administrative sophistication.',
        'language': 'en',
        'kingdom_label': 'Rashtrakuta'
    },
    {
        'paragraph_id': 'rashtrakuta_en_003',
        'text': 'The Kailasa Temple at Ellora, excavated from a single rock, is the Rashtrakutas’ crowning architectural achievement and a masterpiece of Indian art, reflecting Shaiva devotion and engineering prowess.',
        'language': 'en',
        'kingdom_label': 'Rashtrakuta'
    },
]

# Chola (add _003)
sample_data += [
    {
        'paragraph_id': 'chola_en_003',
        'text': 'Chola power peaked under Rajaraja I and Rajendra I, extending to Sri Lanka, the Maldives, and parts of Southeast Asia. Their temple architecture at Thanjavur and Gangaikonda Cholapuram showcases towering vimanas and precise symmetry.',
        'language': 'en',
        'kingdom_label': 'Chola'
    },
]



import json
import re
from pathlib import Path


def simple_sentence_tokenize(text):
    """Lightweight sentence splitter using punctuation boundaries."""
    if not text:
        return []
    # Split on punctuation followed by whitespace; keep abbreviations intact by limiting to .,!,?
    parts = re.split(r'(?<=[.!?])\s+', text.strip())
    return [p.strip() for p in parts if p.strip()]

# Read your text file
with open("cleaned_english_text.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Split the text into sentences (English heuristic)
sentences = simple_sentence_tokenize(text)
len(sentences)
#en(sentences)
paras = [" ".join(sentences[i:i+4]) for i in range(0, len(sentences), 4)]

print(paras[60])
#i have formed paras 
len(paras)
from nlp.language_detector import LanguageDetector
dict_paras = dict()
lang = 0
det = LanguageDetector()
langs = []
for i in range(404):
    lang = det.detect_language(paras[i])
    langs.append(lang['language'])

with open("paragraphs_3","w",encoding = "utf-8") as f:
    f.write("\n;;;\n".join(paras))
Kakatiya = ["The kakatiya dynasty (IAST: Kākatīya) was a Telugu dynasty that ruled most of eastern Deccan region in present-day India between 12th and 14th centuries. Their territory comprised much of the present day Telangana and Andhra Pradesh, and parts of eastern Karnataka, northern Tamil Nadu, and southern Odisha. Their capital was Orugallu, now known as Warangal. Early Kakatiya rulers served as feudatories to Rashtrakutas and Western Chalukyas for more than two centuries."
    ,
    "They assumed sovereignty under Prataparudra I in 1163 CE by suppressing other Chalukya subordinates in the Telangana region. Ganapati Deva (r. 1199–1262) significantly expanded Kakatiya lands during the 1230s and brought under Kakatiya control the Telugu-speaking lowland delta areas around the Godavari and Krishna rivers. Ganapati Deva was succeeded by Rudrama Devi (r. 1262–1289) who is one of the few queens in Indian history."
    ,
    "Marco Polo, who visited India around 1289–1293, made note of Rudrama Devi's rule and nature in flattering terms. She successfully repelled the attacks of Yadavas (Seuna) of Devagiri into the Kakatiyan territory. In 1303, Alauddin Khalji, the emperor of the Delhi Sultanate invaded the Kakatiya territory which ended up as a disaster for the Turks."
    ,
    "The Kakatiya dynasty, which ruled from approximately 1000 to 1323 CE, was a Telugu dynasty that played a vital role in South Indian history. Initially feudatories to the Western Chalukyas of Kalyani, they declared independence around 1151 CE under Kakatiya Prola II, taking advantage of Chalukya decline. Their capital was initially at Hanumakonda but was later shifted to Orugallu (modern-day Warangal), which became a powerful fortified city. The dynasty expanded its territory to include present-day Telangana, Andhra Pradesh, parts of eastern Karnataka, northern Tamil Nadu, and southern Odisha."
    ,
    "Rudrama Devi (1262–1289), one of India's few female monarchs, ruled with administrative skill and military prowess, notably repulsing the Yadava attacks. The dynasty faced invasions from the Delhi Sultanate under Alauddin Khalji and later Tughlaq rulers. Despite fierce resistance, the Kakatiya dynasty fell in 1323 after the siege of Warangal and the capture of Prataparudra II, marking the end of their sovereign rule. The Kakatiyas are remembered for promoting Telugu language and culture, pioneering irrigation infrastructure, and pioneering a distinctive style of temple architecture."
    ,
    "Key rulers include Rudradeva (Prataparudra I), who consolidated power and constructed large irrigation tanks such as Ramappa and Bhadrakali lakes and laid the foundation for Warangal's fortifications. Ganapati Deva (r. 1199–1262) was the most powerful ruler who expanded the kingdom substantially, from Kanchipuram in the south to the Godavari basin in the north and Raichur Doab in the west. He promoted agriculture through large-scale irrigation projects and made the port of Motupalli a major trading hub, fostering prosperity. The exquisite Ramappa Temple was built during his reign by his general Recharla Rudra and is now a UNESCO World Heritage Site."]

lang_kakatiya = []
for i in Kakatiya :
    lang = det.detect_language(i)
    lang_kakatiya.append(lang['language'])

    

# Satavahana
Satavahana = [
"The Satavahanas (; Sādavāhana or Sātavāhana, IAST: Sātavāhana), also referred to as the Andhras (also Andhra-bhṛtyas or Andhra-jatiyas) in the Puranas, were an ancient Indian dynasty. Most modern scholars believe that the Satavahana rule began in the late 2nd century BCE and lasted until the early 3rd century CE, although some assign the beginning of their rule to as early as the 3rd century BCE based on the Puranas, but uncorroborated by archaeological evidence. The Satavahana kingdom mainly comprised the present-day Andhra Pradesh, Telangana, and Maharashtra. At different times, their rule extended to parts of modern Gujarat, Madhya Pradesh, and Karnataka.",
"The dynasty had different capital cities at different times, including Pratishthana (Paithan) and Amaravati (Dharanikota). The origin of the dynasty is uncertain, but according to the Puranas, their first king overthrew the Kanva dynasty. In the post-Maurya era, the Satavahanas established peace in the Deccan region and resisted the onslaught of foreign invaders. In particular their struggles with the Saka (Western Satraps) went on for a long time.",
"Notable for being early issuers of state coinage, the Satavahanas played a critical role in bridging cultures between the Indo-Gangetic plains and southern India. They followed Mauryan administrative traditions and included hereditary rulers, feudatories, and ministers in their governance. The Satavahanas were patrons of Brahmanism and Mahayana Buddhism, performed Vedic sacrifices, and made generous donations to Buddhist monasteries. Their territory included fertile river valleys, facilitating trade and agriculture. They controlled significant Indian sea ports, dominating trade with the Roman Empire, as noted in the Periplus of the Erythraean Sea."
]

lang_satavahana = []
for i in Satavahana:
    lang = det.detect_language(i)
    lang_satavahana.append(lang['language'])


# Chalukya
Chalukya = [
"The Chalukya dynasty was a Classical Indian dynasty that ruled large parts of southern and central India between the 6th and the 12th centuries. During this period, they ruled as three related yet individual dynasties. The earliest dynasty, known as the \"Badami Chalukyas\", ruled from Vatapi (modern Badami) from the middle of the 6th century.",
"The Badami Chalukyas began to assert their independence at the decline of the Kadamba kingdom of Banavasi and rapidly rose to prominence during the reign of Pulakeshin II. After the death of Pulakeshin II, the Eastern Chalukyas became an independent kingdom in the eastern Deccan. They ruled from Vengi until about the 11th century.",
"Pulakeshin II, arguably the most famous Chalukya ruler, extended the empire across the Deccan, defeated northern and southern rivals, and demonstrated military prowess. The dynasty split into Eastern and Western branches, the former ruling the coastal Andhra region with Telugu literary patronage, and the latter reviving fortunes in the 10th century and fostering Kannada literature as well as Sanskrit scholarship."
]

lang_chalukya = []
for i in Chalukya:
    lang = det.detect_language(i)
    lang_chalukya.append(lang['language'])


# Vijayanagara
Vijayanagara = [
"The Vijayanagara Empire, also known as the Karnata Kingdom, was a late medieval Hindu empire that ruled much of southern India. It was established in 1336 by the brothers Harihara I and Bukka Raya I of the Sangama dynasty, belonging to the Yadava clan of Chandravamsa lineage. The empire rose to prominence as a culmination of attempts by the southern powers to ward off Muslim invasions by the end of the 13th century.",
"At its peak in the early 16th century under Krishnadevaraya, it subjugated almost all of Southern India's ruling dynasties and pushed the Deccan sultanates beyond the Tungabhadra-Krishna River doab region, in addition to annexing the Gajapati Empire (Odisha) up to the Krishna River, becoming one of the most prominent states in India."
]

lang_vijayanagara = []
for i in Vijayanagara:
    lang = det.detect_language(i)
    lang_vijayanagara.append(lang['language'])


# Rashtrakuta
Rashtrakuta = [
"The Rashtrakuta Empire (Kannada: [raːʂʈrɐkuːʈɐ]) was a royal Indian polity ruling large parts of the Indian subcontinent between the 6th and 10th centuries. The earliest known Rashtrakuta inscription is a 7th-century copper plate grant detailing their rule from Manapur, a city in Central or West India.",
"At their peak the Rashtrakutas of Manyakheta ruled a vast empire stretching from the Ganges River and Yamuna River doab in the north to Kanyakumari in the south, a fruitful time of political expansion, architectural achievements and famous literary contributions."
]

lang_rashtrakuta = []
for i in Rashtrakuta:
    lang = det.detect_language(i)
    lang_rashtrakuta.append(lang['language'])


# Chola
Chola = [
"The Chola dynasty was a Tamil dynasty originating from Southern India. At its height, it ruled over the Chola Empire, an expansive maritime empire.",
"The earliest datable references to the Chola are from inscriptions dated to the 3rd century BCE during the reign of Ashoka of the Maurya Empire. The Chola empire was at its peak and achieved imperialism under the Medieval Cholas in the mid-9th century CE."
]

lang_chola = []
for i in Chola:
    lang = det.detect_language(i)
    lang_chola.append(lang['language'])


    
def get_sample_corpus():
    """
    Returns sample corpus data in the expected format.
    Each item should have: paragraph_id, text, language, kingdom_label
    """
    def build_corpus_from_kingdoms(kingdom_data):
        sample_dat = []
        for kingdom, data in kingdom_data.items():
            paras = data["paragraphs"]
            langs = data["languages"]

            for i, (para, lang) in enumerate(zip(paras, langs), start=1):
                # Create ID in format → kingdom_lang_index (e.g. kakatiya_en_001)
                paragraph_id = f"{kingdom.lower()}_{lang}_{i:03d}"
                entry = {
                    "paragraph_id": paragraph_id,
                    "text": para.strip(),
                    "language": lang,
                    "kingdom_label": kingdom
                }
                sample_dat.append(entry)
        return sample_dat

    kingdom_data = {
        "Kakatiya": {"paragraphs": Kakatiya, "languages": lang_kakatiya},
        "Satavahana": {"paragraphs": Satavahana, "languages": lang_satavahana},
        "Chalukya": {"paragraphs": Chalukya, "languages": lang_chalukya},
        "Vijayanagara": {"paragraphs": Vijayanagara, "languages": lang_vijayanagara},
        "Rashtrakuta": {"paragraphs": Rashtrakuta, "languages": lang_rashtrakuta},
        "Chola": {"paragraphs": Chola, "languages": lang_chola},
    }
    sample_dat = build_corpus_from_kingdoms(kingdom_data)
    sample_data.extend(sample_dat)
    # --- Append Telugu paragraphs from the labeled JSON (use first detected kingdom) ---
    try:
        labeled_path = Path(__file__).resolve().parents[0] / 'data' / 'labeled_paragraphs.json'
        if labeled_path.exists():
            with open(labeled_path, 'r', encoding='utf-8') as f:
                labeled = json.load(f)

            # For each labeled paragraph, if it's Telugu (has Telugu chars) and kingdoms exist,
            # append to sample_data using the first kingdom label.
            for key, item in sorted(labeled.items(), key=lambda x: int(x[0])):
                para = item.get('paragraph', '').strip()
                kingdoms = item.get('kingdoms', [])
                if not para or not kingdoms:
                    continue

                # quick Telugu heuristics: presence of Telugu Unicode block
                if not any('\u0C00' <= ch <= '\u0C7F' for ch in para):
                    continue

                kingdom = kingdoms[0]

                # build a paragraph id similar to other entries, avoid collision by counting existing
                existing_count = sum(1 for e in sample_data if e.get('kingdom_label') == kingdom and e.get('language') == 'te')
                paragraph_id = f"{kingdom.lower()}_te_{existing_count+1:03d}"

                entry = {
                    'paragraph_id': paragraph_id,
                    'text': para,
                    'language': 'te',
                    'kingdom_label': kingdom
                }
                sample_data.append(entry)
    except Exception:
        # keep function robust if file missing or malformed
        pass

    return sample_data

# Function to get corpus statistics
def get_corpus_stats(corpus_data):
    """Get statistics about the corpus"""
    stats = {
        'total_paragraphs': len(corpus_data),
        'by_language': {},
        'by_kingdom': {},
        'kingdoms': set()
    }
    
    for item in corpus_data:
        lang = item['language']
        kingdom = item['kingdom_label']
        
        # Language stats
        if lang not in stats['by_language']:
            stats['by_language'][lang] = 0
        stats['by_language'][lang] += 1
        
        # Kingdom stats
        if kingdom not in stats['by_kingdom']:
            stats['by_kingdom'][kingdom] = {'total': 0, 'by_language': {}}
        stats['by_kingdom'][kingdom]['total'] += 1
        
        if lang not in stats['by_kingdom'][kingdom]['by_language']:
            stats['by_kingdom'][kingdom]['by_language'][lang] = 0
        stats['by_kingdom'][kingdom]['by_language'][lang] += 1
        
        stats['kingdoms'].add(kingdom)
    
    stats['kingdoms'] = list(stats['kingdoms'])
    return stats
