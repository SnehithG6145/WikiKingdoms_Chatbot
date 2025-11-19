"""
Gazetteer for kingdom intent detection.
Contains all known ways to refer to each kingdom in both languages.
"""

def get_gazetteer():
    """
    Returns gazetteer mapping kingdom names to their various forms
    Structure: {kingdom_label: {primary_names, aliases, rulers, places, entities}}
    """
    
    gazetteer = {
        'Kakatiya': {
            'primary_names': [
                'Kakatiya', 'Kakatiyas', 'Kakatiya dynasty', 'Kakatiya kingdom',
                'కాకతీయ', 'కాకతీయులు', 'కాకతీయ వంశం', 'కాకతీయ రాజ్యం'
            ],
            'aliases': [
                'Kakateya', 'Kakateeya', 'Kakatya', 'Kakatiyar',
                'కాకతీయుల', 'కాకతీయవంశం', 'కాకతీయరాజ్యం'
            ],
            'rulers': [
                'Rudrama Devi', 'Rudramadevi', 'Rani Rudrama Devi',
                'Ganapati Deva', 'Ganapatideva', 'Ganapathi Deva',
                'Prataparudra', 'Pratapa Rudra', 'Prataparudra II',
                'Beta Raja', 'Durga Nripati', 'Mahadeva',
                'రుద్రమదేవి', 'రుద్రమాదేవి', 'రాణి రుద్రమదేవి',
                'గణపతిదేవుడు', 'గణపతి దేవుడు', 'గణపతీశ్వరుడు',
                'ప్రతాపరుద్రుడు', 'ప్రతాపరుద్ర', 'ప్రతాపరుద్రుడు రెండవ',
                'బేతరాజు', 'దుర్గనృపతి', 'మహాదేవుడు'
            ],
            'places': [
                'Warangal', 'Orugallu', 'Ekasila Nagaram', 'Hanumakonda',
                'వరంగల్', 'ఒరుగల్లు', 'ఏకశిల నగరం', 'హనుమకొండ',
                'Thousand Pillar Temple', 'Ramappa Temple', 'Bhadrakali Temple'
            ],
            'entities': [
                'Telugu dynasty', 'Deccan', 'Eastern Deccan',
                'తెలుగు వంశం', 'దక్కన్', 'తూర్పు దక్కన్'
            ]
        },
        
        'Satavahana': {
            'primary_names': [
                'Satavahana', 'Satavahanas', 'Satavahana dynasty', 'Satavahana empire',
                'శాతవాహన', 'శాతవాహనులు', 'శాతవాహన వంశం', 'శాతవాహన సామ్రాజ్యం'
            ],
            'aliases': [
                'Andhra dynasty', 'Andhrabhritya', 'Satvahana', 'Satakarni',
                'ఆంధ్ర వంశం', 'ఆంధ్రభృత్య', 'సాత్వాహన', 'శాతకర్ణి'
            ],
            'rulers': [
                'Gautamiputra Satakarni', 'Gautamiputra Shatakarni',
                'Simuka', 'Satakarni I', 'Krishna', 'Shatakarni II',
                'Pulumavi', 'Vashishtiputra Pulumavi', 'Yajna Sri Satakarni',
                'గౌతమీపుత్ర శాతకర్ణి', 'గౌతమీపుత్ర శతకర్ణి',
                'సిముకుడు', 'శాతకర్ణి మొదటి', 'కృష్ణుడు', 'శతకర్ణి రెండవ',
                'పులుమావి', 'వసిష్ఠీపుత్ర పులుమావి', 'యజ్ఞశ్రీ శాతకర్ణి'
            ],
            'places': [
                'Pratishthana', 'Paithan', 'Amaravati', 'Dhanyakataka',
                'Nashik', 'Junnar', 'Karle', 'Bhaja',
                'ప్రతిష్ఠాన', 'పైఠాణ్', 'అమరావతి', 'ధాన్యకటక',
                'నాసిక్', 'జున్నార్', 'కార్లె', 'భాజా'
            ],
            'entities': [
                'Deccan plateau', 'Ancient India', 'Buddhism patron',
                'దక్కన్ పీఠభూమి', 'ప్రాచీన భారతదేశం', 'బౌద్ధ మత పోషకులు'
            ]
        },
        
        'Chalukya': {
            'primary_names': [
                'Chalukya', 'Chalukyas', 'Chalukya dynasty', 'Chalukya empire',
                'చాలుక్య', 'చాలుక్యులు', 'చాలుక్య వంశం', 'చాలుక్య సామ్రాజ్యం'
            ],
            'aliases': [
                'Badami Chalukyas', 'Eastern Chalukyas', 'Western Chalukyas',
                'Early Chalukyas', 'Later Chalukyas', 'Chalukya-Chola',
                'బాదామి చాలుక్యులు', 'తూర్పు చాలుక్యులు', 'పశ్చిమ చాలుక్యులు',
                'తొలి చాలుక్యులు', 'తరువాతి చాలుక్యులు', 'చాలుక్య చోళులు'
            ],
            'rulers': [
                'Pulakeshin II', 'Pulakesin II', 'Jayasimha I', 'Ranaraga',
                'Kirtivarman I', 'Mangalesha', 'Vijayaditya', 'Vikramaditya I',
                'Vinayaditya', 'Vikramaditya II', 'Kirtivarman II',
                'పులకేశిన్ రెండవ', 'పులకేసిన్ రెండవ', 'జయసింహ మొదటి',
                'రణరాగ', 'కీర్తివర్మన్ మొదటి', 'మంగళేశ', 'విజయాదిత్య',
                'విక్రమాదిత్య మొదటి', 'వినయాదిత్య', 'విక్రమాదిత్య రెండవ'
            ],
            'places': [
                'Badami', 'Vatapi', 'Aihole', 'Pattadakal', 'Mahakuta',
                'Alampur', 'Kalyani', 'Bijapur', 'Vengi',
                'బాదామి', 'వాతాపి', 'ఐహోలె', 'పట్టడకల్', 'మహాకూట',
                'ఆళంపూర్', 'కళ్యాణి', 'బిజాపూర్', 'వేంగి'
            ],
            'entities': [
                'Cave temples', 'Rock-cut architecture', 'Dravidian architecture',
                'గుహా దేవాలయాలు', 'రాతిలో చెక్కిన వాస్తుశిల్పం', 'ద్రావిడ వాస్తుశిల్పం'
            ]
        },
        
        'Vijayanagara': {
            'primary_names': [
                'Vijayanagara', 'Vijayanagar', 'Vijayanagara Empire', 'Vijayanagara Kingdom',
                'విజయనగర', 'విజయనగరం', 'విజయనగర సామ్రాజ్యం', 'విజయనగర రాజ్యం'
            ],
            'aliases': [
                'Karnataka Empire', 'South Indian Empire', 'Karnata Rajya',
                'కర్ణాట సామ్రాజ్యం', 'దక్షిణ భారత సామ్రాజ్యం', 'కర్ణాట రాజ్యం'
            ],
            'rulers': [
                'Harihara I', 'Bukka Raya I', 'Harihara II', 'Bukka Raya II',
                'Deva Raya I', 'Deva Raya II', 'Krishnadevaraya', 'Krishna Deva Raya',
                'Achyuta Deva Raya', 'Sadashiva Raya', 'Rama Raya', 'Tirumala Deva Raya',
                'హరిహరరాయలు మొదటి', 'బుక్కరాయలు మొదటి', 'హరిహరరాయలు రెండవ',
                'బుక్కరాయలు రెండవ', 'దేవరాయలు మొదటి', 'దేవరాయలు రెండవ',
                'కృష్ణదేవరాయలు', 'కృష్ణ దేవరాయలు', 'అచ్యుత దేవరాయలు',
                'సదాశివరాయలు', 'రామరాయలు', 'తిరుమల దేవరాయలు'
            ],
            'places': [
                'Hampi', 'Hospet', 'Virupaksha Temple', 'Vittala Temple',
                'Lotus Mahal', 'Elephant Stables', 'Hazara Rama Temple',
                'హంపి', 'హోస్పేట్', 'విరూపాక్ష దేవాలయం', 'విట్ఠల దేవాలయం',
                'లోటస్ మహల్', 'ఏనుగుల లాయం', 'హజార రామ దేవాలయం'
            ],
            'entities': [
                'Ashtadiggajas', 'Eight poets', 'Telugu literature', 'Carnatic music',
                'అష్టదిగ్గజలు', 'ఎనిమిది కవులు', 'తెలుగు సాహిత్యం', 'కర్ణాటక సంగీతం'
            ]
        },
        
        'Rashtrakuta': {
            'primary_names': [
                'Rashtrakuta', 'Rashtrakutas', 'Rashtrakuta dynasty', 'Rashtrakuta empire',
                'రాష్ట్రకూట', 'రాష్ట్రకూటులు', 'రాష్ట్రకూట వంశం', 'రాష్ట్రకూట సామ్రాజ్యం'
            ],
            'aliases': [
                'Rastrakuta', 'Rashtrakootas', 'Rathod', 'Rathor',
                'రాష్ట్రకూటలు', 'రాష్ట్రకూటవంశం', 'రాఠోడ్', 'రాఠోర్'
            ],
            'rulers': [
                'Dantidurga', 'Krishna I', 'Govinda II', 'Dhruva', 'Govinda III',
                'Amoghavarsha I', 'Krishna II', 'Indra III', 'Amoghavarsha II',
                'Govinda IV', 'Amoghavarsha III', 'Krishna III', 'Khottiga',
                'దంతిదుర్గ', 'కృష్ణ మొదటి', 'గోవింద రెండవ', 'ధ్రువ', 'గోవింద మూడవ',
                'అమోఘవర్ష మొదటి', 'కృష్ణ రెండవ', 'ఇంద్ర మూడవ', 'అమోఘవర్ష రెండవ',
                'గోవింద నాలుగవ', 'అమోఘవర్ష మూడవ', 'కృష్ణ మూడవ', 'ఖొట్టిగ'
            ],
            'places': [
                'Manyakheta', 'Malkhed', 'Ellora', 'Kailasa Temple', 'Elephanta',
                'Nashik', 'Latur', 'Gulbarga', 'Kalyani',
                'మాన్యఖేట', 'మాల్ఖేద్', 'ఎల్లోరా', 'కైలాస దేవాలయం', 'ఎలిఫెంటా',
                'నాసిక్', 'లాతూర్', 'గుల్బర్గా', 'కళ్యాణి'
            ],
            'entities': [
                'Rock-cut architecture', 'Kannada literature', 'Kavirajamarga',
                'రాతిలో చెక్కిన వాస్తుశిల్పం', 'కన్నడ సాహిత్యం', 'కవిరాజమార్గం'
            ]
        },
        
        'Chola': {
            'primary_names': [
                'Chola', 'Cholas', 'Chola dynasty', 'Chola empire',
                'చోళ', 'చోళులు', 'చోళ వంశం', 'చోళ సామ్రాజ్యం'
            ],
            'aliases': [
                'Imperial Cholas', 'Medieval Cholas', 'Later Cholas',
                'సామ్రాజ్య చోళులు', 'మధ్యయుగ చోళులు', 'తరువాతి చోళులు'
            ],
            'rulers': [
                'Vijayalaya', 'Aditya I', 'Parantaka I', 'Rajaraja Chola I',
                'Rajendra Chola I', 'Rajadhiraja Chola', 'Rajendra Chola II',
                'Virarajendra', 'Adhirajendra', 'Kulothunga Chola I',
                'Vikrama Chola', 'Kulothunga Chola II', 'Rajaraja Chola II',
                'విజయాలయ', 'ఆదిత్య మొదటి', 'పరాంతక మొదటి', 'రాజరాజ చోళుడు మొదటి',
                'రాజేంద్ర చోళుడు మొదటి', 'రాజాధిరాజ చోళుడు', 'రాజేంద్ర చోళుడు రెండవ',
                'వీరరాజేంద్ర', 'అధిరాజేంద్ర', 'కులోత్తుంగ చోళుడు మొదటి',
                'విక్రమ చోళుడు', 'కులోత్తుంగ చోళుడు రెండవ', 'రాజరాజ చోళుడు రెండవ'
            ],
            'places': [
                'Thanjavur', 'Tanjore', 'Gangaikonda Cholapuram', 'Chidambaram',
                'Kumbakonam', 'Darasuram', 'Brihadisvara Temple', 'Airavatesvara Temple',
                'తంజావూర్', 'తంజోర్', 'గంగైకొండ చోళపురం', 'చిదంబరం',
                'కుంభకోణం', 'దరాసురం', 'బృహదీశ్వర దేవాలయం', 'ఐరావతేశ్వర దేవాలయం'
            ],
            'entities': [
                'Tamil literature', 'Naval power', 'Southeast Asia', 'Temple architecture',
                'Bronze sculptures', 'Maritime trade', 'Dravidian architecture',
                'తమిళ సాహిత్యం', 'నౌకాబలం', 'ఆగ్నేయాసియా', 'దేవాలయ వాస్తుశిల్పం',
                'కాంస్య శిల్పాలు', 'సముద్ర వాణిజ్యం', 'ద్రావిడ వాస్తుశిల్పం'
            ]
        }
    }
    
    return gazetteer

def get_all_protected_words():
    """Get all words that should be protected from spell correction"""
    gazetteer = get_gazetteer()
    protected = set()
    
    for kingdom_data in gazetteer.values():
        for category in ['primary_names', 'aliases', 'rulers', 'places', 'entities']:
            if category in kingdom_data:
                for name in kingdom_data[category]:
                    # Add the full name
                    protected.add(name.lower())
                    # Add individual words from multi-word names
                    words = name.lower().split()
                    protected.update(words)
    
    return protected

def get_kingdom_aliases():
    """Get mapping of all aliases to canonical kingdom names"""
    gazetteer = get_gazetteer()
    aliases = {}
    
    for kingdom, data in gazetteer.items():
        # Add all variations as keys pointing to kingdom
        for category in ['primary_names', 'aliases', 'rulers', 'places']:
            if category in data:
                for name in data[category]:
                    aliases[name.lower()] = kingdom
    
    return aliases
