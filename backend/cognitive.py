import cognitive_face as CF

# Provide your own key
_key = ''
attributes = 'age,gender,glasses,emotion'

def get_face_info(url):
    CF.Key.set(_key)
    face_info = []
    for info in CF.face.detect(image=url,attributes=attributes):
        face_info.append(info['faceAttributes'])
    return face_info

def get_face_keywords(url):
    face_info = get_face_info(url)
    all_keywords = []
    young_gender_map = {'male':'boy','female':'Virgo'}
    gender_map = {'male':'man','female':'woman'}
    glasses_map = {'ReadingGlasses':'geek','Sunglasses':'sunglasses'}
    emotion_map = {'anger':'angry','happiness':'smile','contempt':'rolling','disgust':'unamused','fear':'fear','neutral':'neutral','sadness':'sad','surprise':'surprised'}
    happy_stage = {'slightly':0.1,'relaxed':0.5,'blush':0.7,'laugh':0.95}
    anger_stage = {'mad':0.9,'pouting':0.95}
    fear_stage = {'scared':0.9,'scream':0.95}
    sad_stage = {'pensive':0.8,'crying':0.9,'sob':0.95}
    stage_map = {'happiness':happy_stage,'anger':anger_stage,'fear':fear_stage,'sadness':sad_stage}
    for info in face_info:
        keywords = []
        if info['age'] <= 6:
            keywords.extend(('baby','young'))
        elif info['age'] <= 15:
            keywords.extend(('young',young_gender_map[info['gender']]))
        elif info['age'] > 60:
            keywords.extend(('old',gender_map[info['gender']]))
        else:
            best_mark = -1
            for key,value in info['emotion'].items():
                if value > best_mark:
                    best_mark = value
                    emotion = key
            if emotion == 'neutral' and info['emotion']['happiness'] > 0.1:
                emotion = 'happiness'
            keywords.extend(('face',emotion_map[emotion]))
            min_dis = 1
            try:
                for key,value in stage_map[emotion].items():
                    if 0 <= info['emotion'][emotion] - value <= min_dis:
                        min_dis = info['emotion'][emotion] - value
                        best_match = key
                if min_dis != 1:
                    keywords.append(best_match)
            except:
                pass

            if emotion == 'happiness':
                if info['glasses'] in glasses_map:
                    keywords.extend((glasses_map[info['glasses']],glasses_map[info['glasses']]))
        #print keywords
        all_keywords.append(keywords)
    return all_keywords
