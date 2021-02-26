from django.shortcuts import render, get_object_or_404, redirect
from .models import Formula,Name
from .forms import Formula_form
from pubchempy import get_compounds
from PIL import Image
import json
import requests
import sqlite3

# Create your views here.

def formula_1H(formula_cid):
    no_hspectrum ='1H NMR 스펙트럼 정보가 없는 물질입니다.'
    no_spectrum ='스펙트럼 정보가 없는 물질입니다.'

    url = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/{}/JSON/?response_type=display'.format(formula_cid)
    res = requests.get(url)
    json_data = res.json()

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
                            return fourth_select_data[i]['Value']['ExternalDataURL'][0]
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
                            return fourth_select_data[i]['Value']['ExternalDataURL']
                            continue

                        else:
                            continue


                else:
                    return no_hspectrum


            else:
                return no_spectrum

        else:
            return no_spectrum

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
                            return fourth_select_data[i]['Value']['ExternalDataURL'][0]
                            continue

                        else:
                            continue

                elif third_select_data[1]['TOCHeading'] == '13C NMR Spectra':
                    fourth_select_data = third_select_data[1]['Information']

                    for i in range(1, len(fourth_select_data)):
                        final_decide = fourth_select_data[i]
                        if final_decide['Name'] == 'Thumbnail':
                            return fourth_select_data[i]['Value']['ExternalDataURL'][0]
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
                            return fourth_select_data[i]['Value']['ExternalDataURL'][0]
                            continue

                        else:
                            continue

                elif third_select_data[1]['TOCHeading'] == '13C NMR Spectra':
                    fourth_select_data = third_select_data[1]['Information']

                    for i in range(1, len(fourth_select_data)):
                        final_decide = fourth_select_data[i]
                        if final_decide['Name'] == 'Thumbnail':
                            return fourth_select_data[i]['Value']['ExternalDataURL'][0]
                            continue

                        else:
                            continue

                else:
                    return no_cspectrum

            else:
                return no_spectrum

        else:
            return no_spectrum

def formula_create(request):
    if request.method == 'POST':
        form = Formula_form(request.POST)
        if form.is_valid():
            formula = form.save(commit=False)
            formula.cid = get_compounds(formula.formula.upper(),'formula')[0].cid
            formula.structure_imageurl = 'https://pubchem.ncbi.nlm.nih.gov/image/imgsrv.fcgi?cid={}&t=l'.format(formula.cid)
            formula.hnmr_imageurl = str(formula_1H(formula.cid))
            formula.cnmr_imageurl = str(formula_13C(formula.cid))
            formula.save()
            return redirect('nmr:index')
    else:
        form = Formula_form()
    context = {'form': form}
    return render(request, 'nmr/index.html', context)