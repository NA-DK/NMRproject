from pubchempy import get_compounds
import json
import requests
import sqlite3

def name_1H(name_cid):
    no_hspectrum ='1H NMR 스펙트럼 정보가 없는 물질입니다.'
    no_spectrum ='스펙트럼 정보가 없는 물질입니다.'

    url = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/{}/JSON/?response_type=display'.format(name_cid)
    res = requests.get(url)
    json_data = res.json()
    # print(type(json_data))
    #69402 61222 137727
    # hydro_spect = json_data['Record']['Section'][4]['Section'][0]['Section'][0]['Information'][2]['Value']['ExternalDataURL'][0]
    # carbo_spect = json_data['Record']['Section'][4]['Section'][0]['Section'][1]['Information'][3]['Value']['ExternalDataURL'][0]
    # print(hydro_spect)
    # print(carbo_spect)

    #hydro spectrum 추출하기

    if json_data['Record']['Section'][1]['TOCHeading'] == 'Chemical Safety':
        first_select_data = json_data['Record']['Section'][4]#dict

        if first_select_data['TOCHeading'] == 'Spectral Information':
            second_select_data = first_select_data['Section'][0]#dict ,1d nmr

            if second_select_data['TOCHeading'] == '1D NMR Spectra':
                third_select_data = second_select_data['Section'][0]

                if third_select_data['TOCHeading'] == '1H NMR Spectra':
                    fourth_select_data = third_select_data['Information']

                    for i in range (1,len(fourth_select_data)):
                        final_decide = fourth_select_data[i]['Name']
                        if final_decide == 'Thumbnail':
                            return str(fourth_select_data[i]['Value']['ExternalDataURL'])
                            continue

                        else:
                            continue


                else:
                    return no_hspectrum


            else:
                return no_spectrum

        else:
            return no_spectrum

    else:
        first_select_data = json_data['Record']['Section'][3]#dict

        if first_select_data['TOCHeading'] == 'Spectral Information':
            second_select_data = first_select_data['Section'][0]#dict ,1d nmr

            if second_select_data['TOCHeading'] == '1D NMR Spectra':
                third_select_data = second_select_data['Section'][0]

                if third_select_data['TOCHeading'] == '1H NMR Spectra':
                    fourth_select_data = third_select_data['Information']

                    for i in range (1,len(fourth_select_data)):
                        final_decide = fourth_select_data[i]['Name']
                        if final_decide == 'Thumbnail':
                            return str(fourth_select_data[i]['Value']['ExternalDataURL'])
                            continue

                        else:
                            continue


                else:
                    return no_hspectrum


            else:
                return no_spectrum

        else:
            return no_spectrum


chemname = input('물질명을 입력해주세요.')
#원하는 물질명을 입력받아 저장받는 변수를 chemname으로 지정
num = 1
name_results = get_compounds(chemname,'name',listkey_count=1,listkey_start=num)

for name_result in name_results:
    name_cid_result = name_result.cid
    print(name_cid_result)


while True:
    name_fin_decide = input('원하는 결과가 나오지 않았다면, a를 눌러주세요')
    # 앞서 보여준 3개의 결과에 원하는게 있는지 없는지 판단하기 위해 만든 변수
    if name_fin_decide == 'a':
        num += 1
        name_results = get_compounds(chemname,'name',listkey_count=1,listkey_start=num)
        for name_result in name_results:
            name_cid_result = name_result.cid
            print(name_cid_result)
        continue
    else:
        break

conn = sqlite3.connect('name_1h.db')
cur = conn.cursor()
conn.execute('CREATE TABLE name_1h(Name TEXT, cid INTEGER, structure_imageurl TEXT, hnmr_imageurl TEXT)')
query = "insert into name_1h values(:Name, :cid, :structure_imageurl, :hnmr_imageurl)"
parameters = ({"Name":chemname,
              "cid": name_cid_result,
              "structure_imageurl": 'https://pubchem.ncbi.nlm.nih.gov/image/imgsrv.fcgi?cid={}&t=l'.format(name_cid_result),
              "hnmr_imageurl" : name_1H(name_cid_result)})
cur.execute(query,parameters)
conn.commit()
conn.close()