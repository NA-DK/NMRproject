from pubchempy import get_compounds
import requests

chemname = input('물질명을 입력해주세요.')
#원하는 물질명을 입력받아 저장받는 변수를 chemname으로 지정
num = 1
name_results = get_compounds(chemname,'name',listkey_count=3,listkey_start=num)
# 만약 cid의 결과가 수십개가 나올 경우가 있음, 그럴 경우 에러가 발생하기 쉬움
# 그렇기 때문에 한번에 산출시키는 물질의 수를 3개로 제한하고, 그 물질들의 산출시작점을 num으로 설정하고, 그 num에 1을 먼저 저장
for name_result in name_results:
    print(name_result.cid)
#예를 들면 2-butane을 입력할 경우, 동일한 물질명을 가진 cid 2개가 산출됨, 만약 1개 이상의 cid가 산출될 경우,
#results는 list의 형태를 띄고 있으므로, for문을 적용함

while True:
    name_fin_decide = input('원하는 결과가 나오지 않았다면, a를 눌러주세요')
    # 앞서 보여준 3개의 결과에 원하는게 있는지 없는지 판단하기 위해 만든 변수
    if name_fin_decide == 'a':
        num += 3
        name_results = get_compounds(chemname,'name',listkey_count=3,listkey_start=num)
        for name_result in name_results:
            print(name_result.cid)
        continue
    else:
        break
