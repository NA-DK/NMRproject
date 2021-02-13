import json
import requests

url = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/241/JSON/?response_type=display'
res = requests.get(url)
json_data = res.json()
# print(type(json_data))

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
                        print(fourth_select_data[i]['Value']['ExternalDataURL'])
                        break

                    else:
                        continue


            else:
                print('1H NMR 스펙트럼 정보가 없는 물질입니다.')


        else:
            print('스펙트럼 정보가 없는 물질입니다.')

    else:
        print('스펙트럼 정보가 없는 물질입니다.')

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
                        print(fourth_select_data[i]['Value']['ExternalDataURL'])
                        break

                    else:
                        continue


            else:
                print('1H NMR 스펙트럼 정보가 없는 물질입니다.')


        else:
            print('스펙트럼 정보가 없는 물질입니다.')

    else:
        print('스펙트럼 정보가 없는 물질입니다.')
