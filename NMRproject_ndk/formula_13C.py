from pubchempy import get_compounds
import json
import requests
import sqlite3

def formula_13C(formula_cid):
    no_cspectrum = '13C NMR 스펙트럼 정보가 없는 물질입니다.'
    no_spectrum = '스펙트럼 정보가 없는 물질입니다.'

    url = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/{}/JSON/?response_type=display'.format(
        formula_cid)
    res = requests.get(url)
    json_data = res.json()

    if json_data['Record']['Section'][1]['TOCHeading'] == 'Chemical Safety':
        first_select_data = json_data['Record']['Section'][4]  # dict

        if first_select_data['TOCHeading'] == 'Spectral Information':
            second_select_data = first_select_data['Section'][0]  # dict ,1d nmr

            if second_select_data['TOCHeading'] == '1D NMR Spectra':
                third_select_data = second_select_data['Section']

                if third_select_data[0]['TOCHeading'] == '13C NMR Spectra':
                    fourth_select_data = third_select_data[0]['Information']

                    for i in range(1, len(fourth_select_data)):
                        final_decide = fourth_select_data[i]
                        if final_decide['Name'] == 'Thumbnail':
                            return str(fourth_select_data[i]['Value']['ExternalDataURL'])
                            continue

                        else:
                            continue

                elif third_select_data[1]['TOCHeading'] == '13C NMR Spectra':
                    fourth_select_data = third_select_data[1]['Information']

                    for i in range(1, len(fourth_select_data)):
                        final_decide = fourth_select_data[i]
                        if final_decide['Name'] == 'Thumbnail':
                            return str(fourth_select_data[i]['Value']['ExternalDataURL'])
                            continue

                        else:
                            continue

                else:
                    return no_cspectrum


            else:
                return no_spectrum
        else:
            return no_spectrum

    else:
        first_select_data = json_data['Record']['Section'][3]  # dict

        if first_select_data['TOCHeading'] == 'Spectral Information':
            second_select_data = first_select_data['Section'][0]  # dict ,1d nmr

            if second_select_data['TOCHeading'] == '1D NMR Spectra':
                third_select_data = second_select_data['Section'][0]

                if third_select_data['TOCHeading'] == '13C NMR Spectra':
                    fourth_select_data = third_select_data['Information']

                    for i in range(1, len(fourth_select_data)):
                        final_decide = fourth_select_data[i]
                        if final_decide['Name'] == 'Thumbnail':
                            return str(fourth_select_data[i]['Value']['ExternalDataURL'])
                            continue

                        else:
                            continue

                elif third_select_data[1]['TOCHeading'] == '13C NMR Spectra':
                    fourth_select_data = third_select_data[1]['Information']

                    for i in range(1, len(fourth_select_data)):
                        final_decide = fourth_select_data[i]
                        if final_decide['Name'] == 'Thumbnail':
                            return str(fourth_select_data[i]['Value']['ExternalDataURL'])
                            continue

                        else:
                            continue

                else:
                    return no_cspectrum

            else:
                return no_spectrum

        else:
            return no_spectrum

chemformula = input('분자식을 입력하세요')
improve_chemformula = chemformula.upper()
# 대문자를 입력해도 되게끔 upper함수를 이용함.
# 원래 pubchempy모듈에서는 소문자로 구성된 분자식을 인식하지 못함.
num = 1
for compound in get_compounds(improve_chemformula, 'formula', listkey_count=1, listkey_start=num):
    formula_result = compound
# 분자식 하나에 해당하는 물질이 많은 경우가 있고 이걸 한번에 다 로드하는 경우, 응답오류가 발생하는 현상을 확인함.
# 그렇기 때문에 listkey_count를 이용하여 한번에 불러오는 물질의 개수를 3개로 설정하고
# listkey_start를 1이라는 초기 값이 정해진 변수인 num으로 설정하면서, 물질의 순번을 매겨 start를 1번부터 출력하게끔 만들어줌
formula_cid_result = formula_result.cid
print(formula_cid_result)
# 출력 값이 여러 개일 경우, formula_results에 list가 들어가므로 for문을 적용함.
while True:
    formula_fin_decide = input('원하는 결과가 나오지 않았다면, a를 입력해주세요')
    # 출력 값안에 만약 본인이 원하는 물질이 없을 경우, 어떤 입력값을 받아 출력을 계속하게 만듬(추후에 버튼을 클릭하는 방식으로 만들 것임.)
    if formula_fin_decide == 'a':
        num += 1
        for compound in get_compounds(improve_chemformula, 'formula', listkey_count=1, listkey_start=num):
            formula_result = compound
        # 원하는 값이 없을 경우 출력 순번에 3을 더하고, 그 뒤에 3개의 물질을 출력함.
        formula_cid_result = formula_result.cid
        print(formula_cid_result)
        continue
    else:
        break


conn = sqlite3.connect('formula_13c.db')
cur = conn.cursor()
conn.execute('CREATE TABLE formula_13c(Formula TEXT, cid INTEGER, structure_imageurl TEXT, cnmr_imageurl TEXT)')
query = "insert into formula_13c values(:Formula, :cid, :structure_imageurl, :cnmr_imageurl)"
parameters = ({"Formula":chemformula,
              "cid": formula_cid_result,
              "structure_imageurl": 'https://pubchem.ncbi.nlm.nih.gov/image/imgsrv.fcgi?cid={}&t=l'.format(formula_cid_result),
              "cnmr_imageurl" : formula_13C(formula_cid_result)})
cur.execute(query,parameters)
conn.commit()
conn.close()